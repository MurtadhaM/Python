# Get them Values
values_dict = {'(1,2)': '10', '(2,3)': '5', '(3,4)': '10'}
# Get Daddy man to enter an  answer
the_input = input("Enter the link daddy man: ")
# Parse out the value based on the 2 inputs
first_value = str(the_input).strip("()")[0]

second_value = str(the_input).strip("()")[2]
output_value = values_dict.get(the_input)
# This only works with Python 3.9 or maybe 3.6
#ONLY WORKS FOR 3.9
#print(f'The Link between {first_value} and {second_value} is: {output_value} MB')
print('The Link between {} and {} is: {} MB'.format(first_value,second_value,output_value))

