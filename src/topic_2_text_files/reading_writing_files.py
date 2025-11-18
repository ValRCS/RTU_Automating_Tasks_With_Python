# we will be showing how to read and write text files

# first we want to know what our working directory is
# we will use Path from the pathlib module
from pathlib import Path
current_dir = Path.cwd()
print(f"Current working directory: {current_dir}")

# so I know the file is called the_choice_yeats.txt 
# let's look for it recursively in the current directory
# file_list = list(current_dir.rglob("the_choice_yeats.txt"))
file_list = list(current_dir.rglob("the_choice_*.txt")) # * is a joker wildcard
# works similarly to how Windows File Explorer search works
# rglob means recursive globbing - searching through all subdirectories
# it is possible there are multiple files with the same name in subdirectories
# print how many files were found
print(f"Number of files found: {len(file_list)}")
# print all files at once
print(f"Files found: {file_list}")
# print the full path of each file found
# we create a loop to go through files one by one here
for file_path in file_list: # file_path is just a variable name could be anything
    print(f"Found file at: {file_path}")
# note the indentation after : for indicates a block of code

# let's check the length of the file list and if it is at least one get the first file
if len(file_list) > 0: # we are checking whether we found at least one file
    # we do the following block only if we found at least one file
    file_to_read = file_list[0]  # get the first file found
    # note how we access list elements by index starting at 0
    # this is very common in programming languages
    # we start 0 not 1
    print(f"Will read from file: {file_to_read}")
else:
    # we do this block if no files were found
    print("No file found. Exiting.")
    exit()  # exit the script if no file is found immediately

# so here we know we have a valid file name with location
# let's read the file
with open(file_to_read, mode='r', encoding='utf-8') as file_stream: # file_stream is just a variable name
    # 'r' means read mode
    # encoding='utf-8' ensures we read special characters correctly
    file_contents = file_stream.read()  # read the entire file into a string variable
    print("File contents read successfully.")
    # file is still technically open here within the with block
# file is automatically closed here! - this is the beauty of using 'with'

# let's pritn first 100 characters of the file
print("First 100 characters of the file:")
print(file_contents[:100])  # print the first 100 characters
# above is so called slicing of strings
# [:100] means from start to index 100 (not including 100)
# technically it is characters 0 to 99 included
# so 0 is silent we could have written [0:100] as well but not needed
# how about the last 20 characters?
print("Last 20 characters of the file:")
print(file_contents[-20:])  # print the last 20 characters
# i could have printed ALL of the contents with
# print(file_contents) but for big text files that is not practical 
# you do not want to print 100,000 characters to the console :)

# how about reading lines?
with open(file_to_read, mode='r', encoding='utf-8') as file_stream:
    lines = file_stream.readlines()  # read all lines into a list
    print(f"Total number of lines in the file: {len(lines)}")
    # file_stream is still open here
# file_stream is closed here
# let's print the first 5 lines
print("First 5 lines of the file:")
# we are learning a new way of looping using range()
# actually not very Pythonic but common in other languages
for i in range(5):  # loop from 0 to 4
    print(f"Range value i: {i}")  # show the current value of i
    print(f"Line {i+1}: ", end='')  # i+1 to show line numbers starting at 1    
    print(lines[i].rstrip())  # rstrip to remove trailing newline characters
    # if I did not remove newline characters the print would add an extra blank line

# let's do some string processing with our lines
# first to remember in string processing is that Python strings are immutable
# this means that we do not change them
# instead we create a new string based on the old one

# so let's go through first 5 lines and create new strings by uppercasing them
# after stripping whitespace
processed_lines = []  # create an empty list to hold processed lines
# let's go through slice of first 5 lines
for line in lines[:5]:  # lines[:5] gives us the first 5
    new_line = line.strip().upper()  # strip whitespace and uppercase
    # similarly I could use lower() to lowercase
    # let's check the length of new line and only add lines containing text
    if len(new_line) > 0:  # only add non-empty lines
        processed_lines.append(new_line)  # add the new line to our list

# let's see the processed lines
print(f"Have Processed {len(processed_lines)} lines (stripped and uppercased):")
for pline in processed_lines: # again pline could be any variable name
    print(pline)

# let's get the last line in processed lines
if len(processed_lines) > 0:
    last_line = processed_lines[-1]  # last line using negative index -1
    print(f"Last processed line: {last_line}")
else:
    print("No processed lines available. Stopping here.")
    # exit if needed
    exit()

# let's replace all double , with single , in the last line
# modified_line = last_line.replace(",,", ",")  # replace double
# we saw from above approach that we are left from 4 commas to 2
# how about looping while we have no double commas left?
# we use a while loop
# while loops keep going while the condition is true
modified_line = last_line  # start with last_line, we need this to start
while ",," in modified_line:
    modified_line = modified_line.replace(",,", ",")

# let's split our last line into words
words = modified_line.split()  # split on whitespace by default
# so split essentially tokenizes the string into words
# split takes a string and returns a list of words after splitting
print(f"Last line split into words ({len(words)} words):")
for word in words:
    print(word)

# so we have a number of lists already
# let's print types of our variables
print(f"Type of lines variable: {type(lines)}")  # should be list
print(f"Type of processed_lines variable: {type(processed_lines)}")  # should be list
print(f"Type of words variable: {type(words)}")  # should be list

# have to rememer that Python is dynamically typed so type COULD change
# generaly we try to avoid changing types of variables in code
# but it is possible to do so
print(f"Type of file_contents variable: {type(file_contents)}")  # should be str
print(f"Type of last_line variable: {type(last_line)}")  # should be str
print(f"Type of modified_line variable: {type(modified_line)}")  # should be str

# how about file_to_read ?
print(f"Type of file_to_read variable: {type(file_to_read)}")  # should be Path
# Path is a special type from pathlib module representing file paths

# so generaly syntax for for loop is
# for variable in iterable:
#    # do something with variable
#    # do more stuff with that particular item - variable

# iterable could be string, list, range and many other types (not int, not float)
# so pretty much anything that can be thought of as collection of items can be loope through with for loop


# so branching with if else is
# if condition:
#    # do something if condition is true
# else:
#    # do something else if condition is false

# we could do more with if elif else
# if condition1:
#    # do something if condition1 is true
# elif condition2:
#    # do something else if condition2 is true
# else:
#    # do something else if none of the conditions are true

# let's see an example of if elif else
number_of_words = len(words)
# we will run only 1 out of 4 branches here
if number_of_words == 0:
    print("No words found in the last line.")
    print("Please check the file contents.")
elif number_of_words < 10: # the order of elif matters!!
    print("Less than 10 words found in the last line.")
    print(f"Actual number of words: {number_of_words}")
elif number_of_words < 50:
    print("Less than 50 words found in the last line.")
else: # as Sherlock Holmes said if impossible is eliminated whatever remains however improbable must be the truth
    print("50 or more words found in the last line.")


# small read, filter, write example
# let's read the file again and write back only lines which contain word the somewhere
# so here we will open up a new file for writing
# we want our current file to be in the same folder as our read file
output_file_path = file_to_read.parent / "filtered_results.txt"
# i chose the name not to interfere with our original rglob search
print(f"Will write filtered lines to: {output_file_path}")

# so we will open two files at once
with open(file_to_read, mode='r', encoding='utf-8') as read_stream:
     print(f"Opened file for reading: {file_to_read}")
     # mode =w means write mode it WILL OVERWRITE existing file or create new one
     with open(output_file_path, mode='w', encoding='utf-8') as write_stream:
        # note the \ at the end of the first line to continue to next line
        # we have read_stream and write_stream variables for the two files
        for line in read_stream:  # read line by line
            # above approach works even on huuge files even on 1TB text files
            # next we add some sort logic for our filter
            # you could replace the logic in next line 
            # with whatever your needs for filtering are
            if "the" in line.lower():  # check if 'the' is in the line (case insensitive)
                write_stream.write(line)  # write the line to output file

# both files are automatically closed here
print(f"Filtered lines written to: {output_file_path}")


# let's append a current datetime to our output file
from datetime import datetime # i am important standard libray module
# this particular module provides date and time services
current_datetime = datetime.now()  # get current date and time
# a stands for append mode - it appends at the END
with open(output_file_path, mode='a', encoding='utf-8') as append_stream:
    append_stream.write(f"\n# File processed on {current_datetime.isoformat()}\n")

# NOTE: you can only append at the end of the file with append mode
# if you need to add to beginning or middle of file
# you have to read the entire file, modify contents and write back

# end of script

# so exercise for students would be to clean the messy file some more

# look for extra !! and other bad symbols and get rid of those
# then write back into new file