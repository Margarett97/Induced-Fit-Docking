import os
from parameters import *

os.chdir(work_dir)

#select ligand chain ID:   
with open(ligand+".pdb","r+") as f:
    line=f.readline().split()
    lig_chain=line[2] 
with open("temp.py","a") as p:
    name="lig_chain='"
    p.write(name+lig_chain+"'\n")

        
    os.chdir(work_dir)
    ID=line[1] #change numeric ligand ID to string
    if ID.isnumeric():

        data=f.read()
        repl=data.replace(ID,"UNK")

        with open(f,"w") as g:

            g.write(repl)
     
#select protein chain ID: 
with open(receptor+".pdb",'r') as r:
    line=r.readlines()
    for i,lines in enumerate(line):
        if lines.startswith('ATOM'):
            a=lines.split()
            chain=a[4]
with open("temp.py","a") as p:
    name="chain='"
    p.write(name+chain+"'\n")














           
    
    
