#author: Sílvia Moros
#date: August 2020
#This program sorts the words "London", "Canterbury", "York" and "Leicester" by their length (in ascending order) and prints the result out.


# First, we define our input as an array of strings
cities = ["London", "Canterbury", "York", "Leicester"]

# You can also try it with a very long list. Uncomment this line to do so.
# cities = ['Lancaster', 'Sunderland', 'Wolverhampton', 'Nottingham', 'Oxford', 'Plymouth', 'Salisbury', 'Salford', 'Wakefield', 'Lichfield', 'Wells', 'Preston', 'Brighton and Hove', 'St Albans', 'Kingston upon Hull', 'Chichester', 'Durham', 'Liverpool', 'Bath', 'Bradford', 'Cambridge', 'Ely', 'York', 'Exeter', 'Birmingham', 'Carlisle', 'Portsmouth', 'Chester', 'Ripon', 'Coventry', 'Gloucester', 'Sheffield', 'Winchester', 'Lincoln', 'Canterbury', 'Westminster', 'Newcastle upon Tyne', 'Peterborough', 'Worcester', 'Leeds', 'Norwich', 'Stoke-on-Trent', 'Southampton', 'Bristol', 'Derby', 'Truro', 'Manchester', 'Hereford', 'City of London', 'Leicester']

# Initialize our result, which will be empty for now
result = []

# Initialize our loop variables
i = 0
j = 0
number_of_cities = len(cities)  # len() of a list gives you the number of elements in it
                                # len() of a string will give you the lenght of it
n = number_of_cities


number_of_steps = 0

# Sort using selection sort
for i in range(0, number_of_cities):
    minimum_length = len(cities[0])
    minimum_element = cities[0]
    

    for j in range(0, n):
        if (len(cities[j]) < minimum_length):
            minimum_length = len(cities[j])
            minimum_element = cities[j]

        number_of_steps = number_of_steps + 1

    # At the end of the second loop, we will have the shorter element in minimum_element
    # We just need to add it to our results and remove it from our working list

    result.append(minimum_element)
    cities.remove(minimum_element)
    n = n - 1


print("")
print("The ordered list is:")
print(str(result))
print("The list had " + str(number_of_cities) + " cities and I ordered it in " + str(number_of_steps) + " steps.")





#modified to sort alphabetically
#modified by Andreea Dobre on 01/10/2026
cities = ["London", "Canterbury", "York", "Leicester"]

result = []

number_of_cities = len(cities)
n = number_of_cities

number_of_steps = 0

#sort using selection sort
for i in range(number_of_cities):
    minimum_element = cities[0]

    for j in range(n):
        if cities[j] < minimum_element:
            minimum_element = cities[j]

        number_of_steps = number_of_steps + 1
        
    result.append(minimum_element)
    cities.remove(minimum_element)
    n = n - 1

print("The alphabetically ordered list is:")
print(result)
print("The list had " + str(number_of_cities) + " cities and I ordered it in " + str(number_of_steps) + " steps.")




#modified to sort intengers
#modified by Andreea Dobre on 01/10/2026
var = [12, 5, 8, 1, 20]

result = []

number_of_var = len(var)
n = number_of_var

for i in range(number_of_var):
    minimum_element = var[0]

    for j in range(n):
        if var[j] < minimum_element:
            minimum_element = var[j]

    result.append(minimum_element)
    var.remove(minimum_element)
    n = n - 1

print("The ordered list is:")
print(result)
