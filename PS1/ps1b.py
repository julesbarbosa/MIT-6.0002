###########################
# 6.0002 Problem Set 1b: Space Change
# Name:
# Collaborators:
# Time:
# Author: charz, cdenise

#================================
# Part B: Golden Eggs
#================================

# Problem 1
def dp_make_weight(egg_weights, target_weight, memo = {}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight
    """
        ## ITERATIVE VERSION #### 
    # count_eggs = 0
    # new_eggs = egg_weights[::-1] 
    
    # if egg_weights == [] or target_weight == 0:
    #   return 0
    # elif target_weight in egg_weights:
    #     count_eggs = count_eggs + 1
    #     return count_eggs
    # else:
    #     for i in new_eggs:
    #         while i <= target_weight:
    #             target_weight = target_weight - i 
    #             count_eggs += 1
    #     return count_eggs
    
    ########
    
    new_eggs = egg_weights
    
    if target_weight in memo:
        return memo[target_weight]
    elif len(new_eggs) == 1:     
        result = target_weight
    elif new_eggs[-1] > target_weight:      
        result = dp_make_weight(new_eggs[:-1], target_weight, memo)
    else:
        nextItem = new_eggs[-1]
        Withvalue = dp_make_weight(new_eggs, target_weight - nextItem, memo)
        Withvalue += 1
        
        WithoutValue = dp_make_weight(new_eggs[:-1], target_weight, memo)
        
        if Withvalue > WithoutValue:
            result = WithoutValue
        else:
            result = Withvalue
    memo[target_weight] = result
    return result
                
        
        


# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    egg_weights = (1, 5, 10, 25)
    n = 99
    print("Egg weights = (1, 5, 10, 25)")
    print("n = 99")
    print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()