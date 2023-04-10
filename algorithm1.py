var_list = [element.replace("array","")[1:] for element in open("in2a.txt").read().splitlines() if element.startswith("array")]

def tuplesList(lst):
    result = []
    for item in lst:
        name, values = item.split(' = ')
        values = values.strip("[]").split(", ")
        result.append((name, values))
    return result


def pull_lsts(lst):
    lsts = []
    for i in range(1, len(lst), 2):
        lsts.append(lst[i][1])
    return lsts

def pull_strings(lst):
    strings = []
    for i in range(0, len(lst), 2):
        strings.extend(lst[i][1])
    return strings



lists = tuplesList(var_list)
cities_strings = pull_strings(lists)
cities_words = pull_lsts(lists)

def find_cities(array_a, array_b):
    cities = [city for city in array_b if city in array_a]
    output_order = [array_a.find(city) for city in cities]
    sorted_cities = [city for _, city in sorted(zip(output_order, cities))]
    sorted_order = sorted(output_order)
    return sorted_order, sorted_cities

output_order, output_array = find_cities(cities_strings[1],cities_words[1])

array1 = cities_strings[0]
array2 = cities_words[0]

for i in range(0, len(cities_strings)):
    
  output_order, output_array = find_cities(cities_strings[i],cities_words[i])
  print(f"\nOutput Order {i+1}: {output_order} \nOutput Array {i+1}: {output_array}\n")

