import subprocess, os
from parameters import *


##SOFT DOCKING:
subprocess.call([chimera_path, "--nogui", "--script","1_select_chain.py"],shell=True)

subprocess.call(["py","2_chain.py"],shell=True)

subprocess.call(["python2", "3_prepare_receptor4.py", "-r", receptor+".pdb", "-A", "hydrogens", "-U", "nphs_lps_waters"],shell=True)

subprocess.call(["python2", "4_prepare_ligand4.py", "-l",ligand+".pdb", "-A", "hydrogens", "-U", "nphs"],shell=True)

subprocess.call(["python2", "5_prepare_gpf4.py", "-l", ligand+".pdbqt","-r", receptor+".pdbqt",
                 "-o", "grid.gpf", "-p", "gridcenter="+x+","+y+","+z,"-p","npts="+x_dim+","+y_dim+","+z_dim,"-p","spacing="+spacing],shell=True)


subprocess.check_call([grid_path, "-p", work_dir+"/"+"grid.gpf", "-l", work_dir+"/"+"grid.glg"],cwd=work_dir)

subprocess.call(["python2", "6_prepare_dpf42.py", "-l", ligand+".pdbqt", "-r", receptor+".pdbqt", "-o", receptor+".dpf"],shell=True)


subprocess.check_call([dock_path, "-p", receptor+".dpf", "-l", receptor+".dlg"],cwd=work_dir)

subprocess.call(["python2", "7_write_models.py", "-d", receptor+".dlg", "-o", "docking"])


name='docking_'
for i in range(1,11):
    subprocess.call(["python2", "8_pdbqt_to_pdb.py", "-f", name+str(i)+".pdbqt"],shell=True)

subprocess.call([chimera_path, "--nogui", "--script","9_combine.py"])    



