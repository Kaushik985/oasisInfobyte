# -*- coding: utf-8 -*-
"""irisFlowerClassification

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1V6GxIe67gWIPhtRYzRY-JIpOpeJKjh2A
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

iris_df = pd.read_csv('/content/irisflowers.zip')
iris_df = iris_df.drop(columns=["Id"])

X = iris_df.drop("Species", axis=1)
y = iris_df["Species"]

label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size = 0.3, random_state = 42)

model = RandomForestClassifier(random_state = 42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
finalReport = classification_report(y_test, y_pred, target_names=label_encoder.classes_)

print("Model Accuracy:", accuracy)
print("\nClassification Report:\n", finalReport)