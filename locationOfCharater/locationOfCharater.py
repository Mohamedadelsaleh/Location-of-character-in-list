text = input("Please Enter Your Text here:")
location = []
i = 0
for letter in text:
    if letter == 'i':
        location.append(i)
    i += 1

print("Locations of [i] in text is : ", location)

