available_rows = [
    0,
    127
]

available_columns = [
    0,
    7

]


file = open('../input.txt')

contents = file.read()

numbers = list()

def partition_input(input):
    available_rows1 = available_rows
    #column =
    if input == 'B':
        distance = available_rows1[1] - available_rows1[0]
        if distance <= 1:
            # print('row is: ' + str(available_rows1[1]))
            return available_rows1[1]
            #row = available_rows1[1]
        available_rows1[0] = int(available_rows1[0] + (distance / 2)) + 1

    elif input == 'F':
        distance = available_rows1[1] - available_rows1[0]
        if distance <= 1:
            #print('row is: ' + str(available_rows[0]))
            return available_rows[0]
            # row = available_rows1[0]

        available_rows1[1] = int(available_rows1[0] + (distance / 2))
        # print(available_rows)

    else:
        print('else  is : ' + str(input))


def partition_columns(columns):
    available_columns1 = available_columns
    if columns == 'R':
        distance = available_columns1[1] - available_columns1[0]
        if distance <= 2:
            #print('column is: ' + str(available_columns1[1]))
            return available_columns1[1]
        available_columns1[0] = int(available_columns1[0] + (distance / 2)) + 1
    if columns == 'L':
        distance = available_columns1[1] - available_columns1[0]
        if distance <= 2:
            #print('column is: ' + str(available_columns1[0]))
            return available_columns1[0]
        available_columns1[1] = int(available_columns1[1] - (distance / 2))

rows = list()
columns = list()
for ticket in contents.split('\n'):
    available_columns[0] = 0
    available_columns[1] = 7
    available_rows[0] = 0
    available_rows[1] = 127
    my_set = list()
    ticket1 = ticket.strip()
    #print(ticket1)

    for char in ticket1[:7]:
        row = partition_input(char)
        if type(row) is int:
            rows.append(row)
          #  print(row)
    for char in ticket1[7:]:
        column = partition_columns(char)
        if type(column) is int:
            columns.append(column)
           # print(column)

        #my_set.append(column)

    #total = row * 8 + column
    #numbers.append(total)
    #print(my_set)

#print(str(numbers))

for number in zip(rows, columns):
    #print(number[0] * 8 + number[1])
    numbers.append(number[0] * 8 + number[1])


#print(max(numbers))
numbers = sorted(numbers)
#print(numbers)

# for part 2
for index , seat in enumerate(numbers):
    if abs(seat - numbers[index - 1]) == 2:
        print(numbers[index ] -1 )

    #print(numbers[num])
