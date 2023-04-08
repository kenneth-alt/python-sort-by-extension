import random

extensions = ['.c', '.cpp', '.cs']  # list of file extensions
num_files = 100  # number of files to generate
filename_prefix = 'project_'  # prefix for filenames

with open('c_programs.txt', 'w') as file:
    for i in range(1, num_files+1):
        # generate filename with counter
        filename = f"{filename_prefix}{i:02}"
        # add random extension
        extension = random.choice(extensions)
        # write to file
        file.write(f"{filename}{extension}\n")

