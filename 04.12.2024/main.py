def get_file():
    file = open("input.prod", "r")
    data = file.readlines()
    file.close()

    input = []
    for i in data:
        input.append(i[:-1])  # removes the "\n" at the end of each line

    return input


def find_xmas(grid):
    def search_word(x, y, dx, dy):
        word = "XMAS"
        for i in range(len(word)):
            if not (0 <= x < len(grid) and 0 <= y < len(grid[0])):
                return False
            if grid[x][y] != word[i]:
                return False
            x += dx
            y += dy
        return True

    directions = [
        (0, 1), (1, 0), (1, 1), (1, -1),  # right, down, down-right, down-left
        (0, -1), (-1, 0), (-1, -1), (-1, 1)  # left, up, up-left, up-right
    ]

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for dx, dy in directions:
                if search_word(i, j, dx, dy):
                    count += 1
    return count


if __name__ == "__main__":
    grid = [list(row) for row in get_file()]
    print(find_xmas(grid))
