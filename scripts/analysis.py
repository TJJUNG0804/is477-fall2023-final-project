import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


df = pd.read_csv('data/wine.data', header=None)

columns = [
    "Class", "Alcohol", "Malic acid", "Ash", "Alcalinity of ash", "Magnesium",
    "Total phenols", "Flavanoids", "Nonflavanoid phenols", "Proanthocyanins",
    "Color intensity", "Hue", "OD280/OD315 of diluted wines", "Proline"
]
df.columns = columns

summary_stats = df.describe()
summary_stats.to_csv('results/summary_statistics.csv')

X = df.drop('Class', axis=1)
y = df['Class']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Use a Random Forest Classifier for the task
rfc = RandomForestClassifier(n_estimators=100, random_state=42)
rfc.fit(X_train, y_train)
y_pred = rfc.predict(X_test)

# Compute accuracy
accuracy = accuracy_score(y_test, y_pred)
with open('results/classification_accuracy.txt', 'w') as f:
    f.write(f'Classification Accuracy: {accuracy}')

# Histogram of the 'Alcohol' feature
plt.figure(figsize=(10, 6))
df['Alcohol'].hist(bins=15)
plt.title('Distribution of Alcohol Content')
plt.xlabel('Alcohol')
plt.ylabel('Frequency')
plt.savefig('results/alcohol_distribution.png')