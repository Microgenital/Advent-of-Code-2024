def get_file():
    file = open("input.prod", "r")
    data = file.readlines()
    file.close()

    input = []
    for i in data:
        input.append(i[:-1])  # removes the "\n" at the end of each line

    return input