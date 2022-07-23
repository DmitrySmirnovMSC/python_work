# cities = ["barcelona", "moscow", "madrid", "rome", "buenos aires", "valencia", "saint petersburg", "berlin", "krasnodar", "sochi", "milan", "paris", "new york", "toronto", "granada"]

# for city in cities[-3:]:
#   print(city.title())

cities_one = ["barcelona", "moscow", "madrid", "rome"]
print(cities_one)
cities_two = cities_one[:]
print(cities_two)

cities_one.append("krasnodar")
print(cities_one)
cities_two.append("berlin")
print(cities_two)