#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import os
from names import path, replyLOG, ligand



lig=open(path+'/'+ligand+".pdb",'r')
ligLines=lig.readlines()

count=0
for j,line in enumerate(ligLines):
    if line.startswith('HETATM'):
        count+=1
lig=count
start=('RMSD between'+str(lig))


log = open(path+"/"+replyLOG+".txt", "r")
logLines = log.readlines()
RMSDvalue=[]
for i, li in enumerate(logLines):
    if li.startswith(start):
        value = line.split(" ")[6]
    
