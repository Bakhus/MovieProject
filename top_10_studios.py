#Create column per each studio if studio is in top 10
studios = Combined_df.studio.value_counts()
print studios

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

for studio in top_10_studios:
    Combined_df[studio] = (Combined_df['studio'] == studio)
