import sys
import win32api
import os
import scandir
from PyQt4 import QtGui, QtCore


class Application(QtGui.QMainWindow):
    def __init__(self, parent=None):

        super(Application, self).__init__(parent)
        self.gui = Gooey(self)
        self.setCentralWidget(self.gui)
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Raid-X')
        self.setWindowIcon(QtGui.QIcon('icon.svg'))
        self.show()


class Gooey(QtGui.QWidget):

    def __init__(self,parent):
        super(Gooey, self).__init__(parent)

        self.initUI()

    def initUI(self):

        self.bar = QtGui.QStatusBar(self)
        self.bar.showMessage("Ready")

        runButton = QtGui.QPushButton("Run")
        cancelButton = QtGui.QPushButton("Cancel")
        browseButton = QtGui.QPushButton("Browse")
        self.destTextField = QtGui.QTextEdit("G:")
        destFolderLabel = QtGui.QLabel('Please select the destination folder:', self)
        self.destTextField.setMaximumHeight(destFolderLabel.sizeHint().height()*2)
        driveSelectLabel = QtGui.QLabel('Please select the drives you want to backup:', self)

        global drivelist
        drivelist = []
        global drives
        drives = win32api.GetLogicalDriveStrings()
        drives = drives.split('\000')[:-1]
        for i in drives:
            drivelist.append(QtGui.QCheckBox(i))

        browseButton.clicked.connect(self.showDialog)
        runButton.clicked.connect(self.actualCode)
        cancelButton.clicked.connect(QtCore.QCoreApplication.instance().quit)

        error_files = QtGui.QCheckBox('Create file listing files that couldn\'t be created.')

        h7box = QtGui.QHBoxLayout()
        h7box.addWidget(error_files)

        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(runButton)
        hbox.addWidget(cancelButton)

        h2box = QtGui.QHBoxLayout()
        h2box.addWidget(self.destTextField)
        h2box.addWidget(browseButton)

        h3box = QtGui.QHBoxLayout()
        h3box.addWidget(destFolderLabel)

        h4box = QtGui.QHBoxLayout()
        for i in drivelist:
            h4box.addWidget(i)

        h5box = QtGui.QHBoxLayout()
        h5box.addWidget(driveSelectLabel)

        h6box = QtGui.QHBoxLayout()
        h6box.addWidget(self.bar)

        vbox = QtGui.QVBoxLayout()
        vbox.addLayout(h5box)
        vbox.addLayout(h4box)
        vbox.addLayout(h3box)
        vbox.addLayout(h2box)
        vbox.addLayout(h7box)
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        vbox.addLayout(h6box)

        self.setLayout(vbox)

    def showDialog(self):

        fname = QtGui.QFileDialog.getExistingDirectory(self, 'Open folder', 'G:')

        self.destTextField.setPlainText(fname)

    def actualCode(self):

        filess=0
        folders=0
        errors=0
        self.bar.showMessage("Backup in progress...")
        sources = []
        for i in drivelist:
            if i.isChecked():
                sources.append(drives[drivelist.index(i)])

        destination = self.destTextField.toPlainText()
        new_destination = str(destination) + "\Backup"

        if not os.path.exists(new_destination): os.makedirs(new_destination)

        fileUnable = open(new_destination+"\\unabletocreate.txt", "w")

        for source in sources:
            for root, dirs, files in scandir.walk(source, topdown=False):

                '''for name in dirs:

                    destpath = os.path.join(root, name)
                    destpath = destpath.replace(source,"")
                    temp_source = source.replace(":", " drive")
                    destpath = new_destination + "\\" + temp_source + "\\" + destpath

                    if not os.path.exists(destpath):
                        os.makedirs(destpath)
                    folders+=1'''

                for name in files:

                    destpath = os.path.join(root, name)
                    destpath = destpath.replace(source,"")
                    temp_source = source.replace(":", " drive")
                    destpath = new_destination + "\\" + temp_source + "\\" + destpath
                    try:
                        f_temp = open(destpath,"w").close()
                        filess += 1

                    except:
                        fileUnable.write(os.path.join(root,name) + "\n")
                        errors+=1

        fileUnable.close()

        self.bar.showMessage("Backup complete. Files: " + str(filess) +" , Folders: " + str(folders) + " , Errors: " + str(errors))

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Application()
    sys.exit(app.exec_())



if __name__ == '__main__':
    main()
