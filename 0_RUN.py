import subprocess, os
from parameters import *
from new_folder import createFolder
##
##
##if os.path.exists("temp.py"):
##  os.remove("temp.py")
##
####CREATE NO FOLDER:
##
##createFolder(work_dir+"\IFD")
## 
##
####SOFT DOCKING:
##
##if chain_del=='':
##  subprocess.call([chimera_path, "--nogui", "--script","1a_select_chain.py"],shell=True)
##else:
##  subprocess.call([chimera_path, "--nogui", "--script","1_select_chain.py"],shell=True)
##
##subprocess.call(["py","2_chain.py"],shell=True)
##
##subprocess.call(["python2", "3_prepare_receptor4.py", "-r", receptor+".pdb", "-A", "hydrogens", "-U", "nphs_lps_waters"],shell=True)
##
##subprocess.call(["python2", "4_prepare_ligand4.py", "-l",ligand+".pdb", "-A", "hydrogens", "-U", "nphs"],shell=True)
##
##subprocess.call(["python2", "5_prepare_gpf4.py", "-l", ligand+".pdbqt","-r", receptor+".pdbqt",
##                 "-o", "grid.gpf", "-p", "gridcenter="+x+","+y+","+z,"-p","npts="+x_dim+","+y_dim+","+z_dim,"-p","spacing="+spacing],shell=True)
##
##
##subprocess.check_call([grid_path, "-p", work_dir+"/"+"grid.gpf", "-l", work_dir+"/"+"grid.glg"],cwd=work_dir,shell=True)
##
##subprocess.call(["python2", "6_prepare_dpf42.py", "-l", ligand+".pdbqt", "-r", receptor+".pdbqt", "-o", receptor+".dpf"],shell=True)
##
##
##subprocess.check_call([dock_path, "-p", receptor+".dpf", "-l", receptor+".dlg"],cwd=work_dir,shell=True)
##
##subprocess.call(["python2", "7_write_models.py", "-d", receptor+".dlg", "-o", "docking"],shell=True)
##
##
##name='docking_'
##for i in range(0,10):
##    subprocess.call(["python2", "8_pdbqt_to_pdb.py", "-f", name+str(i)+".pdbqt"],shell=True)
##
##subprocess.call([chimera_path, "--nogui","--silent","--script","9_combine.py"])    
##
##args = ['10_MODELLER.py']
##cmd = ['py'] + args
##with open(work_dir+'\dope.log', "w") as outfile:
##    subprocess.call(cmd, stdout=outfile,shell=True)
##
##subprocess.call(["py","11_dope_ads_distance.py"],shell=True)
##
####ADD NEW PATH
##
##subprocess.call(["py","add_new_path.py"],shell=True)
##
##
##import sys
##sys.path.append(work_dir)
##from temp import *
##
####IFD:
##
##subprocess.call([chimera_path, "--nogui", "--script","12_prep_sec_docking.py"],shell=True)
##
##subprocess.call(["python2", "3_prepare_receptor4.py", "-r", best_pose+"_ligremove.pdb", "-A", "hydrogens", "-U", "nphs_lps_waters"],shell=True)
##
##subprocess.call(["python2", "4_prepare_ligand4.py", "-l",ligand+".pdb", "-A", "hydrogens", "-U", "nphs"],shell=True)
##
##subprocess.call(["python2", "5_prepare_gpf4.py", "-l", ligand+".pdbqt","-r", best_pose+"_ligremove.pdbqt",
##                 "-o", "grid.gpf", "-p", "gridcenter="+x+","+y+","+z,"-p","npts="+x_dim+","+y_dim+","+z_dim,"-p","spacing="+spacing],shell=True)
##
##subprocess.call(["py","6a_smooth_off.py"],shell=True)


import sys
sys.path.append(work_dir)
from temp import *

subprocess.check_call([grid_path, "-p", work_dir+"/"+"grid.gpf", "-l", work_dir+"/"+"grid.glg"],cwd=work_dir,shell=True)

subprocess.call(["python2", "6_prepare_dpf42.py", "-l", ligand+".pdbqt", "-r", best_pose+"_ligremove.pdbqt", "-o", best_pose+"_ligremove.dpf"],shell=True)


subprocess.check_call([dock_path, "-p", best_pose+"_ligremove.dpf", "-l", best_pose+"_ligremove.dlg"],cwd=work_dir,shell=True)

import sys
sys.path.append(work_dir)
from temp import *

subprocess.call(["python2", "7_write_models.py", "-d", best_pose+"_ligremove.dlg", "-o", "docking"],shell=True)


name='docking_'
for i in range(0,10):
    subprocess.call(["python2", "8_pdbqt_to_pdb.py", "-f", name+str(i)+".pdbqt"],shell=True)

subprocess.call([chimera_path, "--nogui","--silent","--script","9a_combine2.py"])


subprocess.call(["py", "13_ads.py"],shell=True)

subprocess.call([chimera_path, "--gui","--silent","--script","14_visualization.py"])


    
    




