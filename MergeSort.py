import numpy as np

# Recursive mergesor implementation
def mergesort(array):

    #print("Mergesorting array " + str(array))
    
    if len(array) == 1: # Can't divide it further, return it
        return array

    middle_of_array = int(len(array) / 2) # int() rounds down into an integer

    left_array = array[0:middle_of_array]
    right_array = array[middle_of_array : len(array)]

    # Recursive part
    sorted_left_array = mergesort(left_array)
    sorted_right_array = mergesort(right_array)

    # Once sorted, merge
    sorted_array = merge_arrays(sorted_left_array, sorted_right_array)
    #print("Merged " + str(sorted_left_array) + " and " + str(sorted_right_array) + " into " + str(sorted_array))

    return sorted_array

# Merges 2 arrays together. If both arrays are sorted independently, the merged array is also sorted
def merge_arrays(array1, array2):

    merged_array_length = len(array1) + len(array2)

    result = np.empty(shape = merged_array_length)

    element_in_array1 = 0
    element_in_array2 = 0

    for i in range(0, merged_array_length):
        
        if element_in_array1 == len(array1):
            # We have reached the end of array 1. Next element must come from array2
            result[i] = array2[element_in_array2]
            element_in_array2 = element_in_array2 + 1
            continue # Continue means that this step on the loop will end here

        if element_in_array2 == len(array2):
            # We have reached the end of array 2. Next element must come from array1
            result[i] = array1[element_in_array1]
            element_in_array1 = element_in_array1 + 1
            continue # Continue means that this step on the loop will end here


        if array1[element_in_array1] <= array2[element_in_array2]:
            result[i] = array1[element_in_array1]
            element_in_array1 = element_in_array1 + 1
        else:
            result[i] = array2[element_in_array2]
            element_in_array2 = element_in_array2 + 1

    return result

