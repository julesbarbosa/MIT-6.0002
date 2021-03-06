###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    cow_list = {}
    
    with open(filename) as f:
        for line in f:
            key, values = line.split(",")
            cow_list[key] = int(values.strip("\n"))
    return cow_list

    

# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
        """
    cowsCopy = cows.copy()
    sortedCows = sorted(cows.items(), key=lambda x: x[1], reverse=True)
    trips = []
    while sum(cowsCopy.values()) > 0:
        ship = []
        total = 0
        for cow, value in sortedCows:
            if cowsCopy[cow] != 0 and value + total <= limit:
                ship.append(cow)
                total += value
                cowsCopy[cow] = 0
        trips.append(ship)
    return trips   
        
  
        
            
            
            



# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
   
    cows_copy = cows.copy()
    trip = []
    total_trip = len(cows) 
    
    def possible_trip(group):
        total = 0
        for i in group: 
            total += cows_copy[i]
        if total > limit:
            return False
        else:
            return True

    
    for partition in get_partitions(cows_copy):
        count_trips = 0
        if len(partition) <= total_trip:
            for group in partition:
                if possible_trip(group) == False:
                   break 
                else: 
                    count_trips += 1
            if count_trips == len(partition):
                total_trip = len(partition)
                trip = partition
                
    return trip  
            
        
# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    
    text = load_cows("ps1_cow_data.txt")
    start = time.time()
    brute_force_cow_transport(text,limit=10)
    end = time.time() 
    print("Brute Force:", end - start)  
    
    start = time.time()
    greedy_cow_transport(text,limit=10)
    end = time.time() 
    print("Greedy:", end - start)  

    