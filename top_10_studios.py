#Create column per each studio if studio is in top 10
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
    
def in_top_10(row):
    if row['studio'] in top_10_studios:
        return 1
    else:
        return 0
    
for studio in top_10_studios:
    Combined_df[studio] = Combined_df.apply(in_top_10, axis=1)
