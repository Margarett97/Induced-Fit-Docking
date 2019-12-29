#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
from chimera import *
from chimera import runCommand as rc
from chimera.tkgui import saveReplyLog as rl

path="C:/Users/pukma/Desktop/Dokowanie/18_thymidine_kinase_b/0_RMSD"
ref='1kim'
model='pose2'
ligand='THM'


os.chdir(path+'/')
currentPose=0

replyobj.status("Processing "+model+".pdb")  
rc("open #0 " + ref + ".pdb")
rc("open #1 " + model + ".pdb")
rc("matchmaker #0 #1 ")
RMSD = rc("rmsd #1:"+ligand+ " #0:"+ligand) 
rl('I.txt')



