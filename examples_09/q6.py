# -*- coding: utf-8 -*-

from repository import get_matches
from repository import get_count_of_countries

matches = get_matches("results.csv")

country_count = get_count_of_countries(matches)

sorted_country_count = sorted(country_count.items(), key=lambda x: x[1], reverse=True)

highest_count_country, count = sorted_country_count[0]

print(highest_count_country, count)