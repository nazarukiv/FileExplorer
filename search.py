import os, shutil

def search():
    #if you select disk C, it will search trough disk until it locates the desired file, assuming it exists
    for adress, dirs, files in os.walk(input("Write down road of start \n")):
        for file in files:
            if file.endswith('.txt'):  # we can add any criteria to this with use of and.
                yield os.path.join(adress, file)




for i in search():
    print(i)