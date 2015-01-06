import sys
import win32api
from code import actualCode
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
        runButton.clicked.connect(self.startRun)
        cancelButton.clicked.connect(QtCore.QCoreApplication.instance().quit)

        global error_files
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

    def startRun(self):

        sources = []
        destination = str(self.destTextField.toPlainText())
        createfiles = False

        self.bar.showMessage("Backup in progress...")
        if error_files.isChecked():
            createfiles = True

        for i in drivelist:
            if i.isChecked():
                sources.append(drives[drivelist.index(i)])

        errors = actualCode(sources, destination, createfiles)
        self.bar.showMessage("Backup complete.  Errors: " + str(errors))


def main():

    app = QtGui.QApplication(sys.argv)
    ex = Application()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

