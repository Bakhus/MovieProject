import os
import json
DATA_DIR = os.path.join('C:\\Users\\EVW207\\Desktop\\bootcamp_git\\ct16_cap1_ds5\\project_1\\data', 'boxofficemojo')

movie_files=os.listdir(DATA_DIR)

movie_list=[]
for names in movie_files:
    target_file_path = os.path.join(DATA_DIR, names)
    with open(target_file_path, 'r') as names:
         movie = json.load(names)
    movie_list.append(movie)

len(movie_list)

import pandas as pd
movies_mojo_df = pd.DataFrame(movie_list)

DATA_DIR = os.path.join('C:\\Users\\EVW207\\Desktop\\bootcamp_git\\ct16_cap1_ds5\\project_1\\data', 'metacritic')

movie_files=os.listdir(DATA_DIR)

movie_list=[]
for names in movie_files:
    target_file_path = os.path.join(DATA_DIR, names)
    with open(target_file_path, 'r') as names:
         movie = json.load(names)
         movie_list.append(movie)

len(movie_list)

list_types = []
for i in movie_list:
    if type(i) == dict:
        list_types.append(i)
        
movies_meta_df = pd.DataFrame(list_types)
