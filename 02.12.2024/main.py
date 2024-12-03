def get_file():
    file = open("input.prod", "r")
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

    return numbers

def is_increasing(numbers):
    return all(numbers[i] < numbers[i + 1] for i in range(len(numbers) - 1))

def is_decreasing(numbers):
    return all(numbers[i] > numbers[i + 1] for i in range(len(numbers) - 1))

def check_adjacent_difference(numbers):
    return all(1 <= abs(numbers[i] - numbers[i + 1]) <= 3 for i in range(len(numbers) - 1))

def is_safe(numbers):
    return (is_increasing(numbers) or is_decreasing(numbers)) and check_adjacent_difference(numbers)

def can_be_safe_with_one_removal(numbers):
    for i in range(len(numbers)):
        modified_numbers = numbers[:i] + numbers[i+1:]
        if is_safe(modified_numbers):
            return True
    return False

def main01():
    numbers = get_file()
    count = 1
    for i in numbers:
        if is_increasing(i) or is_decreasing(i):
            if check_adjacent_difference(i):
                count += 1
    return count

def main02():
    numbers = get_file()
    safe_count = 0

    for line in numbers:
        if is_safe(line) or can_be_safe_with_one_removal(line):
            safe_count += 1

    return safe_count

if __name__ == "__main__":
    print(main01())
    print(main02())