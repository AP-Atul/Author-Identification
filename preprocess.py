import os

dirs = ["./storage/Comedy Articles 5 authors",
        "./storage/Mixed Articles 10 Authors"]

# get stats
lineCount = 0
wordCount = 0
charCount = 0
wordDict = dict()
for directory in dirs:
    files = os.listdir(directory)
    for file in files:
        with open(os.path.join(directory, file), "r") as f:
            lines = f.readlines()
            for line in lines:
                lineCount += 1
                words = line.split(" ")
                wordCount += len(words)
                for word in words:
                    if wordDict.__contains__(word):
                        wordDict[word] += 1
                    else:
                        wordDict[word] = 1
                    for char in word:
                        charCount += 1


print(f"Total lines in articles :: {lineCount}")
print(f"Total words in articles :: {wordCount}")
print(f"Total characters in articles :: {charCount}")
print(f"Total no of unique words :: {len(wordDict)}")

# create stop words
wordDict = {key: value for key, value in sorted(wordDict.items(), key=lambda item: item[1], reverse=True)}
count = 0
LIMIT = 50
stopWords = []
for key, value in wordDict.items():
    # print(f"{key} ----->  {value}")
    stopWords.append(key)
    count += 1
    if count == LIMIT:
        break

# removing stop words and stems
stems = []
with open("./stemmers.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        line = line.replace("\n", "")
        line = line.replace(" ", "")
        stems.append(line)

outputDir = "./storage/output"
if not os.path.isdir(outputDir):
    os.mkdir(outputDir)

# remove stop words and stemming
for directory in dirs:
    files = os.listdir(directory)
    for file in files:
        with open(os.path.join(directory, file), "r") as f:
            lines = f.readlines()
            outputLines = []
            for line in lines:
                words = line.split(" ")
                for word in words:
                    if word in stopWords:
                        line = line.replace(word + " ", "")

                    for stem in stems:
                        if word.__contains__(stem):
                            line = line.replace(stem, "")
                            break

                outputLines.append(line)
        with open(os.path.join(outputDir, file), "w") as output:
            for line in outputLines:
                output.write(line)
        # print(f"{file} written to the output folder")

# recalculating the stats
dirs = ["./storage/output"]

cleanLineCount = 0
cleanWordCount = 0
cleanCharCount = 0
cleanWordDict = dict()
for directory in dirs:
    files = os.listdir(directory)
    for file in files:
        with open(os.path.join(directory, file), "r") as f:
            lines = f.readlines()
            for line in lines:
                cleanLineCount += 1
                words = line.split(" ")
                cleanWordCount += len(words)
                for word in words:
                    if cleanWordDict.__contains__(word):
                        cleanWordDict[word] += 1
                    else:
                        cleanWordDict[word] = 1
                    for char in word:
                        cleanCharCount += 1

print(f"Total cleaned lines in articles :: {cleanLineCount}")
print(f"Total cleaned words in articles :: {cleanWordCount}")
print(f"Total cleaned characters in articles :: {cleanCharCount}")
print(f"Total cleaned no of unique words :: {len(cleanWordDict)}")
print("\n")
print(f"Total discarded lines in articles :: {lineCount - cleanLineCount}")
print(f"Total discarded words in articles :: {wordCount - cleanWordCount}")
print(f"Total discarded characters in articles :: {charCount - cleanCharCount}")
print(f"Total discarded no of unique words :: {len(wordDict) - len(cleanWordDict)}")

# OUTPUT
# 100%|██████████| 2/2 [00:00<00:00,  2.52it/s]
# Total lines in articles :: 10405
# Total words in articles :: 358695
# Total characters in articles :: 1889183
# Total no of unique words :: 73889
# 100%|██████████| 2/2 [00:07<00:00,  3.61s/it]
# 100%|██████████| 1/1 [00:00<00:00,  1.70it/s]
# Total cleaned lines in articles :: 10405
# Total cleaned words in articles :: 287476
# Total cleaned characters in articles :: 1544412
# Total cleaned no of unique words :: 72975
#
#
# Total discarded lines in articles :: 0
# Total discarded words in articles :: 71219
# Total discarded characters in articles :: 344771
# Total discarded no of unique words :: 914
#
# Process finished with exit code 0

