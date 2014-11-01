import os
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
