#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os




lig=open(path+'/'+ligand+".pdb",'r')
ligLines=lig.readlines()

count=0
for j,line in enumerate(ligLines):
    if line.startswith('HETATM'):
        count+=1
lig=count
start=('RMSD between'+str(lig))


with open(path+"/replyLOG.txt","r") as f:
    a=f.read()
    if a.startswith(start):
        print(a)

    
