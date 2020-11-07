# -*- coding: utf-8 -*-

from repository import get_matches

matches = get_matches("results.csv")

result = sorted(matches, key=lambda match: abs(match.home_ft - match.away_ft), reverse=True)

result_top_10 = result[:10]

for item in result_top_10:
    print(f"{item.home_team} {item.home_ft} : {item.away_ft} {item.away_team}")