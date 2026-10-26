#author: Andreea Dobre
#date: 05/10/2026
#This program bubble sorts the words "London", "Canterbury", "York" and "Leicester" by their length (in ascending order) and prints the result out.
# First, we define our input as an array of strings
cities = ["London", "Canterbury", "York", "Leicester"]

# You can also try it with a very long list. Uncomment this line to do so.
# cities = ['Lancaster', 'Sunderland', 'Wolverhampton', 'Nottingham', 'Oxford', 'Plymouth', 'Salisbury', 'Salford', 'Wakefield', 'Lichfield', 'Wells', 'Preston', 'Brighton and Hove', 'St Albans', 'Kingston upon Hull', 'Chichester', 'Durham', 'Liverpool', 'Bath', 'Bradford', 'Cambridge', 'Ely', 'York', 'Exeter', 'Birmingham', 'Carlisle', 'Portsmouth', 'Chester', 'Ripon', 'Coventry', 'Gloucester', 'Sheffield', 'Winchester', 'Lincoln', 'Canterbury', 'Westminster', 'Newcastle upon Tyne', 'Peterborough', 'Worcester', 'Leeds', 'Norwich', 'Stoke-on-Trent', 'Southampton', 'Bristol', 'Derby', 'Truro', 'Manchester', 'Hereford', 'City of London', 'Leicester']

# Assume a swap has happened so the while loop starts
has_swapped = True

# Keep sorting until no swaps are needed
while has_swapped:
    # Reset swap flag at the start of each pass
    has_swapped = False
    for i in range (len(cities)-1):
        if len(cities[i]) > len(cities[i+1]):
            cities[i], cities[i+1] = cities[i+1], cities[i]
            has_swapped = True
print("Sorted list by length using bubble sort: ", cities)
