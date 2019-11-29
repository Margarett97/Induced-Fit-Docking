#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
from chimera import *
from chimera import runCommand as rc
from 13_ads import pose

from parameters import *

os.chdir(work_dir)

#ref='1dbb'


#rc("open #0 " + ref + ".pdb")
rc("open #1 " + pose + ".pdb")
rc("color cyan #1")
rc("color gold :/isHet")
##rc("alias site1 #0:"+ligand)
##rc("alias site2 #1:"+ligand)
##rc("alias both site1 | site2")
##rc("match iterate 2.0 site2 site1")
##rc("focus both")
rc("color byhet")
rc("transparency 75,r")


rc("2dlabels create 1 text PROTEIN color gold xpos 0 ypos 0.1")
rc("2dlabels create 2 text LIGAND color cyan xpos 0 ypos 0.07")
