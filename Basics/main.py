# Author: Murtadha Marzouq
# Program to parse user input

import argparse

# Set a parser
parser = argparse.ArgumentParser(description='Process Passed-in Parameters.')
# Add a url Parameter
parser.add_argument('--url', type=str, nargs='+', default="https://google.com",
                    help='a string for the url (default: https://google.com)')
# Add a depth parameter
parser.add_argument('--depth', type=int, default='1',
                    help='set the depth of of the crawler (default: 1)')
# Add log to files
parser.add_argument('--log', type=bool, default=False,
                    help='Log to files (default: False)')


# Parse The Arguments
args = parser.parse_args()
# Print the url
print("The url is: " + str(args.url))
# Print the crawl depth
print("The depth is: " + str(args.depth))
# Print the log switch
print("logging now is : " + str(args.log))
