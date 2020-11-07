# -*- coding: utf-8 -*-

from repository import get_matches
from repository import get_count_of_tournaments

matches = get_matches("results.csv")

tournaments = get_count_of_tournaments(matches)

for key, value in tournaments.items():
    print(key, value)