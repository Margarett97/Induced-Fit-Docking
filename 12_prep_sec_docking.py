#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
from chimera import *
from chimera import runCommand as rc

from parameters import *

import sys
sys.path.append(work_dir)
from temp import best_pose

os.chdir(work_dir)
rc("open "+ best_pose+".pdb")
rc("select :/isHet " ) 
rc("delete selected")
rc("write #0 ligand_remove.pdb")
rc("close all")
