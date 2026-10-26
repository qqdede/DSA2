target=int(input("Please enter an integer: "))

numbers = [3,4,90,75,382,2,8,3,55,32,1,19,0,11]

for i in range (0,len(numbers)):
    if numbers[i]==target:
        print("I found the number "+str(target)+" in the index "+str(i)+ " of the array.")
    else:
        print("Number not found in the index of the array.")
