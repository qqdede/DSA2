def LinearSearch(numbers, target):

    for i in range (0,len(numbers)):
        if numbers[i]==target:
            print("I found the number "+str(target)+" in the index "+str(i)+ " of the array.")
            return i
