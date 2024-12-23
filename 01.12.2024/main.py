file = open("input.prod", "r")
input = file.readlines()
file.close()

def main_01(data):
    lines = []
    for i in data:
        lines.append(i[:-1]) # removes the "\n" at the end of each line
    list_left = []
    list_right = []

    for i in lines:
        list_left.append(int(i[0:5]))
        list_right.append(int(i[6:13]))

    # sort both lists from smallest to largest
    list_left.sort()
    list_right.sort()

    differences = []

    for i in range(len(list_left)):
        if list_left[i] > list_right[i]:
            differences.append(list_left[i] - list_right[i])
        else:
            differences.append(list_right[i] - list_left[i])

    # add all differences together
    sum = 0
    for i in differences:
        sum += i

    print(f"Solution 01: {sum}")

def main_02(data):
    lines = []
    for i in data:
        lines.append(i[:-1]) # removes the "\n" at the end of each line
    list_left = []
    list_right = []

    for i in lines:
        list_left.append(int(i[0:5]))
        list_right.append(int(i[6:13]))

    numbers = []
    # check how often a number is in the list
    for i in list_left:
        amount = list_right.count(i)
        if amount > 0:
            numbers.append(i*amount)

    # add all amounts together
    sum = 0
    for i in numbers:
        sum += i
    print(f"Solution 02: {sum}")

if __name__ == "__main__":
    main_01(input)
    main_02(input)