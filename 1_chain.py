# script selects the receptor subunits to be deleted.
#It also specifies the receptor chain
#and changes the name of the receptor if it is a number

from parameters import *
import os

os.chdir(work_dir)


names=[]
new=[]
with open(receptor+".pdb","r") as f:
    line=f.readlines()
    for i, lines in enumerate(line):
        if lines.startswith("ATOM"):
            a=lines.split()
            if a[4]!= chain:
                delete=a[4]
                names.append(delete)
                for val in names:
                    if val not in new:
                        new.append(val)

                    
            else:
                chain_del=''

if len(new)>1:
    chain_del=",.".join(new)
elif len(new)==1:
    chain_del=" ".join(new)


with open("temp.py","a") as t:
    name="chain_del='"
    t.write(name+chain_del+"'\n")


        

#select ligand chain ID:   
with open(ligand+".pdb","r+") as f:
    line=f.readlines()
    for i, lines in enumerate(line):
        if lines.startswith("HETATM"):
            a=lines.split()
            lig_chain=a[4] 
    with open("temp.py","a") as p:
        name="lig_chain='"
        p.write(name+lig_chain+"'\n")

        
        os.chdir(work_dir)
        ID=a[3] #change numeric ligand ID to string

        with open(ligand+".pdb","r") as t:
            if ID.isnumeric():
    
                data=t.read()
                repl=data.replace(ID,"UNK")

                with open(ligand+".pdb","w") as g:

                    g.write(repl)

