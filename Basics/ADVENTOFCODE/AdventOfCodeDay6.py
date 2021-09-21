file = open('../input.txt')

contents = file.read()

yes_count = 0

groups = contents.split('\n\n')


# for group in groups:
#    print(group)


def calculate_answers(group_answers):
    answer_key = []
    count = 0
    group_number = int(group_answers.count('\n')) + 1
    print(f'group number is {group_number}')
    # print(group_number)
    # print(answer_key)
    score = 0
    repeat_answer = 0

    for answer in group_answers:
        if answer not in answer_key and answer != '\n':
            answer_key.append(answer)

        # print(answer_key)
    for n in answer_key:
        # print(n)
        if ((str(group_answers).count(n)) == group_number):
            # print(str(group_answers).count(n))
            score += 1

    return score


# print(groups.pop(0))
# print()

for group in groups:
    group_score = calculate_answers(group)

    yes_count += group_score
    print('group score: {}'.format(group_score))
    print(group + '\n')

print(yes_count)
