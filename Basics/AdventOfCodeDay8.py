with open('input.txt', 'r') as text:
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
    print(operation)
    print(number)
    if operation == '+':
        line_number = (int(number) + int(line_number))
    elif operation == '-':
        line_number = ((int(line_number)) - int(number))

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
        start_me(jump_to_index)
    elif procedure == 'nop':
        print('no operation')

    # for line in range(start_index, len(bag[start_index:])):
    #     print(f'starting again at {start_index}')
    #     global initial_value
    #     print('value is : {}'.format(initial_value))
    #     print('value is : {}'.format(initial_value))
    #
    #     for line in range(start_index, len(bag)):
    #         # print(bags[line])
    #
    #         if lines[line].startswith('acc'):
    #             initial_value = acc_opp(bag[line], initial_value)
    #             print('operation is : {}'.format(initial_value))
    #
    #         elif bag[start_index].startswith('jmp'):
    #             index = jmp_opp(bag[start_index], line)
    #             # if index == -1:
    #             #     print(initial_value)
    #             #     exit(0)
    #
    #             print('line number is : {}'.format(index))
    #             start_me(index)
    #         elif bag[line].startswith('nop'):
    #             print('nop operation')
    #             continue


def start_me(starting_i):
    for index, line in enumerate(range(starting_i, len(lines))):
        if line in indexes_traveled:
            print('I have been to index {} with a line of {}'.format(line, lines[line]))
            #exit(0)
        indexes_traveled.append(line)
        print(f'{lines[line]} is the current line with starting index of {starting_i + line} and value of {initial_value}')
        # procedure = lines[line][:3]
        go_to(lines[line], starting_i)


print(start_me(0))
