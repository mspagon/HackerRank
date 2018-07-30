from random import randint
from math import sqrt

def optomizePath(maximumOperatingTravelDistance, forwardShippingRouteList, returnShippingRouteList):
    allRoutesInRange = []

    for forwardRoute in forwardShippingRouteList:
        for returnRoute in returnShippingRouteList:
            routeNumber = (forwardRoute[0], returnRoute[0])
            totalDistance = forwardRoute[1] + returnRoute[1]

            if totalDistance <= maximumOperatingTravelDistance:
                allRoutesInRange.append((routeNumber, totalDistance))

    allRoutesInRange.sort(key=lambda x: x[1], reverse=True)

    bestRouteDistance = allRoutesInRange[0][1]
    for route in allRoutesInRange:
        # continue to print all routes that are equal to the best route distance (ties)
        if route[1] == bestRouteDistance:
            print(route[0])

def main():
    forwardShippingRouteList = []
    returnShippingRouteList = []
    for i in range(randint(1, 30)):
        forwardShippingRouteList.append((i, randint(0, 30) * 1000))

    for i in range(randint(1, 30)):
        returnShippingRouteList.append((i, (randint(0, 30) * 1000)))

    maximumOperatingTravelDistance = 25000

    optomizePath(maximumOperatingTravelDistance, forwardShippingRouteList, returnShippingRouteList)

if __name__ == '__main__':
    main()
