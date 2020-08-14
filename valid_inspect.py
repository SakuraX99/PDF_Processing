import os
import csv

import pandas as pd

root_path = os.getcwd()

data = {"id": [],
            "validation": [],
            "pdfName": [],
            "directory": []
            }

with open('nlpedia-db.csv', 'r', encoding='UTF-8') as f:
    reader = csv.reader(f)
    idx = 0

    for row in reader:
        idx+=1
        if idx>1:
            data["id"].append(row[0])
            url0 = row[7]
            url = url0.split(" ")[0]
            if url != "None":
                dir = row[0] + "_" + row[1] + "_" + row[2] + "_Get"
                work_path = root_path+"/"+dir
                try:
                    if not os.listdir(work_path):
                        data["validation"].append("None")
                        dir = row[0] + "_" + row[1] + "_" + row[2] + "_None"
                        data["directory"].append(dir)
                        data["pdfName"].append("NaN")

                        dst = root_path + "/" + dir
                        os.rename(work_path, dst)
                    else:
                        dir = row[0] + "_" + row[1] + "_" + row[2] + "_Get"
                        data["validation"].append("Get")
                        data["pdfName"].append(os.listdir(root_path + "/" + dir)[0])
                        data["directory"].append(dir)
                except:
                    dir = row[0] + "_" + row[1] + "_" + row[2] + "_None"
                    work_path = root_path + "/" + dir
                    if not os.listdir(work_path):
                        data["validation"].append("None")
                        dir = row[0] + "_" + row[1] + "_" + row[2] + "_None"
                        data["directory"].append(dir)
                        data["pdfName"].append("NaN")

                        dst = root_path + "/" + dir
                        os.rename(work_path, dst)
                    else:
                        dir = row[0] + "_" + row[1] + "_" + row[2] + "_Get"
                        data["validation"].append("Get")
                        data["pdfName"].append(os.listdir(root_path + "/" + dir)[0])
                        data["directory"].append(dir)


            else:

                data["validation"].append("None")
                data["pdfName"].append("NaN")
                data["directory"].append(row[0] + "_" + row[1] + "_" + row[2] + "_None")
    df = pd.DataFrame(data, columns=["id", "validation", "pdfName", "directory"])
    df.to_csv("PDF_Name.csv", index=False, columns=["id", "validation", "pdfName", "directory"])

