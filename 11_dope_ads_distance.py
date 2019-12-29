import os, shutil 
import numpy as np
from collections import OrderedDict
import pandas as pd
from plotnine import *

from parameters import *

os.chdir(work_dir)

#DOPE

log = open(work_dir+'/'+"dope.log", "r")

logLines = log.readlines()
DOPEvalue = []
for i,line in enumerate(logLines):
    if line.startswith("DOPE score               :"):
        value = line.split(":")[1]
        DOPEvalue.append(value)

def tuplizeDopes(vec):
    a=len(vec)
    model1 = list(o.strip() for ix, o in enumerate(vec) if ix % 2 == 0) # DOPE for whole model
    model2 = list(o.strip() for ix, o in enumerate(vec) if ix % 2 == 1) # Dope for selected Residues

    return zip(model1, model2)

Dope_value = tuplizeDopes(DOPEvalue)

with open(work_dir+'/'+"DOPE.txt", 'w') as f:
    f.writelines(list(('%d %s %s\n' % (it, v[0], v[1])) for it, v in enumerate(Dope_value)))

#AUTODOCKSCORE


dockingLog = open(work_dir+'/'+receptor+".dlg", "r")
logLines = dockingLog.readlines()
energyValue=[]
num=1
dockingScore={}
for i, line in enumerate(logLines):
    if line.startswith("Final-Value:"):
        name = str(num)
        energyValue= line.split(":")[1]
        dockingScore[name] = energyValue
        num += 1


def SaveDict(dict, dockingLog):
    lists = dict.items() 
    x, y = zip(*lists)
    SortedValues = dict.values()
    d = OrderedDict(dict.items())
    with open(work_dir+'/'+ dockingLog+ ".txt", 'w') as f:
        for value in d.items():
            f.write('%s %s\n' % value)


SaveDict(dockingScore, "ADS_SCORE")

#DISTANCE

DOPE=open(work_dir+'/'+'DOPE.txt', 'r')
ADS=open(work_dir+'/'+'ADS_SCORE.txt', 'r')


dope=np.loadtxt(DOPE)
dope=dope[:,2]

ads=np.loadtxt(ADS)
ads=ads[:,1]


dope_norm=abs(dope)/max(abs(dope))
ads_norm=abs(ads)/max(abs(ads))


DISTANCE=np.sqrt((pow(ads_norm,2)+pow(dope_norm,2)))
    
## Wykres

data=pd.DataFrame(
    {
    "POSES" : ['pose0','pose1','pose2','pose3','pose4','pose5','pose6','pose7','pose8','pose9'],   
    "col1" : [0,1,2,3,4,5,6,7,8,9],
    "col2" : DISTANCE
    }
    )

gg=ggplot(data , aes(x = 'POSES', y = 'DISTANCE',size='2',color='POSES')) +\
    geom_point() +\
    ggtitle('Optimized distance: '+receptor)

ggsave(plot = gg, filename ='DISTANCE')

#choose max value:

pose_num=data["col2"].idxmax()

pose=("pose"+str(pose_num))


with open("temp.py","a") as p:
    name="best_pose='"
    p.write(name+pose+"'\n")


shutil.copy(work_dir+"/temp.py",work_dir+"/IFD") 
shutil.copy(work_dir+"/"+pose+".pdb",work_dir+"/IFD")
shutil.copy(work_dir+"/"+ligand+".pdb",work_dir+"/IFD")  

