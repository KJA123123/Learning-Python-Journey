
# pass functionality
names = ['Joyce', 'Hannah', 'Manny', 'Manoj', 'Ezekiel']

for name in names:
    if 'j' in name.lower():  # Skips any names which contain a j
        pass  # Skips the if statement and else
    else:
        print(name)
print()

# Break functionality
names = ['Joyce', 'Hannah', 'Manny', 'Manoj', 'Ezekiel']

for name in names:
    if 'h' in name.lower():
        break
    else:
        print(name)
print()

# Continue funcitonality
names = ['Joyce', 'Hannah', 'Manny', 'Manoj', 'Ezekiel']

for name in names:
    if 'm' in name.lower():
        continue
    else:
        print(name)
print()
