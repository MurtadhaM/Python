"""
Author: 
Description:

HOW TO:
# in terminal run:

# to install dependencies
pip3 install flash requests urllib3 

# set environment variables

export FLASK_APP=app
export FLASK_ENV=development

# run the app
flash run

 """

from distutils.log import debug
from urllib import request
from flask import Flask, render_template
from flask import Flask, request


# Create the application instance
app = Flask(__name__)

# PART 1: HALLOWEEN days countdown


@app.route('/')
# calculate the days left til Halloween
def welcome():
    numberofdays = 31 - 24
    return render_template('index.html', numberofdays=numberofdays)

# PART # 2: Animal Image based on input from 1 to 5


@app.route('/pictures/', methods=['GET'])
def get_animal_image():
    # parameter from GET request
    if request.method == 'GET' and request.args.get('animal') == None:
        # get the number url parameter from the request
        return render_template('image.html')
    elif request.method == 'GET' and request.args.get('animal') != None:
        animal = request.args.get('animal')
        # get the image url from the API
        images = ['https://cdn.britannica.com/39/7139-050-A88818BB/Himalayan-chocolate-point.jpg?w=400&h=300&c=crop', 'https://cdn.britannica.com/60/156360-131-C899B352/sounds-Spotted-hyenas-giggles-whoops.jpg', 'https://aldf.org/wp-content/uploads/2018/05/lamb-iStock-665494268-16x9-e1559777676675-1200x675.jpg',
                  'https://www.niabizoo.com/wp-content/uploads/2018/05/ms-animals-habitats-mammals.jpg', 'https://s28151.pcdn.co/wp-content/uploads/sites/2/2022/03/Coyote-animal-sentience-research.jpg', 'https://i.guim.co.uk/img/media/665955f7f484b9f5b15d11a95ba1d0fa8a098873/0_192_3627_2176/master/3627.jpg?width=1200&height=1200&quality=85&auto=format&fit=crop&s=e4e7637ea0cc4382c989a4e56c55c580']

        # input validation
        if type(int(animal)) == int and int(animal) < 6 and int(animal) > 0:
            debug('animal is less than 5 characters')
            return render_template('animal.html', image=images[int(animal)])
        else:
            return render_template('image.html')
