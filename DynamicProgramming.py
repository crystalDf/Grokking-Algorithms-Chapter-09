from prettytable import PrettyTable


class Item:
    def __init__(self, name, value, cost):
        self.name = name
        self.value = value
        self.cost = cost


def dynamic_programming(item_arr, column_num, cell, granularity):

    if cell is None:
        old_cell_size = 0
        cell = [[[] for col in range(column_num)]
                for row in range(len(item_arr))]
    else:
        old_cell_size = len(cell)

        for row in range(len(item_arr) - old_cell_size):
            new_row = [[] for col in range(column_num)]
            cell.append(new_row)

    for i in range(old_cell_size, len(item_arr)):
        for j in range(column_num):
            if i == 0:
                first_arr = []
                if j + 1 >= item_arr[i].cost / granularity:
                    second_arr = [item_arr[i]]
                else:
                    second_arr = []
            else:
                first_arr = cell[i - 1][j]
                if j + 1 == item_arr[i].cost / granularity:
                    second_arr = [item_arr[i]]
                elif j + 1 > item_arr[i].cost / granularity:
                    second_arr = cell[i - 1][int(j - item_arr[i].cost /
                                                 granularity)] + [item_arr[i]]
                else:
                    second_arr = []

            if calculate_cell(first_arr) >= calculate_cell(second_arr):
                cell[i][j] = first_arr
            else:
                cell[i][j] = second_arr

    return cell


def calculate_cell(cell_arr):
    sum_value = 0

    for item in cell_arr:
        sum_value += item.value

    return sum_value


def print_cell(cell_arr):
    item_names = str(calculate_cell(cell_arr)) + " ( "

    for item in cell_arr:
        item_names += item.name + " "

    item_names += ")"

    return item_names


def format_print_cells(item_arr, column_num, cells, granularity):

    headers = ['item']

    for col in range(column_num):
        headers.append(str((col + 1) * granularity))

    table = PrettyTable(headers)

    for i in range(len(cells)):
        row = [item_arr[i].name]
        for j in range(column_num):
            row.append(print_cell(cells[i][j]))
        table.add_row(row)

    print(table)


# Set condition

my_cell = None
my_capacity = 4
my_granularity = 1
my_column_num = int(my_capacity / my_granularity)

# Add guitar, stereo and laptop

guitar = Item("guitar", 1500, 1)
stereo = Item("stereo", 3000, 4)
laptop = Item("laptop", 2000, 3)

my_item_arr = [guitar, stereo, laptop]

my_cell = dynamic_programming(my_item_arr, my_column_num, my_cell,
                              my_granularity)

format_print_cells(my_item_arr, my_column_num, my_cell, my_granularity)

# Add iPhone

iPhone = Item("iPhone", 2000, 1)

my_item_arr.append(iPhone)

my_cell = dynamic_programming(my_item_arr, my_column_num, my_cell,
                              my_granularity)

format_print_cells(my_item_arr, my_column_num, my_cell, my_granularity)

# Add mp3

mp3 = Item("mp3", 1000, 1)

my_item_arr.append(mp3)

my_cell = dynamic_programming(my_item_arr, my_column_num, my_cell,
                              my_granularity)

format_print_cells(my_item_arr, my_column_num, my_cell, my_granularity)

# Reset condition

my_cell = None
my_capacity = 4
my_granularity = 0.5
my_column_num = int(my_capacity / my_granularity)

# Add necklace

necklace = Item("necklace", 1000, 0.5)

my_item_arr.append(necklace)

my_cell = dynamic_programming(my_item_arr, my_column_num, my_cell,
                              my_granularity)

format_print_cells(my_item_arr, my_column_num, my_cell, my_granularity)

# Reset condition

my_cell = None
my_capacity = 2
my_granularity = 0.5
my_column_num = int(my_capacity / my_granularity)

# Add attractions

westminster_abbey = Item("westminster_abbey", 7, 0.5)
globe_theater = Item("globe_theater", 6, 0.5)
national_gallery = Item("national_gallery", 9, 1)
british_museum = Item("british_museum", 9, 2)
st_paul_s_cathedral = Item("st_paul_s_cathedral", 8, 0.5)

my_item_arr = [westminster_abbey, globe_theater, national_gallery,
               british_museum, st_paul_s_cathedral]

my_cell = dynamic_programming(my_item_arr, my_column_num, my_cell,
                              my_granularity)

format_print_cells(my_item_arr, my_column_num, my_cell, my_granularity)

# Reset condition

my_cell = None
my_capacity = 6
my_granularity = 1
my_column_num = int(my_capacity / my_granularity)

# Add items

water = Item("water", 10, 3)
book = Item("book", 3, 1)
food = Item("food", 9, 2)
jacket = Item("jacket", 5, 2)
camera = Item("camera", 6, 1)

my_item_arr = [water, book, food, jacket, camera]

my_cell = dynamic_programming(my_item_arr, my_column_num, my_cell,
                              my_granularity)

format_print_cells(my_item_arr, my_column_num, my_cell, my_granularity)
