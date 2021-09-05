# Problem 7 - bags, bags, bags

with open('input.txt', 'r') as text:
    bags = text.read().split(".\n")

# Part 1


def parentbag(childbag):                # function to find what bags can hold the childbag
    for parent in bags_dict:            # iterate through the different bags
        content = bags_dict[parent]     # what bags can be in parent bag
        if childbag in content:         # if the requested bag can be in parent bag
            parentbag(parent)           # recursion to see what bag can hold the parent bag
            bagset.add(parent)          # add bag to set of bags allowed to (eventually) hold childbag
    return


bags_dict = {}                          # initialize the dict
for bag in bags:                        # populate the dictionary
    bag = bag.replace(" bags", "").replace(" bag", "").replace(".", "")  # Remove text not required
    bag = bag.split(" contain ")        # split each entry into parent and child bag - note the spaces
    bags_dict[bag[0]] = bag[1]          # populate the dict. Key: parent, value: child

bagset = set()
parentbag("shiny gold")
print("Part 1: The amount of different coloured bags that can hold a shiny gold bag: " + str(len(bagset)))


# Part 2


def add_child(parent_bag):
    # Function that will find the amount of individual bags insied a parent bag.
    # The function will go through the children of the parent bag to get their content
    # as well.
    content = bags_dict[parent_bag].split(", ")
    if content[0] == "no other":
        return
    else:
        for child in content:           # iterate through the bags inside the parent bag
            bagname = child[2:]         # Bag name is second char onwards
            number = int(child[0])      # number of bags is the first (0th) char
            if bagname in children_counting:            # TRUE if bag has been counted already
                children_counting[bagname] += number    # increase the amount of that bag
            else:                                       # used if the bag has not been counted already
                children_counting[bagname] = number     # if the bag has not been counted already, add the number of it
            for i in range(number):     # iterate through the amount of bags
                add_child(bagname)      # go through each of the child bags inside the parent bag and get their content
        return


children_counting = {}
add_child("shiny gold")
print("Part 2: Total number of bags: " + str(sum(children_counting.values())))
