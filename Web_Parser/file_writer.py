# Author: Murtadha Marzouq
# Program: This class will handle the file output/input operations

import os


# Each website is a separate project (folder)

def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating directory ' + directory)
        os.makedirs(directory)


# Create queue and crawled files (if not created)

def create_data_files(project_name, base_url):
    crawled_data = os.path.join('OUTPUT', 'data.csv')
    link_file = os.path.join('OUTPUT', ' links.csv')

    if not os.path.isfile(crawled_data):
        write_file(crawled_data, base_url)
    if not os.path.isfile(link_file):
        write_file(link_file, base_url)


# Create a new file
def write_file(path, data):
    with open(path, 'w') as f:
        f.write(str(data))



# Add data onto an existing file
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')


# Delete the contents of a file
def delete_file_contents(path):
    open(path, 'w').close()


# Read a file and convert each line to set items
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results


# Iterate through a set, each item will be a line in a file
def set_to_file(links, file_name):
    with open(file_name, "w") as f:
        print(links)
        for l in sorted(links):
            f.write(l + "\n")
