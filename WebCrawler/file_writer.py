

# this function takes in a filename and a list to write it to a file
def write_file(filename, list_contents):
    outfile = open(filename, 'w')
    for line in list_contents:
        outfile.write(line)
        outfile.write('\n')
    outfile.close()
