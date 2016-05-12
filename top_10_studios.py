'''Create column per each studio if studio is in top 10'''
def add_studios(me_df):
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
        me_df[studio] = me_df.apply(in_top_10, axis=1)
    
    me_df.rename(columns={'Warner Bros. Pictures'                  : 'WarnerBrosPictures'                
    ,'Universal Pictures'                     : 'UniversalPictures'                 
    ,'Columbia Pictures'                      : 'ColumbiaPictures'                  
    ,'Paramount Pictures'                     : 'ParamountPictures'                 
    ,'Twentieth Century Fox Film Corporation' : 'TwentiethCenturyFoxFilmCorporation'
    ,'Sony Pictures Classics'                 : 'SonyPicturesClassics'              
    ,'Buena Vista Pictures'                   : 'BuenaVistaPictures'                
    ,'IFC Films'                              : 'IFCFilms'                          
    ,'Miramax Films'                          : 'MiramaxFilms'                      
    ,'Fox Searchlight Pictures'               : 'FoxSearchlightPictures' }, inplace=True)
    
    return me_df
