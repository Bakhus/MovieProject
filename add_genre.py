'''
This function takes movies data frame and adds columns for each genre.
The data frame must have column called genre
'''

def add_genre(input_df):
    str_genre=[]
    for g in input_df.genre:
        for i in range(len(g)):
            str_genre.append(g[i])

    str_genre=list(set(str_genre))

    for g in str_genre:
        input_df[g]=0

    for i in input_df.index:
        for item in test.ix[i,'genre']:
            input_df.ix[i, item]=1

    return input_df
