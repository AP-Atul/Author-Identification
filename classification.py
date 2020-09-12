import pandas as pd
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

"""
Performing good old classifications 😀
Using sklearn no custom implementation here!
"""
df = pd.read_csv("author_identification_article_plits.csv", header=None)

X = df.iloc[:, 0:9]
y = df.iloc[:, -1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=500)

print(f"Training samples :: {len(X_train)}")
print(f"Testing samples :: {len(X_test)}")

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(f"Model accuracy :: {accuracy_score(y_test, y_pred)}")
print("Classification report")
print(classification_report(y_test, y_pred))

# *************** STATS *****************
# 1. Naive Bayes (Guassian) : 89 %
# 2. SVC : 70 %
# 3. Decision Tree  : 99 %
# 4. K Nearest Neighbour : 98.8 %
# **************************************
