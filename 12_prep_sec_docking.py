#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
from chimera import *
from chimera import runCommand as rc
from 11_dope_ads_distance import pose
from parameters import *

os.chdir(work_dir)
rc("open "+ pose)
rc("select :/isHet " ) 
rc("delete selected")
rc("write #0 "+pose+"_ligremove.pdb")
rc("close all")
