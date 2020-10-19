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
""".strip()



rows = [row.strip() for row in data_as_str.split("\n")]

shark_include_rows = [row.split(" ",1)[1] for row in rows if "shark" in row.lower() ]

for film_name in shark_include_rows:
    print(film_name)
