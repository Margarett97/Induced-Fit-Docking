import os



os.chdir("C:/Users/pukma/Desktop/test")
file="612"

#select chain ID:   
with open(file+".pdb","r+") as f:
    line=f.readline().split(" ")
    lig_chain=line[6]

    ID=line[4] #change numeric ligand ID to string
    if ID.isnumeric():

        data=f.read()
        repl=data.replace(ID,"UNK")



        with open(file+".pdb","w") as g:

            g.write(repl)
    
    


















           
    
    
