# -*- coding: utf-8 -*-

from repository import get_teams

teams = get_teams("results.csv")
goals_for_sorted_teams = sorted(teams.items(), key=lambda item: item[1].goals_for, reverse=True)
team_name, team = goals_for_sorted_teams[0]

print(team_name)
print(team.goals_for)