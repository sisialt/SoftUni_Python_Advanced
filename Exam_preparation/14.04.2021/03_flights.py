def flights(*args):
    flights_with_passengers = {}

    for i in range(0, len(args), 2):

        if args[i] == "Finish":
            break
        elif args[i] in flights_with_passengers:
            flights_with_passengers[args[i]] += args[i + 1]
        else:
            flights_with_passengers[args[i]] = args[i + 1]

    return flights_with_passengers


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print()

print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print()

print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
print()