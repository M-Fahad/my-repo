# Exercise 3-1
names = ["Alice", "Bob", "Charlie"]
for name in names:
    print(name)

# Exercise 3-2
names = ["Alice", "Bob", "Charlie"]
for name in names:
    print(f"Hello, {name}!")

# Exercise 3-3
transportation = ["motorcycle", "car", "bicycle"]
for mode in transportation:
    print(f"I would like to own a {mode}.")

# Exercise 3-4
guests = ["Albert Einstein", "Marie Curie", "Isaac Newton"]
for guest in guests:
    print(f"Dear {guest}, you are invited to dinner.")

# Exercise 3-5
guests = ["Albert Einstein", "Marie Curie", "Isaac Newton"]
print("Sorry, Marie Curie can't make it.")

guests[1] = "Nikola Tesla"  # Replace Marie Curie with Nikola Tesla

for guest in guests:
    print(f"Dear {guest}, you are still invited to dinner.")

# Exercise 3-6
guests = ["Albert Einstein", "Marie Curie", "Isaac Newton"]
print("I found a bigger table!")

guests.insert(0, "Galileo Galilei")  # Add to the beginning
guests.insert(2, "Stephen Hawking")   # Add to the middle
guests.append("Ada Lovelace")          # Add to the end

for guest in guests:
    print(f"Dear {guest}, you are invited to dinner.")

# Exercise 3-7
guests = ["Albert Einstein", "Marie Curie", "Isaac Newton", "Nikola Tesla", "Stephen Hawking"]
print("I can only invite two people for dinner.")

while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry, {removed_guest}, I can't invite you to dinner.")

for guest in guests:
    print(f"Dear {guest}, you are still invited to dinner.")

# Remove the last two names
while guests:
    del guests[-1]

print(guests)  # Should print an empty list

# Exercise 3-8
places = ["Paris", "Tokyo", "New York", "Cairo", "Sydney"]
print("Original list:", places)

print("Sorted (alphabetical):", sorted(places))
print("Original list after sorted():", places)

print("Sorted (reverse-alphabetical):", sorted(places, reverse=True))
print("Original list after sorted():", places)

places.reverse()
print("Reversed list:", places)

places.reverse()
print("Back to original order:", places)

places.sort()
print("Sorted list:", places)

places.sort(reverse=True)
print("Sorted (reverse-alphabetical):", places)

# Exercise 3-9
items = ["mountains", "rivers", "countries", "cities", "languages"]

# Using various list methods
print("Original list:", items)
print("Count of 'countries':", items.count("countries"))
print("Index of 'cities':", items.index("cities"))
items.append("forests")
print("After append:", items)
items.insert(2, "oceans")
print("After insert:", items)
items.remove("rivers")
print("After remove:", items)
popped_item = items.pop()
print("Popped item:", popped_item)
print("After pop:", items)
items.sort()
print("Sorted list:", items)
items.reverse()
print("Reversed list:", items)
items.clear()
print("Cleared list:", items)

# Exercise 3-10
items = ["apple", "banana", "cherry"]
# This will produce an IndexError since index 3 does not exist
print(items[3])
