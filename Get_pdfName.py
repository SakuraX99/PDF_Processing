import os


# with open('pdf_process.txt', 'r', encoding='UTF-8') as f:
#     line = f.readline()
#     idx = 0
#     while line:
#         idx+=1
#         # print(line,end="")
#         fix = idx//500 + 1
#         with open('pdf_process' + "_" + str(fix) + ".sh", 'a+', encoding='UTF-8') as f1:
#             f1.write(line)
#         line = f.readline()

with open('pdf_process_set.sh', 'w', encoding='UTF-8') as f:
    for i in range(89):
        f.write("chmod +x " + "./pdf_process_" + str(i+1) + ".sh" + "\n")
    for i in range(89):
        f.write("nohup " + "./pdf_process_" + str(i+1) + ".sh " + " > log" + str(i+1) + ".file" + " 2>&1 &" + "\n")