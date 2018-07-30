from random import randint
from math import sqrt


def findNearestSteakhouse(totalSteakhouses, allLocations: list, numSteakhouses):
    locations = []
    for point in allLocations:
        distance = sqrt(point[0] ** 2 + point[1] ** 2)
        locations.append((point, distance))

    locations.sort(key=lambda x: x[1])

    result = []
    for x in range(numSteakhouses):
        result.append(locations[x][0])

    return result


allLocations = []
for _ in range(1000):
    x = randint(-100, 100)
    y = randint(-100, 100)
    allLocations.append([x, y])

print(findNearestSteakhouse(len(allLocations), allLocations, 22))
