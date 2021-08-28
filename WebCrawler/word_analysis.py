# house list of lists
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

# Build a for loop from scratch

for sublist in house:
    print(str(sublist[0]) + ' is ' + str(sublist[1]) + ' sqm')