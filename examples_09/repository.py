# -*- coding: utf-8 -*-


from datetime import datetime

import pandas as pd

from entity import Team, Match


def get_matches(file_name) -> []:
    data = pd.read_csv(file_name)

    data_val = data.values

    matches = []
    for row in data_val:
        date = row[0]

        if str(date) != "nan":
            date = datetime.strptime(date, "%Y-%m-%d")
        else:
            date = None

        if str(row[1]) != "nan":
            city_country = row[1].split(",")
        else:
            city_country = None

        if city_country != None:
            if len(city_country) > 1:
                city = city_country[0]
                country = city_country[1]
            else:
                city = city_country[0]
                country = city_country[0]

        home_team = row[2]
        away_team = row[3]
        home_ft = row[4]
        away_ft = row[5]
        tournament = row[6]

        matches.append(Match(date, city, country, home_team, away_team, home_ft, away_ft, tournament))

    return matches


def get_teams(file_name) -> {}:
    matches = get_matches(file_name)

    teams = {}
    for match in matches:

        # if str(row[0]) != "nan":
        #     date = datetime.strptime(row[0], "%Y-%m-%d")
        #
        # if str(row[1]) != "nan":
        #     d = row[1].split(",")

        home_team = match.home_team
        away_team = match.away_team
        home_ft = match.home_ft
        away_ft = match.away_ft

        teams[home_team] = teams.get(home_team, Team(home_team))
        teams[home_team].goals_for += home_ft
        teams[home_team].goals_against += away_ft

        teams[away_team] = teams.get(away_team, Team(away_team))
        teams[away_team].goals_for += away_ft
        teams[away_team].goals_against += home_ft

        if home_ft > away_ft:
            teams[away_team].current_invincibility_series = 0
            teams[home_team].current_invincibility_series += 1
        elif home_ft < away_ft:
            teams[home_team].current_invincibility_series = 0
            teams[away_team].current_invincibility_series += 1
        else:
            teams[away_team].current_invincibility_series += 1
            teams[home_team].current_invincibility_series += 1

    return teams


def get_count_of_tournaments(matches: []):
    tournaments = {}

    for match in matches:
        tournaments[match.tournament] = tournaments.get(match.tournament, 0) + 1

    return tournaments


def get_count_of_countries(matches: []):
    result = {}

    for match in matches:
        result[match.country] = result.get(match.country, 0) + 1

    return result


def get_count_of_cities(matches: []):
    result = {}

    for match in matches:
        result[match.city] = result.get(match.city, 0) + 1

    return result
