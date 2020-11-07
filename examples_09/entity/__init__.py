# -*- coding: utf-8 -*-

class Team:
    def __init__(self, name):
        self.__name = name
        self.__goals_for = 0
        self.__goals_against = 0
        self.__current_invincibility_series = 0
        self.__max_invincibility_series = 0

    @property
    def current_invincibility_series(self):
        return self.__current_invincibility_series

    @property
    def max_invincibility_series(self):
        return self.__max_invincibility_series

    @current_invincibility_series.setter
    def current_invincibility_series(self, current_invincibility_series):
        self.__current_invincibility_series = current_invincibility_series

        if self.__current_invincibility_series > self.__max_invincibility_series:
            self.__max_invincibility_series = self.__current_invincibility_series

    @property
    def goals_for(self):
        return self.__goals_for

    @goals_for.setter
    def goals_for(self, goals_for):
        self.__goals_for = goals_for

    @property
    def goals_against(self):
        return self.__goals_against

    @goals_against.setter
    def goals_against(self, goals_against):
        self.__goals_against = goals_against




class Match:
    def __init__(self, date, city, country, home_team, away_team, home_ft, away_ft ,tournament):
        self.date = date
        self.home_team = home_team
        self.away_team = away_team
        self.home_ft = home_ft
        self.away_ft = away_ft
        self.city = city
        self.tournament = tournament
        self.country = country
