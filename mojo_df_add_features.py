def add_feature(movies_df):
    '''
    This function adds neccesary features from transformation of other variables
    Argument:
    movies_df:  dataframe of movies info
    Return:
    movies_df:  dataframe of movies info with more features
    '''
    movies_df['title length'] = movies_df.apply(lambda x: len(x['title']), axis=1)
    movies_df['nb_theaters'] = movies_df['opening_weekend_take'] / movies_df['opening_per_theater']
    movies_df['ind_2000'] = movies_df.apply(lambda x: 1 if x['year']>2000 else 0, axis=1)
    # get missing indicator    
    movies_df['budget_miss_ind'] = movies_df['production_budget'].apply(lambda x: 1 if np.isnan(x) else 0)
    movies_df['theater_miss_ind'] = movies_df['opening_per_theater'].apply(lambda x: 1 if np.isnan(x) else 0)
    # fillna with 0 
    movies_df['production_budget'].fillna(0)
    movies_df['opening_per_theater'].fillna(0)
    movies_df['opening_weekend_take'].fillna(0)
    movies_df['nb_theaters'].fillna(0)
    return movies_df
