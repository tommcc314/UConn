import os
files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith(".py")]
newfile = open("PythonFiles.txt", "w")
for f in files:
    newfile.write(f + "\n")
newfile.close()