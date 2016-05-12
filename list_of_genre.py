genre_df=movies_meta_df[["title","genre"]]
genre_list=list(genre_df[["genre"]].values.flatten())
unique_genre_list=list(set([item for sublist in genre_list for item in sublist]))
