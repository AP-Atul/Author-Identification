# Author-Identification
This is an implementation of the paper
- [Author Identification using Sequential Minimal Optimization with rule-based Decision Tree on Indian Literature in Marathi](https://doi.org/10.1016/j.procs.2018.05.024)

- [Download the dataset](http://tdil-dc.in/index.php?option=com_download&task=showresourceDetails&toolid=2007&lang=en)

## Stats
### 1. Information about the .csv file

I have provided a pre processed csv file using the `preprocess.py` and `dataFrameGen.py`. Also the vector for text is generated using the `vectorizer.py` which uses features of the articles. (without using NLTK)

 original dataset contained: 
  - Total lines in articles :: 10405
  - Total words in articles :: 358695
  - Total characters in articles :: 1889183
  - Total no of unique words :: 73889

### 2. Features selected
  - line count 
  - char count 
  - word count 
  - average word size 
  - vowels per word 
  - consonants per word 
  - matras per word 
  - count of words of fize size 
  - count of words below size 
  - count of words above size 

### 3. Model stats

| Sr. No. | Classifier | Accuracy |
| --- | --- | --- |
| 1 | Naive Bayes (Guassian) | 89 % |
| 2 | SVC | 70 % |
| 3 | Decision Tree  | 99 % |
| 4 | K Nearest Neighbour | 98.8 % |
