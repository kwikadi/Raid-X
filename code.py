import scandir
import os
from PyQt4 import QtCore
import time

class Background(QtCore.QThread):
    def __init__(self,source,dest,create=True):
        super(Background, self).__init__()
        self.sources = source
        self.createfiles = create
        self.destination = dest
        self.errors = 0

    def run(self):

        data_gui = []

        new_destination = self.destination + "\Raid_X_Backup"

        if not os.path.exists(new_destination): os.makedirs(new_destination)

        if self.createfiles:
            fileUnable = open(new_destination+"\\unabletocreate.txt", "w")

        for source in self.sources:
            for root, dirs, files in scandir.walk(source, topdown=False):

                for name in dirs:
                    time.sleep(0.1)
                    destpath = os.path.join(root, name)
                    destpath = destpath.replace(source,"")
                    temp_source = source.replace(":", " drive")
                    destpath = new_destination + "\\" + temp_source + "\\" + destpath

                    if not os.path.exists(destpath):
                        os.makedirs(destpath)

                for name in files:
                    destpath = os.path.join(root, name)
                    destpath = destpath.replace(source,"")
                    temp_source = source.replace(":", " drive")
                    destpath = new_destination + "\\" + temp_source + "\\" + destpath
                    try:
                        f_temp = open(destpath,"w").close()

                    except:
                        if self.createfiles:
                            fileUnable.write(os.path.join(root,name) + "\n")
                        self.errors+=1
                
        if self.createfiles:
            fileUnable.close()

        self.errors = -1



