#author: Andreea Dobre
#date: 01/10/2026
#This program sorts integers and prints the result out.


# First, we define var as randint(lowest possible number, higher possible number, size)
import numpy as np
var = np.random.randint(0,500,3)

# Initialize our result, which will be empty for now
result = []

# Initialize our loop variables
i = 0
j = 0
number_of_var = len(var)
n = number_of_var

number_of_steps = 0

#sort using selection sort
for i in range(number_of_var):
    minimum_element = var[0]

    for j in range(n):
        if var[j] < minimum_element:
            minimum_element = var[j]

        number_of_steps = number_of_steps + 1

        # At the end of the second loop, we will have the shorter element in minimum_element
        # We just need to add it to our results and remove it from our working list
        
    result.append(minimum_element)
    var.remove(minimum_element)
    n = n - 1

print("The alphabetically ordered list is:")
print(result)
print("The list had " + str(number_of_var) + " integers and I ordered it in " + str(number_of_steps) + " steps.")


