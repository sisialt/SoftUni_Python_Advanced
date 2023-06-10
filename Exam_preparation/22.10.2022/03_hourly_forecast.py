def forecast(*args):
    locations = {}
    locations_sorted_weather = {"Sunny": [], "Cloudy": [], "Rainy": []}
    result = ""

    for arg in args:
        locations[arg[0]] = arg[1]

        locations_sorted_weather[arg[1]].append(arg[0])

    for city in sorted(locations_sorted_weather["Sunny"]):
        result += f"{city} - Sunny\n"
    for city in sorted(locations_sorted_weather["Cloudy"]):
        result += f"{city} - Cloudy\n"
    for city in sorted(locations_sorted_weather["Rainy"]):
        result += f"{city} - Rainy\n"

    return result

# def forecast(*args): # pochti minava!
#     locations = {}
#
#     result = []
#
#     for arg in args:
#         if arg[1] not in locations:
#             locations[arg[1]] = []
#         locations[arg[1]].append(arg[0])

#     if "Sunny" in locations:
#         result.append([f"{loc} - Sunny" for loc in sorted(locations["Sunny"])])
#     if "Cloudy" in locations:
#         result.append([f"{loc} - Cloudy" for loc in sorted(locations["Cloudy"])])
#     if "Rainy" in locations:
#         result.append([f"{loc} - Rainy" for loc in sorted(locations["Rainy"])])
#
#     return [print(*inner_list, sep="\n") for inner_list in result if inner_list]

# def forecast(*args):
#     locations = {}
#     for el in args:
#         if el[0] not in locations:
#             locations[el[0]] = el[1]
#     sorted_result = {k: v for k,v in sorted(locations.items(), key=lambda x: (x[1], x[0]))}
#     sunny = ''
#     cloudy = ''
#     rainy = ''
#     for key, value in sorted_result.items():
#         if value == 'Sunny':
#             sunny += f'{key} - {value}\n'
#         elif value == 'Cloudy':
#             cloudy += f'{key} - {value}\n'
#         elif value == 'Rainy':
#             rainy += f'{key} - {value}\n'
#
#     return sunny + cloudy + rainy




print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))
print()
print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))
print()
print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))
