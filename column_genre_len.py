genre_df=movies_meta_df[["title","genre"]]
genre_list=list(genre_df[["genre"]].values.flatten())
unique_genre_list=list(set([item for sublist in genre_list for item in sublist]))


genre_df['genre_len'] = genre_df.apply(lambda x: len(x['genre']), axis=1)


[u'Sci-Fi',
 u'Crime',
 u'Romance',
 u'Animation',
 u'Music',
 u'Adult',
 u'Comedy',
 u'War',
 u'Horror',
 u'Film-Noir',
 u'Western',
 u'News',
 u'Thriller',
 u'Adventure',
 u'Mystery',
 u'Short',
 u'Drama',
 u'Action',
 u'Documentary',
 u'Musical',
 u'History',
 u'Family',
 u'Fantasy',
 u'Sport',
 u'Biography']
