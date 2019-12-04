import os
from parameters import *

os.chdir(work_dir)

with open("grid.gpf","r") as f:
    a=f.read()
    repl=a.replace("smooth 0.5","")
    with open("grid.gpf","w") as g:
        g.write(repl)
    
    
    
