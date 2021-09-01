import requests
from bs4 import BeautifulSoup

import html_parser

output = '2'


class main():
    def __init__(self, *args):
        # print(args.__len__())
        if (args.__len__() > 0):
            self.url = args[0]
            self.depth = args[1]

    def parse_page(self, page):
        contents = BeautifulSoup(page.text, 'html.parser')
        print(contents.)
        #parsed_contents = contents.find()
        #parsed_contents = parsed_contents.prettify()
        return contents

    def make_request(self):
        response = requests.get(self.url)
        return response

    def main(self):
        response = self.make_request()
        o = self.parse_page(response)
        return o



m = main("https://charlotte.edu", 2)
#print(m.main())
m.main()
#m.print_output()
