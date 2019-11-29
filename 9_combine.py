#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
from chimera import *
from chimera import runCommand as rc

path='C:/Users/pukma/Desktop/test'
os.chdir(path)
chain_lig='C'
chain='A'

#Łączenie białka z ligandem

ligand_dok="1rthA_612"
for j in range(0,10):
    rc("open #0 " + receptor + ".pdb")
    rc("delete H")
    rc("changechains "+chain_lig+","+chain+" "+chain+","+chain) 
    rc("resrenumber 1 #2")
    rc("write #2 pose" +str(j) + ".pdb")
    rc("close all")





    


 
    



























    
