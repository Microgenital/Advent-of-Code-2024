file = open("input.test", "r")
data = file.readlines()
file.close()

# Clean the data
input = []
for i in data:
    input.append(i[:-1]) # removes the "\n" at the end of each line

print(input)