import  glob
import pickle
import  matplotlib

import  numpy               as  np
import  matplotlib.pyplot   as  plt

savedSessionsPaths = glob.glob('./savedSessions/*.p')

for sessionPath in savedSessionsPaths:
    f = open(sessionPath, 'rb')
    obj = pickle.load(f)  
    for win in obj:
        print(win)