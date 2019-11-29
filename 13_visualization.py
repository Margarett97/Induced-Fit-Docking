#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
from chimera import *
from chimera import runCommand as rc

path='C:/Users/pukma/Desktop/test'
ref='1dbb'
pose='pose9'
ligand='STR'
os.chdir(path)

rc("open #0 " + ref + ".pdb")
rc("open #1 " + pose + ".pdb")
rc("color gold #0")
rc("color cyan #1")
rc("alias site1 #0:"+ligand)
rc("alias site2 #1:"+ligand)
rc("alias both site1 | site2")
rc("match iterate 2.0 site2 site1")
rc("focus both")
rc("color byhet")
rc("transparency 100,r")


rc("2dlabels create 1 text MODEL color gold xpos 0 ypos 0.1")
rc("2dlabels create 2 text REFERENCE color cyan xpos 0 ypos 0.07")
