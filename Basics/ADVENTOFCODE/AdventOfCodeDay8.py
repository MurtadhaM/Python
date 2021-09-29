with open('file.txt', 'r') as text:
    lines = text.read().split("\n")
initial_value = 0
indexes_traveled = list()





def acc_opp(line_opp, value):
    output = 0
    # print(line_opp)
    operation = line_opp.split(' ')[1][0]
    number = line_opp.split(' ')[1][1:]

    # print(operation)
    # print(number)
    if operation == '+':
        # print((int(number) + int(value)))
        output = (int(number) + int(value))
        print(f'adding and the  result is {output} because {value} + {number} = {output}')

    elif operation == '-':
        # print((int(value)) - int(number))
        output = ((int(value)) - int(number))
        print(f'subtracting and the  result is {output} because {value} - {number} = {output}')

    return output


def jmp_opp(line_opp, line_number):
    operation = line_opp.split(' ')[1][0]
    number = line_opp.split(' ')[1][1:]
    if operation == '+':
        line_number = (int(number) + int(line_number)) - 1
    elif operation == '-':
        line_number = ((int(line_number)) - int(number)) + 1

    return line_number


def go_to(bag, start_index):
    global initial_value
    procedure = bag[:3]
    print(procedure)
    if procedure == 'acc':
        initial_value = acc_opp(bag, initial_value)
        print('The value is: {}'.format(initial_value))
    elif procedure == 'jmp':
        jump_to_index = jmp_opp(bag, start_index)
        print(f'trying to jump to index {jump_to_index}')
        # start_me(jump_to_index)
    elif procedure == 'nop':
        print('no operation')
        go_to(bag, start_index + 1)


# def start_me(starting_i):
#     for index, line in enumerate(range(starting_i, len(lines))):
#         if line in indexes_traveled:
#             print('I have been to index {} with a line of {}'.format(line, lines[line]))
#             #exit(0)
#         indexes_traveled.append(line)
#         print(f'{lines[line]} is the current line with starting index of {starting_i + line} and value of {initial_value}')
#         # procedure = lines[line][:3]
#         go_to(lines[line], starting_i)

for index, line in enumerate(lines):
    print(go_to(line, index))
    if(index > 3):
        break
