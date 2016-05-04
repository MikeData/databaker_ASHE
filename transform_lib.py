 # -*- coding: utf-8 -*-
"""
Spyder Editor

Basic reusable functions to help post-process data with Pandas.

Author: Mike
"""

import pandas as pd


# Dismiss command for unwanted items. Will remove all 8 relevant columns.
def dismiss(myframe, headers):
    
    for each in headers:
        Column1 = myframe.columns.get_loc(each)
        for x in range(1, 9):
            myframe = myframe.drop(myframe.columns[Column1], axis=1)
    return myframe
    
 
Converts everything to string and joins around a single space
# def strip_and_join(obs_file, dimlist):
    for x in dimlist:
        obs_file[x] = obs_file[x].astype(str)
        obs_file[x] = obs_file[x].map(lambda x: x.strip())
        obs_file[x] = obs_file[x].map(lambda x: ' '.join(x.split()))        
    obs_file[dimlist[0]] = obs_file[dimlist[0]] + ' ' + obs_file[dimlist[1]] + ' ' + obs_file[dimlist[2]]
    obs_file[dimlist[0]] = obs_file[dimlist[0]].map(lambda x: x.strip())
    return obs_file[dimlist[0]]
    
