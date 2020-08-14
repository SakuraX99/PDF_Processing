

# for i in range(112):
#     Str = "nohup python3 -u Crawler_Parameter.py " + str(i*500) + " 500 > Crawler_" + str(i*500) +"_500.log 2>&1 &"
#     print(Str)
import csv
import os
filename = 'pdf_process.txt'
root_path = os.getcwd()
with open(filename, 'w') as file_object:
    with open('PDF_Name.csv', 'r', encoding='UTF-8') as f:
        reader = csv.reader(f)
        idx = 0

        for row in reader:
            idx+=1
            if idx>1:
                validation = row[1]
                if validation!="None":
                    command = "java -Xmx6g -jar science-parse-cli-assembly-3.0.1.jar " + row[2] + ''' "$1" ''' + "-f " + "./" + row[3] + "/" + row[0] + "_parse.json"
                    file_object.write(command + "\n")

