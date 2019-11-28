#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
from chimera import *
from chimera import runCommand as rc

from names import path, receptor, chain, chain_lig
os.chdir(path)

#Łączenie białka z ligandem

ligand_dok="my_docking.00"
for j in range(0,10):
    replyobj.status("Processing " + ligand_dok + str(j) + ".pdb")
    rc("open #0 " + receptor + ".pdb")
    rc("delete H")
    rc("open #1 " + ligand_dok+str(j)+".pdb")
    rc("resrenumber 999 #1")
    rc("combine #0,1  ")
    rc("changechains "+chain_lig+","+chain+" "+chain+","+chain) 
    rc("resrenumber 1 #2")
    rc("write #2 pose" +str(j) + ".pdb")
    rc("close all")





    


 
    



























    
