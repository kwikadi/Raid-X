import sys
import os
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        runButton = QtGui.QPushButton("OK")
        cancelButton = QtGui.QPushButton("Cancel")
        browseButton = QtGui.QPushButton("Browse")
        textEdit = QtGui.QTextEdit()
        dest_folder = QtGui.QLabel('Please select the destination folder:', self)
        textEdit.setMaximumHeight(dest_folder.sizeHint().height()*2)

        browseButton.clicked.connect(self.showDialog)
        runButton.clicked.connect(self.actualCode)

        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(runButton)
        hbox.addWidget(cancelButton)

        h2box = QtGui.QHBoxLayout()
        h2box.addWidget(textEdit)
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

        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open folder', '/home')

        self.textEdit.setText()

    def actualCode(self):
        f = open('workfile.txt', 'w+')

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
    ex = Example()
    sys.exit(app.exec_())



if __name__ == '__main__':
    main()
