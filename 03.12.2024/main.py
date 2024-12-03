import re


def get_file():
    file = open("input.prod", "r")
    data = file.readlines()
    file.close()

    # Clean the data
    input = []
    for i in data:
        input.append(i[:-1])  # removes the "\n" at the end of each line
    datas = ""
    for i in input:
        datas += i
    return datas


def find_and_multiply(input_string):
    # Regular expression to find valid mul(X,Y) instructions
    pattern = r'mul\(\d{1,3},\d{1,3}\)'
    matches = re.findall(pattern, input_string)

    total_sum = 0

    for match in matches:
        numbers = re.findall(r'\d+', match)
        x, y = int(numbers[0]), int(numbers[1])
        total_sum += x * y

    return total_sum


def find_and_multiply_on_off(input_string):
    # Regular expression to find valid mul(X,Y) instructions
    pattern = r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)'
    matches = re.findall(pattern, input_string)

    total_sum = 0
    mul_enabled = True  # Initially, mul instructions are enabled

    for match in matches:
        if match == 'do()':
            mul_enabled = True
        elif match == "don't()":
            mul_enabled = False
        elif mul_enabled and match.startswith('mul'):
            # Extract the numbers from the match
            numbers = re.findall(r'\d+', match)
            x, y = int(numbers[0]), int(numbers[1])
            # Perform the multiplication and add to the total sum
            total_sum += x * y

    return total_sum


if __name__ == "__main__":
    print(find_and_multiply(get_file()))
    print(find_and_multiply_on_off(get_file()))
