data_as_str = """
1. The Shallows (2016)
  2. Open Water (2004)
3. 47 Meters Down (2017) 
4. Deep Blue Sea(1999) 
    5. The Meg (2018) 
6. The Reef (2010) 
7. Jaws 2 (1978) 
8. Zombie (1979) 
      9. Sharknado (2013) 
10. Tintorera… Tiger Shark (1977)   
11. Jaws: The Revenge (1987) 
     12. Great White (1981) 
13. Example (2018)
""".strip()

rows = [row.strip() for row in data_as_str.split("\n")]

dates = [int(row[-5:-1]) for row in rows]

year_films = {}

for i in range(0, len(dates)):
    if year_films.get(dates[i]) == None:
        year_films[dates[i]] = []
    film_name = rows[i][:-6].strip().split(" ", 1)[1]
    year_films[dates[i]].append(film_name)

max_year = None

for key in year_films:
    if max_year == None:
        max_year = key
    elif max_year < key:
        max_year = key

print(f"{max_year} films:\n")
for film_name in year_films[max_year]:
    print(film_name)

