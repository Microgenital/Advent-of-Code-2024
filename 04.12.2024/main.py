def get_file():
    file = open("input.test", "r")
    data = file.readlines()
    file.close()

    input = []
    for i in data:
        input.append(i[:-1])  # removes the "\n" at the end of each line

    return input

print(get_file())