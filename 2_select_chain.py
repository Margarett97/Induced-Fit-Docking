#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#Script preparing the selected protein subunit

import os
from chimera import *
from chimera import runCommand as rc
from parameters import *


os.chdir(work_dir)

import sys
sys.path.append(work_dir)
from temp import *



rc("open "+ receptor +".pdb") 
rc("delete :."+chain_del)
rc("select :/isHet " ) 
rc("delete selected")
rc("write #0 "+receptor+".pdb")
rc("close all")





