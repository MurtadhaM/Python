# Import the Canvas class
from canvasapi import Canvas

# Canvas API URL
API_URL = "https://uncc.instructure.com"
# Canvas API key
API_KEY = "7301~tA6shZGj3KVAHFLLpoTd9CN8KOcmdFAGxu5Elarf4FZtFOIrMOox0vT0hdoOca86"

# Initialize a new Canvas object
canvas = Canvas(API_URL, API_KEY)
courses = canvas.get_courses(enrollment_state='active')

def print_user_info():
    """
    Prints the current user's information
    """
    print(courses)


print(courses[0])

#print_user_info()