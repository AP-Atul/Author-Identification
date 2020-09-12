import os
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


# saving the data frame
df = pd.DataFrame(X)
df.to_csv("author_identification_article_splits.csv", index=False, header=False)
