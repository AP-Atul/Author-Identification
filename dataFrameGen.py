import os
import numpy as np
import pandas as pd
from lib.vectorizer import Vectorizer


def partition(lst, n):
    return [lst[i:i + n] for i in range(0, len(lst), n)]


X = []
vectorizer = Vectorizer()

labelsDict = dict()
directory = "./storage/output"  # your dataset directory
labelCount = 0
for file in os.listdir(directory):
    with open(os.path.join(directory, file), "r") as f:
        # print(f"Processing file :: {file}")
        label = os.path.splitext(file)[0].replace(" Mixed Articles", "")  # getting labels using file names
        labelsDict[label] = labelCount
        labelCount += 1
        lines = partition(f.readlines(), 10)
        for line in lines:
            vector = vectorizer.transform(line)
            vector.append(labelCount)
            X.append(vector)

        print("|", label, "|", int(np.sum(vector[0])), "|", int(np.sum(vector[1])), "|",  int(np.sum(vector[2])), "|",  int(np.sum(vector[3])),
              "|",  int(np.sum(vector[4])), "|",  int(np.sum(vector[5])) ,"|",
              int(np.sum(vector[6])),"|",  int(np.sum(vector[7])),"|",  int(np.sum(vector[8])),"|",  int(np.sum(vector[9])),"|",
              int(np.sum(vector[10])), "|")

# saving the data frame
df = pd.DataFrame(X)
df.to_csv("author_identification_article_plits.csv", index=False, header=False)
