def get_file():
    file = open("input.test", "r")
    data = file.readlines()
    file.close()

    input = []
    for i in data:
        input.append(i[:-1])  # removes the "\n" at the end of each line

    return input

def format(list):
    # Somewhere in the input list is a blank line, its splits the lists there an returns 2 separate lists
    for i in range(len(list)):
        if list[i] == "":
            return list[:i], list[i+1:]

def is_update_valid(update_list, rules):
    # Check if an update is valid according to the rules
    for rule in rules:
        x, y = rule.split("|")
        if x in update_list and y in update_list:
            # Get the indices of the pages in the update list
            idx_x = update_list.index(x)
            idx_y = update_list.index(y)
            if idx_x >= idx_y:
                return False  # Rule violated
    return True

def get_middle_number(input_list):
    return input_list[len(input_list) // 2]

def main():
    input_data = get_file()
    update_list, rules = format(input_data)
    print(update_list)
    print(rules)

    total_middle_sum = 0
    for i in range(1, len(update_list)):
        if is_update_valid(rules[:i], update_list):
            middle_number = int(get_middle_number(update_list[:i]))
            total_middle_sum += middle_number
    print(total_middle_sum)

    # FIXME: something with "update_list" and "rules" is wrong, need to figure out what is what

if __name__ == "__main__":
 main()