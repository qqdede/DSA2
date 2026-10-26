#author: Andreea Dobre
#date: 05/10/2026
#This program is bubble sort.

# First, we define our input as an array of integers
arr = [8, 3, 5, 1, 9, 2]

# Assume a swap has happened so the while loop starts
has_swapped = True

# Initialize our while loop, here is where swaps are being made
while has_swapped == True:
    # Reset swap flag at the start of each pass
    has_swapped = False
    # Loop through all adjacent pairs of elements
    for i in range (0, len(arr)-1):
    # If the left value is bigger than the right value
        if arr[i] > arr[i+1]:
            # Swap the two values
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1]=temp
            # Record that a swap occurred
            has_swapped = True
        else:
        # Elements are already in the correct order
            pass
print("Sorted list using bubble sort: ", arr)
