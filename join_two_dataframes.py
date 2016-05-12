'''
This python script joins two pandas data frames named:
movies_mojo_df and movies_meta_df
'''

# Drop rows with no Titles
movies_meta_df.dropna(inplace=True,subset=['title'])
movies_mojo_df.dropna(inplace=True,subset=['title'])

#Create new columns with titles in lower case and stripped leading and trailing white spaces
movies_meta_df['l_title']=[x.lower().strip() for x in movies_meta_df.title]
movies_mojo_df['l_title']=[x.lower().strip() for x in movies_mojo_df.title]

# Create combined data frame joined on new column, l_title
Combined_df=pd.merge(movies_mojo_df, movies_meta_df, on='l_title')
