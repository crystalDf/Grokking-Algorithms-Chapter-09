from prettytable import PrettyTable


def calculate_longest_common_substring(word_a, word_b):

    cells = [[0 for col in range(len(word_b))] for row in range(len(word_a))]

    for i in range(len(word_a)):
        for j in range(len(word_b)):
            if word_a[i] == word_b[j]:
                if i == 0 or j == 0:
                    cells[i][j] = 1
                else:
                    cells[i][j] = cells[i - 1][j - 1] + 1
            else:
                cells[i][j] = 0

    return cells


def format_print_cells(word_a, word_b, cells):

    headers = [""]

    for j in range(len(word_b)):
        headers.append(str(j + 1))

    table = PrettyTable(headers)

    row = [""]
    for j in range(len(word_b)):
        row.append(word_b[j])
    table.add_row(row)

    for i in range(len(word_a)):
        row = [word_a[i]]
        for j in range(len(word_b)):
            row.append(cells[i][j])
        table.add_row(row)

    print(table)


def find_most_similar_word(input_word, candidates):

    max_value = 0
    target_word = ""

    for candidate in candidates:
        cells = calculate_longest_common_substring(input_word, candidate)
        value = calculate_value_in_cells(cells)
        if value > max_value:
            max_value = value
            target_word = candidate

    return target_word


def calculate_value_in_cells(cells):

    value = 0

    for i in range(len(cells)):
        for j in range(len(cells[i])):
            if cells[i][j] > value:
                value = cells[i][j]

    return value


my_cells = calculate_longest_common_substring("HISH", "FISH")
format_print_cells("HISH", "FISH", my_cells)

my_cells = calculate_longest_common_substring("HISH", "VISTA")
format_print_cells("HISH", "VISTA", my_cells)

print(find_most_similar_word("HISH", ["FISH", "VISTA"]))

my_cells = calculate_longest_common_substring("BLUE", "CLUES")
format_print_cells("BLUE", "CLUES", my_cells)