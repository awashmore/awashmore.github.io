import nfl_data_py as nfl
import matplotlib.pyplot as plt
import pandas as pd

#gather the fantasy data
weekly_data = nfl.import_weekly_data([2022], ['player_name', 'position', 'week', 'fantasy_points_ppr'])
weekly_data.sort_values(by=['fantasy_points_ppr'], ascending=False, inplace=True)
weekly_data.sort_values(by=['week', 'position'], ascending=True, inplace=True)
weekly_data = weekly_data.reset_index()
weekly_data = weekly_data[(weekly_data.position == 'QB') | (weekly_data.position == 'RB') | (weekly_data.position == 'WR') | (weekly_data.position == 'TE')]
weekly_data = weekly_data.reset_index()
weekly_data.to_excel('weekly_fantasy_data.xlsx', engine='xlsxwriter')

mahomes_data = weekly_data[(weekly_data.player_name == 'P.Mahomes')]
# mahomes_data = mahomes_data.reset_index()
mahomes_data_new = pd.DataFrame(mahomes_data, columns=['position', 'week', 'fantasy_points_ppr'])
# mahomes_data.loc[:, 'player_name':'fantasy_points_ppr']
mahomes_data_new.to_excel('mahomes_fantasy_data.xlsx', engine='xlsxwriter')

player_data = nfl.import_ids()
player_data = player_data.reset_index()
player_data = player_data[(player_data.position == 'QB') | (player_data.position == 'RB') | (player_data.position == 'WR') | (player_data.position == 'TE')]
player_data.to_excel('player_data.xlsx', engine='xlsxwriter')
# player_names = player_data['name'].to_list()

# mahomes_data_new.plot(x='week', y='fantasy_points_ppr')
plt.scatter(mahomes_data_new['week'], mahomes_data_new['fantasy_points_ppr'])
plt.xticks(range(1, 23))
plt.show()

# for player in player_names:
#     print(player)