file = open("input.test", "r")
data = file.readlines()
file.close()

# Clean the data
input = []
for i in data:
    input.append(i[:-1]) # removes the "\n" at the end of each line

# split the data into seperate ints and add them to a list
# the numbers are in the format: "3 10 5 3 7"

numbers = []
for i in input:
    numbers.append(i.split(" "))

# change a list of strings to a list of ints
for i in range(len(numbers)):
    for j in range(len(numbers[i])):
        numbers[i][j] = int(numbers[i][j])

# check if the numbers are increasing or decreasing, if 2 numbers in a row are the same, the list is not increasing or decreasing

def is_increasing(numbers):
    return all(numbers[i] < numbers[i + 1] for i in range(len(numbers) - 1))

def is_decreasing(numbers):
    return all(numbers[i] > numbers[i + 1] for i in range(len(numbers) - 1))


for i in numbers:
    if is_increasing(i) or is_decreasing(i):
        print(i)

