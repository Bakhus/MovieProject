# -*- coding: utf-8 -*-
"""
Created on Fri May 13 10:06:52 2016

@author: djl358
"""

# imports
import os
import json
import pprint
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm

def change_to_list_df(input_df):
    '''
    because when we load the data from csv, the genre column is string instead of list
    we need to change its type to list
    '''
    def change_to_list(x):
        if type(x) == str:
            return x[1:-1].split(', ')
        else:
            print x

    input_df['genre'] = input_df.apply(lambda x: change_to_list(x['genre']), axis=1)
    return input_df
    
def add_genre(input_df):
    #input_df = combined_df.copy()
    input_df = change_to_list_df(input_df)
    try:
        master_list = []
        for item_list in input_df["genre"]:
            if not item_list is None:
                for item in item_list:
                    master_list.append(item)
    except:
        print 'exception',item_list, item, type(item)
    
    unique_genre_list = list(set(master_list))

    for g in unique_genre_list:
        input_df[g]=0
    try:
        for i in input_df.index:
            if isinstance(input_df.ix[i,'genre'], list):
                for item in input_df.ix[i,'genre']:
                    input_df.ix[i, item]=1
    except:
        print 'd', i, item
    return input_df, unique_genre_list
    
def plot_genre_gross(input_df, unique_genre_list):
    '''
    This function plots the mean domestic gross by different genre
    '''
    dome_gross_genre = dict()
    dome_gross_genre_df = pd.DataFrame(columns=unique_genre_list)
    for item in unique_genre_list:
        dome_gross_genre[item] = input_df.loc[input_df[item]==1]['domestic_gross'].count()
        dome_gross_genre_df[item] = input_df['domestic_gross']*input_df[item]
    #dome_gross_genre = pd.DataFrame(dome_gross_genre, index=[0])
    dome_gross_genre_df=dome_gross_genre_df.replace(0, np.nan)

    # plot boxplot    
    dome_gross_genre_df.boxplot()
    plt.xticks(rotation='vertical')
    plt.ylim([0, 3*10**8])
    plt.show()
    
    # plot count
    plt.bar(range(len(dome_gross_genre)), dome_gross_genre.values())
    plt.xticks(range(len(dome_gross_genre)), dome_gross_genre.keys(), rotation='vertical')
    plt.show()
    return
    
def add_studios(me_df):
    '''Creates column per each studio if studio is in top 10. The top ten are hard coded.'''

    #List of top ten studios
    top_10_studios = ['Warner Bros. Pictures'
    ,'Universal Pictures'
    ,'Columbia Pictures'
    ,'Paramount Pictures'
    ,'Twentieth Century Fox Film Corporation'
    ,'Sony Pictures Classics'
    ,'Buena Vista Pictures'
    ,'IFC Films'
    ,'Miramax Films'
    ,'Fox Searchlight Pictures']

    def in_top_10(row):
        if row['studio'] in top_10_studios:
            return 1
        else:
            return 0

    for studio in top_10_studios:
        try: 
            me_df[studio] = me_df.apply(in_top_10, axis=1)
        except: 
            print me_df['studio']

    me_df.rename(columns={'Warner Bros. Pictures'                  : 'WarnerBrosPictures'
    ,'Universal Pictures'                     : 'UniversalPictures'
    ,'Columbia Pictures'                      : 'ColumbiaPictures'
    ,'Paramount Pictures'                     : 'ParamountPictures'
    ,'Twentieth Century Fox Film Corporation' : 'TwentiethCenturyFoxFilmCorporation'
    ,'Sony Pictures Classics'                 : 'SonyPicturesClassics'
    ,'Buena Vista Pictures'                   : 'BuenaVistaPictures'
    ,'IFC Films'                              : 'IFCFilms'
    ,'Miramax Films'                          : 'MiramaxFilms'
    ,'Fox Searchlight Pictures'               : 'FoxSearchlightPictures' }, inplace=True)

    return me_df

def create_season(combined_df):
    '''
    This function change release_date to date and create season variables based on released date.
    '''
    combined_df['release_date']=pd.to_datetime(combined_df['release_date'])
    def month_to_season(x):
        if x.month <=4:
            return 'spring'
        elif x.month <=7:
            return 'summer'
        elif x.month <=10:
            return 'fall'
        else: 
            return 'christmas'
    combined_df['release_season'] = combined_df.apply(lambda x: month_to_season(x['release_date']), axis=1)
    
    combined_df.groupby('release_season')['domestic_gross'].mean().plot()
    plt.title('Average domestic gross take')
    plt.show()
    return combined_df

#####
df_csv = pd.read_csv('C:/Users/djl358/bdatabootcamp_proj1/MovieProject/Movie_Analysis.csv')
df_csv = create_season(df_csv)
df_csv = add_studios(df_csv)
df_csv, genre_list = add_genre(df_csv)

df_csv_fnl = pd.read_csv('C:/Users/djl358/bdatabootcamp_proj1/MovieProject/Movie_Analysis_fnl.csv')
df_csv_fnl = change_to_list_df(df_csv_fnl)

def genre_len_fun(x):
    if type(x)==list:
        return len(x)
df_csv_fnl['genre_len'] = df_csv_fnl.apply(lambda x: genre_len_fun(x['genre']), axis=1)
df_csv_fnl['genre_len'].fillna(0, inplace=True)
df_csv_fnl.loc[:,['genre_len', 'domestic_gross']].boxplot(by=['genre_len'])
plt.ylim([0, 3*10**8])
plt.show()
df_csv_fnl.groupby(['genre_len'])['domestic_gross'].count().plot(kind='bar')

def genre_len_type_fun(x):
    if (x >= 3.0) and (x <= 6.0):
        return 1
    else: 
        return 0
df_csv_fnl['genre_num_3_6_ind'] = df_csv_fnl.apply(lambda x: genre_len_type_fun(x['genre_len']), axis = 1)
df_csv_fnl.loc[:,['genre_num_3_6_ind', 'domestic_gross']].boxplot(by=['genre_num_3_6_ind'])
plt.ylim([0, 2*10**8])
plt.show()

df_csv_fnl.loc[:,['director_experience', 'domestic_gross']].boxplot(by=['director_experience'])
plt.ylim([0, 3*10**8])
plt.show()
df_csv_fnl.groupby(['director_experience'])['domestic_gross'].count().plot(kind='bar')

df_csv_fnl['director_experience'] = df_csv_fnl.apply(lambda x: min(x['director_experience'], 9), axis = 1)


df_csv_fnl.loc[:,['rating', 'domestic_gross']].boxplot(by=['rating'])
plt.ylim([0, 3*10**8])
plt.xticks(rotation='vertical')
plt.show()
df_csv_fnl.groupby(['rating'])['domestic_gross'].count().plot(kind='bar')

grouped_pg_rtng = [
'PG-13',
'PG',
'G',
'TV-14',         
'TV-PG',
'PG--13',
'GP',
'TV-G'
]


def rating_new_fun(x):
    if x in grouped_pg_rtng:
        return 1
    else:
        return 0
df_csv_fnl['rtng_PG_ind']=df_csv_fnl.apply(lambda x: rating_new_fun(x['rating']),axis=1)

df_csv_fnl.loc[:,['rtng_PG_ind', 'domestic_gross']].boxplot(by=['rtng_PG_ind'])
plt.ylim([0, 3*10**8])
plt.show()
df_csv_fnl.groupby(['rtng_PG_ind'])['domestic_gross'].count().plot(kind='bar')

def plot_hist_boxplot(var_name, by_var_name, df):
    df.loc[:,[var_name, by_var_name]].boxplot(by=[by_var_name])
    plt.ylim([0, 3*10**8])
    plt.show()
    df_csv_fnl.groupby([by_var_name])[var_name].count().plot(kind='bar')
    

def season_ind_fun(x):
    if x in ['summer', 'christmas']:
        return 1
    else:
        return 0
df_csv_fnl['season_ind']=df_csv_fnl.apply(lambda x: season_ind_fun(x['release_season']),axis=1)

plot_hist_boxplot('domestic_gross', 'season_ind', df_csv_fnl)

df_csv_fnl['release_ind'] = df_csv_fnl.apply(lambda x: 1 if np.isnan(x['widest_release']) else 0, axis=1)
df_csv_fnl['wide_release_log'] = np.log(df_csv_fnl['widest_release']+1)


num_predictor = [
'wide_release_log',
'release_ind',
'season_ind',
'director_experience',
'rtng_PG_ind'
]
df_for_reg = df_csv_fnl[num_predictor+['l_title', 'domestic_gross']]
# correlation matrix plot
plt.matshow(df_for_reg.corr())
plot_corr(df_for_reg)
    
# theater_miss_ind
#'nb_theaters',
#'title length',
#'genre_num_3_6_ind',


df_for_reg.fillna(0, inplace=True)
X = df_for_reg[num_predictor] 
y = df_for_reg['domestic_gross']
    
X_mat = sm.add_constant(X)
linmodel = sm.OLS(y, X_mat).fit()
print linmodel.summary()
plt.scatter(y, linmodel.resid)
plt.scatter(y, linmodel.fittedvalues)



for item in num_predictor:
    print item
    plt.scatter(df_for_reg[item] , df_for_reg['domestic_gross'])
    plt.show()


def plot_corr(df,size=10):
    '''Function plots a graphical correlation matrix for each pair of columns in the dataframe.

    Input:
        df: pandas DataFrame
        size: vertical and horizontal size of the plot'''

    corr = df.corr()
    fig, ax = plt.subplots(figsize=(size, size))
    ax.matshow(corr)
    plt.xticks(range(len(corr.columns)), corr.columns);
    plt.yticks(range(len(corr.columns)), corr.columns);




