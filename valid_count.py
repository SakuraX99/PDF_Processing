import csv
import time
import os


count = 0
for root, dirs, files in os.walk("/usr2/home/pliu3/PDF_Processing"):

    for dir in dirs:
       print(dir)