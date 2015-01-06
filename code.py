import scandir
import os

def actualCode(sources,destination,createfiles=True):

    filess=0
    folders=0
    errors=0
    data_gui = []

    new_destination = destination + "\Backup"

    if not os.path.exists(new_destination): os.makedirs(new_destination)

    if createfiles:
        fileUnable = open(new_destination+"\\unabletocreate.txt", "w")

    for source in sources:
        for root, dirs, files in scandir.walk(source, topdown=False):

            for name in dirs:

                destpath = os.path.join(root, name)
                destpath = destpath.replace(source,"")
                temp_source = source.replace(":", " drive")
                destpath = new_destination + "\\" + temp_source + "\\" + destpath

                if not os.path.exists(destpath):
                    os.makedirs(destpath)
                folders+=1

            for name in files:

                destpath = os.path.join(root, name)
                destpath = destpath.replace(source,"")
                temp_source = source.replace(":", " drive")
                destpath = new_destination + "\\" + temp_source + "\\" + destpath
                try:
                    f_temp = open(destpath,"w").close()
                    filess += 1

                except:
                    if createfiles:
                        fileUnable.write(os.path.join(root,name) + "\n")
                    errors+=1
    if createfiles:
        fileUnable.close()

    data_gui.append(filess)
    data_gui.append(folders)
    data_gui.append(errors)

    return data_gui


