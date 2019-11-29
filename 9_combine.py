#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import sys
sys.path.append(work_dir)
from temp import *
import os
from chimera import *
from chimera import runCommand as rc
from parameters import *





os.chdir(work_dir)


#Łączenie białka z ligandem

ligand_dok="docking_"
for j in range(1,11):
    rc("open #0 " + receptor + ".pdb")
    rc("delete H")
    rc("open #1 " + ligand_dok+str(j)+".pdb")
    rc("delete H")
    rc("resrenumber 999 #1")
    rc("combine #0,1  ")
    rc("changechains "+lig_chain+","+chain+" "+chain+","+chain) 
    rc("resrenumber 1 #2")
    rc("write #2 pose" +str(j) + ".pdb")
    rc("close all")
    





    


 
    



























    
