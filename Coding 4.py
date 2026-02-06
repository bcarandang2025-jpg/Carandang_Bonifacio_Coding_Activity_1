friends = ["Jo", "Angel", "JH", "JB"]

for i in range(len(friends)):
    if i == len(friends) - 1:
        print("and " + friends[i])
    else:
        print(friends[i], end=", ")

jim, Angel, JH, JB = friends

friends = []

n = int(input("How many friends do you want to add? "))

for i in range(n):
    name = input(f"Enter name {i+1}: ")
    friends.append(name)

print("\nFriends list:", friends)

# Remove a name
remove_name = input("Enter a name to remove: ")
if remove_name in friends:
    friends.remove(remove_name)

# Sort the list
friends.sort()

print("Sorted list:", friends)