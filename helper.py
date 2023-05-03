import pandas as pd
import numpy as np
def getcoords(filename):    
    df = pd.read_csv(filename,index_col=False)

    tf = df[["Longitude", "Latitude"]]
    tf.loc[(df!=0).any(axis=1)]

    return tf
def getcounts(filename):
    df = pd.read_csv(filename,index_col=False)
    tf = df["Radiation(cps)"]
    tf = np.array(tf)
    tf = np.around(tf)
    tf = tf.astype(int)
    tf = tf.tolist()
    return tf
def dot(locs, counts):
    mapper = []
    for i in range(len(locs)):
        temp = [locs[i]] * counts[i]
        mapper.extend(temp) 
    return mapper
    
locs = [1,2,3,4,5]
counts = [1,2,3,4,5]

print(dot(locs,counts))

     