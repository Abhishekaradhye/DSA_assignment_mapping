"""Time to play with Python dictionaries!
You're going to work on a dictionary that
stores cities by country and continent.
One is done for you - the city of Mountain 
View is in the USA, which is in North America.

You need to add the cities listed below by
modifying the structure.
Then, you should print out the values specified
by looking them up in the structure.

Cities to add:
Bangalore (India, Asia)
Atlanta (USA, North America)
Cairo (Egypt, Africa)
Shanghai (China, Asia)"""


"""Print the following (using "print").
1. A list of all cities in the USA in
alphabetic order.
2. All cities in Asia, in alphabetic
order, next to the name of the country.
In your output, label each answer with a number
so it looks like this:
1
American City
American City
2
Asian City - Country
Asian City - Country"""


locations = {'North America': {'USA': ['Mountain View']}}

from collections import OrderedDict


locations = OrderedDict()
locations['North America'] = OrderedDict({'USA': ['Mountain View']})
locations['Asia'] = OrderedDict({'India': ['Bangalore'], 'China': ['Shanghai']})
locations['Africa'] = OrderedDict({'Egypt': ['Cairo']})

locations['North America']['USA'].append('Atlanta')


print("1")

usa_cities = sorted(locations['North America']['USA'])
for city in usa_cities:
    print(city)

print("2")

for country, cities in locations['Asia'].items():
    sorted_cities = sorted(cities)  
    for city in sorted_cities:
        print(city,' - ',country)
