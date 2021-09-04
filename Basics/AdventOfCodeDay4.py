from PIL import __getattr__

file = open('input.txt')

contents = file.read()
# contents = file.read().replace('\n', ' ').strip()

# Tags
tags = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']

valid = 0
values = list()
dictionary = dict()

#def check

def is_valid(passport):
    try:
        if passport.__contains__('hgt') and passport.__contains__('iyr') and passport.__contains__('byr')  and passport.__contains__('hcl') and passport.__contains__('eyr') and passport.__contains__('pid') and passport.__contains__('ecl'):
            print('tags valid')
        elif int(passport.get('byr')[:4]) >= 1920 and  int(passport.get('byr')[:4]) <= 2002:
            print('(Birth Year) valid')
        elif int(passport.get('iyr'))  >= 2010 and  int(passport.get('iyr')) <= 2020:
            print('(Issue Year) - valid')
        elif int(passport.get('eyr'))  >= 2020 and  int(passport.get('eyr'))  <= 2030:
            print('(Expiration Year) - valid')
        elif passport.get('hgt') and passport.get('hgt').endswith('cm'):
            print('(Height) - valid')

        else:
           return False
    except Exception as e:
        print(e)

for index, line in enumerate((contents.split('\n\n'))):
    temp = list()
    tempdict = dict()
    for index1, value in enumerate(str(line.replace('\n', ' ').split('\\n')).split(' ')):
        if len(value.split(':')) > 1:
            v = {value.strip('[\'').split(':')[0]: value.split(':')[1]}
            tempdict[value.strip('[\'').split(':')[0]] = value.split(':')[1]
            temp.append(v)

    #print(tempdict)

    dictionary.update(tempdict)
    values.append(tempdict)



# for  l in values:
#     print(str(l))

#print(dictionary.values())
#print(v)
for passport in values:
    if is_valid(passport):
        valid += 1
print(valid)

#
# for passport in values:
#     #for key in :
#for index, key in enumerate(values):
    #for index2, value in enumerate(key):
     #   print(index, key[index2])
       # print(key[index2].__doc__)
    #print(passport.keys())