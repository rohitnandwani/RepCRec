from os import listdir, getcwd
from os.path import isfile, join
from subprocess import check_output



test_files_path = join(getcwd(), 'test')
test_files = [f for f in listdir(test_files_path) if isfile(join(test_files_path, f))]

for test_file in test_files:
    #test_file = open(join(test_files_path, test_file), 'r')
    #test_file_contents = test_file.read()
    process = check_output(['python', 'main.py', join(test_files_path, test_file)])
    print (process)


