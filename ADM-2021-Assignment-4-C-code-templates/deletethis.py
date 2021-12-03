import pandas as pd

x = pd.read_csv('l_orderkey-int32.csv', sep='\n')
# x = x.head(5000)
x = x.sample(1001214)
# print(x.shape[0])
x.to_csv('newInput.csv', sep='\n')

'''
Dataset 1

Run1
Branched - 265426689 = 4m25s
Predicated - 473676110 = 7m54s 

Run2
Branched - 257701088 = 4m18s
Predicated - 388022065 = 6m28s

Run3
Branched - 244743491 = 4m5s
Predicated - 399345718 = 6m39s


Shuffled data

Run1
Branched - 594958800 = 9m55s
Predicated - 390853664 = 6m31s

Run2
Branched - 590791286 = 9m51s
Predicated - 390613188 = 6m31s

Run3
Branched - 582031183 = 9m42s
Predicated - 390441136 = 6m31s

'''