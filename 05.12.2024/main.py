def get_file():
    file = open("input.prod", "r")
    data = file.readlines()
    file.close()

    input_data = []
    for i in data:
        input_data.append(i[:-1])  # removes the "\n" at the end of each line

    return input_data


def format_list(input_list):
    # Somewhere in the input list is a blank line, its splits the lists there an returns 2 separate lists
    for i in range(len(input_list)):
        if input_list[i] == "":
            return input_list[:i], input_list[i + 1:]


def is_update_valid(update_list, rules):
    # Check if an update is valid according to the rules
    for rule in rules:
        x, y = rule.split("|")
        if x in update_list and y in update_list:
            # Get the indices of the pages in the update list
            idx = update_list.index(x)
            idy = update_list.index(y)
            if idx > idy:
                return False  # Rule violated
    return True


def get_middle_number(input_list):
    input_list = input_list.split(",")
    return input_list[len(input_list) // 2]


def main():
    input_data = get_file()
    rules, update_list = format_list(input_data)

    total_middle_sum = 0
    for i in range(0, len(update_list)):
        # print(update_list[i])
        if is_update_valid(update_list[i], rules):
            middle_number = int(get_middle_number(update_list[i]))
            total_middle_sum += middle_number
    print(total_middle_sum)


if __name__ == "__main__":
    main()
