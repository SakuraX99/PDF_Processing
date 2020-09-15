import csv
import time
import os

with open("valid_inspect.txt", 'w', encoding='UTF-8') as f:
    for root, dirs, files in os.walk("/usr2/home/pliu3/PDF_Processing"):
        for dir in dirs:
            if dir==".git":
                continue
            if dir == ".idea":
                continue
            f.write(dir + " ")
            for root1, dirs1, files1 in os.walk(dir):
                for file in files1:
                    f.write(file)
            f.write("\n")

##  + ":" + str(os.path.getsize("/usr2/home/pliu3/PDF_Processing/"+ dir+"/"+file))+" "