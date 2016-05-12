def create_season(combined_df):
    '''
    This function change release_date to date and create season variables based on released date.
    '''
    combined_df['release_date']=pd.to_datetime(combined_df['release_date'])
    def month_to_season(x):
        if x.month <=4:
            return 'spring'
        elif x.month <=7:
            return 'summer'
        elif x.month <=10:
            return 'fall'
        else: 
            return 'christmas'
    combined_df['release_season'] = combined_df.apply(lambda x: month_to_season(x['release_date']), axis=1)
    
    combined_df.groupby('release_season')['domestic_gross'].mean().plot()
    plt.title('Average domestic gross take')
    plt.show()
    return combined_df
