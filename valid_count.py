import csv
import time
import os


count = 0
with open("valid_inspect.txt", 'w', encoding='UTF-8') as f:
    for root, dirs, files in os.walk("/usr2/home/pliu3/PDF_Processing"):

        for dir in dirs:
            f.write(dir + " ")
            for root1, dirs1, files1 in os.walk(dir):
                for file in files1:
                    f.write(file + ":" + os.path.getsize(dir+"/"+file)+" ")
            f.write("\n")


