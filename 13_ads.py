#AUTODOCKSCORE
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

from collections import OrderedDict
from operator import itemgetter
import pandas as pd
from plotnine import *
import matplotlib as mpl
mpl.rcParams['patch.force_edgecolor'] = True

receptor="1rthA"
path='C:/Users/pukma/Desktop/IFD'

dockingLog = open(path+'/'+receptor+".dlg", "r")
logLines = dockingLog.readlines()
energyValue=[]
num=0
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
    with open(path+'/'+ dockingLog+ ".txt", 'w') as f:
        for value in d.items():
            f.write('%s %s\n' % value)

SaveDict(dockingScore, "ASD_SCORE")


file=np.loadtxt('ASD_SCORE.txt')
ADS=file[:,1]

data=pd.DataFrame(
    {
    "POSES" : ['pose0','pose1','pose2','pose3','pose4','pose5','pose6','pose7','pose8','pose9'],   
    "col1" : [0,1,2,3,4,5,6,7,8,9],
    "col2" : ADS
    })

gg=ggplot(data , aes(x = 'POSES', y = 'ADS',size='2',color='POSES')) +\
    geom_point() +\
    ggtitle('AutoDockScore')
    
        
ggsave(plot = gg, filename ='ADScore')

#choose the best pose:

value=np.argmin(ADS)
pose=("pose"+str(value))






















