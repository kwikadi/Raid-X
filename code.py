import sys
import os
from PyQt4 import QtGui, QtCore

class Gooey(QtGui.QWidget):

    def __init__(self):
        super(Gooey, self).__init__()

        self.initUI()

    def initUI(self):

        runButton = QtGui.QPushButton("Run")
        cancelButton = QtGui.QPushButton("Cancel")
        browseButton = QtGui.QPushButton("Browse")
        self.destTextField = QtGui.QTextEdit("F:")
        dest_folder = QtGui.QLabel('Please select the destination folder:', self)
        self.destTextField.setMaximumHeight(dest_folder.sizeHint().height()*2)

        browseButton.clicked.connect(self.showDialog)
        runButton.clicked.connect(self.actualCode)
        cancelButton.clicked.connect(QtCore.QCoreApplication.instance().quit)

        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(runButton)
        hbox.addWidget(cancelButton)

        h2box = QtGui.QHBoxLayout()
        h2box.addWidget(self.destTextField)
        h2box.addWidget(browseButton)

        h3box = QtGui.QHBoxLayout()
        h3box.addWidget(dest_folder)

        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(h3box)
        vbox.addLayout(h2box)
        #vbox.addSpacing(self,4)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Raid-X')
        self.show()


    def showDialog(self):

        fname = QtGui.QFileDialog.getExistingDirectory(self, 'Open folder', 'C:')

        self.destTextField.setPlainText(fname)

    def actualCode(self):

        destination = self.destTextField.toPlainText()
        f = open('files.txt', 'w+')
        print destination
        for root, dirs, files in os.walk("F:\\", topdown=True):

            for name in files:

                a = os.path.join(root, name)
                trial = list(a)
                trial[1] = "+"
                a = "G:\\" + "".join(trial) + ".txt"
                #make file here.
                #Add basic data about file, like where it was taken from and when it was last modified.
                f.write(a + "\n")

            for name in dirs:

                a = os.path.join(root, name)
                trial = list(a)
                trial[1] = "+"
                a = "G:\\" + "".join(trial)
                f.write(a + "\n")
                if not os.path.exists(a):
                    os.makedirs(a)

        f.close()
        QtCore.QCoreApplication.instance().quit()

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Gooey()
    sys.exit(app.exec_())



if __name__ == '__main__':
    main()
