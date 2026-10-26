numbers = input("Enter the elements of your sorted array (elements separated by spaces): ")
array = numbers.split()
for i in range (len(array)):
    array[i] = int(array[i])
print("The sorted array is: ", array)
