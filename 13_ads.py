import os
import numpy as np
from collections import OrderedDict
import pandas as pd
from plotnine import *

from parameters import *

os.chdir(work_dir)


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


file=np.loadtxt('ADS_SCORE.txt')
ADS=file[:,1]

data=pd.DataFrame(
    {
    "POSES" : ['pose1','pose2','pose3','pose4','pose5','pose6','pose7','pose8','pose9','pose10'],   
    "col1" : [1,2,3,4,5,6,7,8,9,10],
    "col2" : ADS
    })

gg=ggplot(data , aes(x = 'POSES', y = 'ADS',size='2',color='POSES')) +\
    geom_point() +\
    ggtitle('AutoDockScore')
    
        
ggsave(plot = gg, filename ='ADScore')

#choose the best pose:

value=np.argmin(ADS)
pose=("pose"+str(value))






















