'''
This function adds Director experience and Director name columns to the
combined data frame.
Director experience is the number of movies the direcor made
'''

def add_dir_exp(input_df):
    dir_exp= pd.DataFrame(pd.value_counts(input_df.director_y.values))
    dir_exp.reset_index(level=0, inplace=True)
    dir_exp.columns=['director','director_experience']
    df_with_direxp=pd.merge(input_df,dir_exp, left_on='director_y', right_on='director', how='outer')

    print df_with_direxp.shape

    return df_with_direxp
