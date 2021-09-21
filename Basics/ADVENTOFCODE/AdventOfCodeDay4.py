
file = open('../input.txt')

contents = file.read()
# contents = file.read().replace('\n', ' ').strip()

# Tags
tags = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']

valid = 0
values = list()
dictionary = dict()


# def check

def check_byr(tag):
    if tag.__contains__('byr') and 1920 <= int(tag.get('byr')[:4]) <= 2002:
        return True
    else:
        print('The Byr is wrong : ' + str(tag))

        return False


def check_iyr(tag):
    if tag.__contains__('iyr') and 2010 <= int(tag.get('iyr')[:4]) <= 2020:
        return True
    else:
        print('The iyr is wrong : ' + tag.get('iyr')[:4])

        return False


def check_eyr(tag):
    if tag.__contains__('eyr') and 2020 <= int(tag.get('eyr')[:4]) <= 2030:
        return True
    else:
        print('The eyr is wrong : ' + str(tag))

        return False


def check_hgt(tag):
    stringTag = str(tag.get('hgt')).strip('\']')
    if stringTag.endswith('cm'):
        if 150 <= int(stringTag.strip('cm')) <= 193:
            return True
        else:
            return False
    elif stringTag.endswith('in'):
        if 59 <= int(stringTag.strip('in')) <= 76:
            return True
        else:
            return False
    else:
        return False


def check_hcl(tag):
    allow_characters = ['#', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', '\'', ']']

    if tag.get('hcl')[0] == '#' and len(tag.get('hcl')[:6]) >= 6:
        for char in tag.get('hcl'):
            if char in allow_characters:
                continue
            else:
                print(tag)
                return False
        return True
    else:
        print('The hcl is wrong : ' + str(tag))
        return False


def check_ecl(tag):
    string_taq = tag.get('ecl').strip('\']')
    allow_characters = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if string_taq in allow_characters:
        return True
    else:
        print('The ecl is wrong : ' + str(tag))

        return False


def check_pid(tag):
    string_taq = tag.get('pid').strip('\']')
    if len(string_taq) == 9:
        return True
    else:
        print('The pid is wrong : ' + str(tag))

        return False


def is_valid(passport):
    try:
        if passport.__contains__('hgt') and passport.__contains__('iyr') and passport.__contains__(
                'byr') and passport.__contains__('hcl') and passport.__contains__('eyr') and passport.__contains__(
            'pid') and passport.__contains__('ecl'):
            if check_byr(passport) and check_iyr(passport) and check_eyr(passport) and check_hgt(
                    passport) and check_hcl(passport) and check_ecl(passport) and check_pid(passport):
                return True
        else:
            return False

    except Exception as e:
        print(str(e) + str(passport))


for index, line in enumerate((contents.split('\n\n'))):
    temp = list()
    tempdict = dict()
    for index1, value in enumerate(str(line.replace('\n', ' ').split('\\n')).split(' ')):
        if len(value.split(':')) > 1:
            v = {value.strip('[\'').split(':')[0]: value.split(':')[1]}
            tempdict[value.strip('[\'').split(':')[0]] = value.split(':')[1]
            temp.append(v)


    dictionary.update(tempdict)
    values.append(tempdict)

for passport in values:
    if is_valid(passport):
        valid += 1
    # else:
    # print(passport)
print(valid)
