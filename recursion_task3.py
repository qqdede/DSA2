#recursion task 3 DSA2
#Andreea Dobre
#27/10/2026

#defining the function 'follow_instructions' where the function expect
#a list of strings and returning a list of integers
def follow_instructions(instructions: list[str]) -> list[int]:
    #another function in the main one: recursive function, because it calls itself recursively
    #follow - travel from the current index of the list and return list of visited indexes
    def follow(i: int) -> list[int]:
        #first condition: index is inside the list
        if i >= len(instructions):
            return []

        # record the current index and check the color of the element
        visited = [i]
        colour = instructions[i]

        #colour check for blue
        #if it is blue, we need to go to the index of next blue
        if colour == "blue":
            #check for blue from the next index until the last one in lenght of the list
            j = i + 1
            while j < len(instructions) and instructions[j] != "blue":
                j = j + 1
            # if no blue was found, stop
            if j == len(instructions):
                return visited
            #if next blue is found, we move to the next index, after the blue
            return visited + follow(j + 1)

        #colour check for red
        elif colour == "red":
            #move to index 2*i + 1
            return visited + follow(2 * i + 1)

        #colour check for green
        elif colour == "green":
            #move to the next element
            return visited + follow(i + 1)

        #stop if the value is not a recognised colour (out of reach)
        else:
            return visited

    #check if list is empty, and if empty, return empty list
    if len(instructions) == 0:
        return []

    #otherwise, start the recursive process at index 0 
    return follow(0)


#list1
list1 = [
    "green", "red", "blue", "green", "blue",
    "red", "green", "blue", "green", "blue",
    "green", "blue", "red", "blue", "red", "green"
]
print(follow_instructions(list1))


#list2
list2 = [
    "red", "green", "blue", "red", "green",
    "blue",  "green", "red", "green", "blue",
    "green", "green", "blue", "blue", "red",
    "red", "green", "red", "green", "blue"
]
print(follow_instructions(list2))
