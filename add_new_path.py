from parameters import *

with open("parameters.py","r") as f:
        a=f.read()
        b=a.replace(work_dir,work_dir+"/IFD")
        f.close()
        with open("parameters.py","w") as g:
            g.write(b)
