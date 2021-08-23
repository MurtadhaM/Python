# Author: Murtadha Marzouq

int = 1
float = 1.1
string = "str"
bool = True


result = str(type(string)) + str(type(int))
result = result.replace("<class '", "")
result = result.replace("'>", " ")

print(result)


