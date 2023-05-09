import nfl_data_py as nfl

years = list(range(1999,2023))
weekly_data = nfl.import_weekly_data(years, ['player_display_name',
                                             'position', 
                                              'season', 
                                              'week',
                                              'receptions',
                                              'targets',
                                              'receiving_tds', 
                                              'receiving_yards',
                                              'receiving_air_yards', 
                                              'receiving_yards_after_catch', 
                                              'receiving_first_downs', 
                                              'receiving_epa',
                                              'racr',
                                              'target_share',
                                              'air_yards_share',
                                              'wopr',
                                              'fantasy_points_ppr'])
weekly_data.sort_values(by=['season', 'week'], ascending=True, inplace=True)
weekly_data = weekly_data.reset_index()
wr_stats = weekly_data[(weekly_data.position == 'WR')]
wr_stats = wr_stats[wr_stats['player_display_name'].notnull()]

# group the data by player and season, and calculate the sum of weekly stats
season_totals = wr_stats.groupby(['player_display_name', 'season']).agg({
    'receiving_yards': 'sum',
    'receiving_tds': 'sum',
    'receptions': 'sum',
    'targets': 'sum',
    'receiving_air_yards': 'sum',
    'receiving_yards_after_catch': 'sum',
    'receiving_first_downs': 'sum',
    'receiving_epa': 'mean',
    'racr': 'mean',
    'target_share': 'mean',
    'air_yards_share': 'mean',
    'wopr': 'mean',
    'fantasy_points_ppr': 'mean'
}).reset_index()

wr_with_10_tds = season_totals[season_totals['receiving_tds'] >= 10]
wr_names = wr_with_10_tds['player_display_name'].to_list()

season_totals = season_totals[season_totals['player_display_name'].isin(wr_names)].reset_index()
season_totals.sort_values(by=['player_display_name', 'season'], ascending=True, inplace=True)
season_totals.to_excel('wr_statistics.xlsx', engine='xlsxwriter')
