#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import os
from chimera import *
from chimera import runCommand as rc
from names import chain_del, receptor_pdb,  path

os.chdir(path)

replyobj.status("Processing" + receptor_pdb + ".pdb")
rc("open "+ receptor_pdb) 
rc("delete : ."+chain_del)
rc("select :/isHet " ) 
rc("delete selected")
rc("write #0 "+receptor_pdb+".pdb")
rc("close all")





