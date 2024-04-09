import os, shutil

KEY_FOR_SEARCH = input('What do you want to find? \n')
PATH_FOR_COPY = input("Write down the place where files should be copied?\n")

def search():
    #if you select disk C, it will search trough disk until it locates the desired file, assuming it exists
    for adress, dirs, files in os.walk(input("Write down road of start \n")):
        for file in files:
            if file.endswith('.txt'):  # we can add any criteria to this with use of and.
                yield os.path.join(adress, file)

def read_from_pathtxt(path):
    with open(path) as r:
        for i in r:
            if KEY_FOR_SEARCH in i:
                return copy(path)

def copy(path):
    file_name = path.split('\\')[-1]

    shutil.copyfile(path, os.path.join(PATH_FOR_COPY, file_name))
    print('File was copied!', file_name)

for i in search():
    try:
        read_from_pathtxt(i)
    except Exception as e:
        with open(os.path.join(PATH_FOR_COPY,'error.txt'), 'a') as r:
            r.write(str(e) + '\n' + i + '\n')
