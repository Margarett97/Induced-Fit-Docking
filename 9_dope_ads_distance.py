import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

from collections import OrderedDict
from operator import itemgetter
import pandas as pd
from plotnine import *
import matplotlib as mpl
mpl.rcParams['patch.force_edgecolor'] = True

from names import path, log_file, receptor

#DOPE

log = open(path+'/'+log_file+".log", "r")

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

with open(path+'/'+"DOPE.txt", 'w') as f:
    f.writelines(list(('%d %s %s\n' % (it, v[0], v[1])) for it, v in enumerate(Dope_value)))

#AUTODOCKSCORE


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

#DISTANCE

DOPE=open(path+'/'+'DOPE.txt', 'r')
ADS=open(path+'/'+'ASD_SCORE.txt', 'r')


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
    ggtitle('Zoptymalizowana odległość')

print(gg)

