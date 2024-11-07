# -*- coding: utf-8 -*-
"""salesPredictionAnalysis

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1iivFOs7aKgHoSjWE8NfK7KeYv74Y1c_n
"""

import pandas as pd
df = pd.read_csv('/content/advertisingsales.task.zip')

df.head()
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

advertising_data = pd.read_csv('advertisingsales.task.zip')
X = advertising_data[['TV', 'Radio', 'Newspaper']]
y = advertising_data['Sales']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error (MSE): {mse}")
print(f"R-squared (R²): {r2}")
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, color='blue')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', lw=2)
plt.title('Actual vs Predicted Sales')
plt.xlabel('Actual Sales')
plt.ylabel('Predicted Sales')
plt.grid(True)
plt.show()