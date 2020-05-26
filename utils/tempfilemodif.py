import glob
import os
import sys 
folder = sys.argv[1]


files = glob.glob(folder+  '/*/*.dat*')
print(files)
line = '<collection>'
for file in files:
    with open(file,'r+') as f:        
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)
        f.seek(0, os.SEEK_END)
        f.write("</collection>")
