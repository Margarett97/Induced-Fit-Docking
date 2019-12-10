#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#Script preparing the selected protein subunit (without chain removal)

import os
from chimera import *
from chimera import runCommand as rc
from parameters import *

os.chdir(work_dir)

rc("open "+ receptor +".pdb") 
rc("select :/isHet " ) 
rc("delete selected")
rc("write #0 "+receptor+".pdb")
rc("close all")





