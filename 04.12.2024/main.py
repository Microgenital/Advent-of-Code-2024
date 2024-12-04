import re


def get_file():
    file = open("input.test", "r")
    data = file.readlines()
    file.close()

    input = []
    for i in data:
        input.append(i[:-1])  # removes the "\n" at the end of each line

    return input


def find_xmas(input):
    pattern = r'XMAS|SAMX'
    matches = 0
    for i in input:
        if re.search(pattern, i):
            matches += 1
    return matches


if __name__ == "__main__":
    print(find_xmas(get_file()))
