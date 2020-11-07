# -*- coding: utf-8 -*-

from repository import get_matches
from repository import get_count_of_cities


matches = get_matches("results.csv")

city_count = get_count_of_cities(matches)

sorted_city_count = sorted(city_count.items(), key=lambda x: x[1], reverse=True)

highest_count_city, count = sorted_city_count[0]

print(highest_count_city, count)
