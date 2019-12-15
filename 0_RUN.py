import subprocess, os
from parameters import *
from new_folder import createFolder

if os.path.exists("temp.py"):
  os.remove("temp.py")

##CREATE NEW FOLDER:

createFolder(work_dir+"\IFD")

##SOFT DOCKING:

subprocess.run(["py","1_chain.py"],shell=True)

import sys
sys.path.append(work_dir)
from temp import *

if chain_del!='':
  subprocess.run([chimera_path, "--nogui", "--script","2_select_chain.py"],shell=True)
else:
  subprocess.run([chimera_path, "--nogui", "--script","2a_select_chain.py"],shell=True)


subprocess.run(["python2", "3_prepare_receptor4.py", "-r", receptor+".pdb", "-A", "hydrogens", "-U", "nphs_lps_waters"],shell=True)

subprocess.run(["python2", "4_prepare_ligand4.py", "-l",ligand+".pdb", "-A", "hydrogens", "-U", "nphs"],shell=True)

subprocess.run(["python2", "5_prepare_gpf4.py", "-l", ligand+".pdbqt","-r", receptor+".pdbqt",
                 "-o", "grid.gpf", "-p", "gridcenter="+x+","+y+","+z,"-p","npts="+x_dim+","+y_dim+","+z_dim,"-p","spacing="+spacing],shell=True)


subprocess.run([grid_path, "-p", work_dir+"/"+"grid.gpf", "-l", work_dir+"/"+"grid.glg"],cwd=work_dir,shell=True)


subprocess.run(["python2", "6_prepare_dpf42.py", "-l", ligand+".pdbqt", "-r", receptor+".pdbqt", "-o", receptor+".dpf"],shell=True)


subprocess.run([dock_path, "-p", receptor+".dpf", "-l", receptor+".dlg"],cwd=work_dir,shell=True)


subprocess.run(["python2", "7_write_models.py", "-d", receptor+".dlg", "-o", "docking"],shell=True)


name='docking_'
for i in range(0,10):
    subprocess.run(["python2", "8_pdbqt_to_pdb.py", "-f", name+str(i)+".pdbqt"],shell=True)

subprocess.run([chimera_path, "--nogui","--silent","--script","9_combine.py"])    

args = ['10_MODELLER.py']
cmd = ['py'] + args
with open(work_dir+'\dope.log', "w") as outfile:
    subprocess.run(cmd, stdout=outfile,shell=True)

subprocess.run(["py","11_dope_ads_distance.py"],shell=True)

##ADD NEW PATH

subprocess.run(["py","add_new_path.py"],shell=True)

import parameters
from six.moves import reload_module
reload_module(parameters)

from parameters import *

import sys
sys.path.append(work_dir)
import temp
reload_module(temp)
from temp import *


##IFD:

subprocess.run([chimera_path, "--nogui", "--script","12_prep_sec_docking.py"],shell=True)


subprocess.run(["python2", "3_prepare_receptor4.py", "-r", best_pose+"_ligremove.pdb", "-A", "hydrogens", "-U", "nphs_lps_waters"],shell=True)

subprocess.run(["python2", "4_prepare_ligand4.py", "-l",ligand+".pdb", "-A", "hydrogens", "-U", "nphs"],shell=True)

subprocess.run(["python2", "5_prepare_gpf4.py", "-l", ligand+".pdbqt","-r", best_pose+"_ligremove.pdbqt",
                 "-o", "grid.gpf", "-p", "gridcenter="+x+","+y+","+z,"-p","npts="+x_dim+","+y_dim+","+z_dim,"-p","spacing="+spacing],shell=True)

subprocess.run(["py","6a_smooth_off.py"],shell=True)


subprocess.run([grid_path, "-p", work_dir+"/"+"grid.gpf", "-l", work_dir+"/"+"grid.glg"], cwd=work_dir, shell=True)

subprocess.run(["python2", "6_prepare_dpf42.py", "-l", ligand+".pdbqt", "-r", best_pose+"_ligremove.pdbqt", "-o", best_pose+"_ligremove.dpf"],shell=True)


subprocess.run([dock_path, "-p", best_pose+"_ligremove.dpf", "-l", best_pose+"_ligremove.dlg"], cwd=work_dir, shell=True)


subprocess.run(["python2", "7_write_models.py", "-d", best_pose+"_ligremove.dlg", "-o", "docking"],shell=True)


name='docking_'
for i in range(0,10):
    subprocess.run(["python2", "8_pdbqt_to_pdb.py", "-f", name+str(i)+".pdbqt"],shell=True)

subprocess.run([chimera_path, "--nogui","--silent","--script","9a_combine2.py"])


subprocess.run(["py", "13_ads.py"],shell=True)

subprocess.run([chimera_path, "--gui","--silent","--script","14_visualization.py"])


    
    




