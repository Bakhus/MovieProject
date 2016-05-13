
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
    input_df = combined_df.copy()
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
