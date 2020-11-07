# -*- coding: utf-8 -*-

from repository import get_teams

teams = get_teams("results.csv")

sorted_teams_by_max_invincibility = sorted(teams.items(), key=lambda x: x[1].max_invincibility_series, reverse=True)

team_name, team = sorted_teams_by_max_invincibility[0]

print(team_name)
print(team.max_invincibility_series)
