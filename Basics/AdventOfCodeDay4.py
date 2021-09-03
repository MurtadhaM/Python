

file = open('input.txt')
file2 = open('input.txt')

contents = file.read().strip('\n').strip().replace('\n','')
contents2 = file2.read().strip().split('\n')[::2]
