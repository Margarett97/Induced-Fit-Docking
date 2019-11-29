import subprocess, os
from new_folder import *



##DZIAŁANIE W KONKRETNEJ ŚCIEŻCE


##SOFT DOCKING:

subprocess.call(["C:/Program Files/Chimera 1.13.1/bin/chimera", "--nogui", "--script","C:/Users/pukma/Desktop/IFD/1_select_chain.py"])
subprocess.call(["python2", "2_prepare_receptor4.py", "-r", "1rth.pdb", "-A", "hydrogens", "-U", "nphs_lps_waters"])
subprocess.call(["python2", "3_prepare_ligand4.py", "-l", "612.pdb", "-A", "hydrogens", "-U", "nphs"])
subprocess.call(["python2", "4_prepare_gpf4.py", "-l", "612.pdbqt","-r", "1rth.pdbqt", "-o", "grid.gpf", "-p", "gridcenter=0.745,-35.615,25.516"])
subprocess.call(["C:/Program Files (x86)/The Scripps Research Institute/Autodock/4.2.6/autogrid4", "-p", "grid.gpf", "-l", "grid.glg"])
subprocess.call(["python2", "5_prepare_dpf42.py", "-l", "612.pdbqt", "-r", "1rth.pdbqt", "-o", "1rth.dpf"])
subprocess.call(["C:/Program Files (x86)/The Scripps Research Institute/Autodock/4.2.6/autodock4", "-p", "1rth.dpf", "-l", "1rth.dlg"])
subprocess.call(["bash","6_split_dockings.sh"]) ##TRZEBA TO ZMIENIĆ ŻEBY NIE TRZEBA BYŁO WPISYWAĆ PARAMETRÓW
subprocess.call(["C:/Program Files/Chimera 1.13.1/bin/chimera", "--nogui", "--script","C:/Users/pukma/Desktop/PROTOKOL/7_combine.py"])
subprocess.call(["py", "8_MODELLER.py", ">","dope.log"])
subprocess.call(["py", "9_dope_ads_distance.py"])
subprocess.call(["C:/Program Files/Chimera 1.13.1/bin/chimera", "--nogui", "--script","C:/Users/pukma/Desktop/PROTOKOL/10_RMSD.py"])

## Create new folder for IFD files:

#createFolder('C:/Users/pukma/Desktop/test/new')

##IFD:

#TRZEBA OPEACOWAĆ SKRYPT KTÓRY SAM WYBIERA NAJLEPSZĄ POZĘ I USUWA LIGAND
