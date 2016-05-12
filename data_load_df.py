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

wanted_keys = ['user_score',
 'rating',
 'complete',
 'runtime_minutes',
 'release_date',
 'director',
 'metascore',
 'num_user_ratings',
 'metacritic_page',
 'studio',
 'year',
 'title'] # The keys you want

movie_list=[]
for names in movie_files:
    target_file_path = os.path.join(DATA_DIR, names)
    with open(target_file_path, 'r') as names:
         movie = json.load(names)
         movie1 = dict((k, movie[k]) for k in wanted_keys if k in movie)
    movie_list.append(movie1)

len(movie_list)

movies_meta_df = pd.DataFrame(movie_list)
