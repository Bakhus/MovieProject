genre_df['genre_len'] = genre_df.apply(lambda x: len(x['genre']), axis=1)
