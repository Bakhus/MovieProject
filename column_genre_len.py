genre_df=movies_meta_df[["title","genre"]]
genre_list=list(genre_df[["genre"]].values.flatten())
unique_genre_list=list(set([item for sublist in genre_list for item in sublist]))


genre_df['genre_len'] = genre_df.apply(lambda x: len(x['genre']), axis=1)
