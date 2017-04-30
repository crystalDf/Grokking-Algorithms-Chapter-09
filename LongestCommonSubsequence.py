from prettytable import PrettyTable


def calculate_longest_common_subsequence(word_a, word_b):

    cells = [[0 for col in range(len(word_b))] for row in range(len(word_a))]

    for i in range(len(word_a)):
        for j in range(len(word_b)):
            if word_a[i] == word_b[j]:
                if i == 0 or j == 0:
                    cells[i][j] = 1
                else:
                    cells[i][j] = cells[i - 1][j - 1] + 1
            else:
                if i == 0 and j > 0:
                    cells[i][j] = cells[i][j - 1]
                elif i > 0 and j == 0:
                    cells[i][j] = cells[i - 1][j]
                else:
                    cells[i][j] = max(cells[i - 1][j], cells[i][j - 1])

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
        cells = calculate_longest_common_subsequence(input_word, candidate)
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


my_cells = calculate_longest_common_subsequence("FOSH", "FISH")
format_print_cells("FOSH", "FISH", my_cells)

my_cells = calculate_longest_common_subsequence("FOSH", "FORT")
format_print_cells("FOSH", "FORT", my_cells)

print(find_most_similar_word("FOSH", ["FISH", "FORT"]))
