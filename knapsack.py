import time
import argparse
import sys

def main():

    start = time.process_time()

    parser = argparse.ArgumentParser(description="Solves the 0/1 knapsack problem for a given set of items.")
    parser.add_argument("-i", help="items to take", action="store_true")
    parser.add_argument("-v", help="total value of the items taken", action="store_true")
    parser.add_argument("-w", help="total weight of the items taken", action="store_true")
    parser.add_argument("-t", help="execution time", action="store_true")
    parser.add_argument("filename", help=".txt file to parse")
    args = parser.parse_args()

    try:
        with open(args.filename, 'r') as file:
            raw = [ list(map(int, i.split())) for i in file.readlines() ]
    except IOError:
        print("No such file.")
        sys.exit()
    
    capacity = raw[0][0]
    numOfItems = raw[0][1]

    keep = []
    for i in range(numOfItems):
        keep.append( [ 0 for j in range(0, capacity) ] )

    values = [ i[0] for i in raw[1:] ]
    weights = [ i[1] for i in raw[1:] ]

    current = [ 0 for j in range(0, capacity + 1)]

    for i in range (1, numOfItems  + 1):
        previous = current[:]
        for j in range(1, capacity + 1):
            if weights[i - 1] <= j:
                if current[j] <= previous[j - weights[i - 1]] + values[i - 1]:
                    current[j] = previous[j - weights[i - 1]] + values[i - 1]
                    keep[i-1][j-1] = 1

    totalValue = current[capacity]
    
    itemsToTake = set()
    while numOfItems >= 0:
        if keep[numOfItems - 1][capacity - 1] == 1:
            itemsToTake.add( ( values[numOfItems - 1],  weights[numOfItems - 1] ))
            capacity -= weights[numOfItems - 1]
            numOfItems -= 1
        else:
            numOfItems -= 1

    totalWeight = 0
    for item in itemsToTake:
        totalWeight += item[1]

    if args.v:
        print("Total value of the items taken: {}".format(totalValue))

    if args.w:
        print("Total weight of the items taken: {}".format(totalWeight))

    if args.i:
        print("The items we should take (value, weight): {}".format(itemsToTake))
        
    if args.t:
        print("--- {} seconds ---".format(time.process_time() - start))

if __name__ == "__main__":
    main()   
