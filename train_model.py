import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score
import joblib

# Load dataset
df = pd.read_csv("water_potability.csv")

# Check null values
print(df.isnull().sum())

# Handle missing values
imputer = SimpleImputer(strategy="mean")
X = df.drop("Potability", axis=1)
y = df["Potability"]

X = imputer.fit_transform(X)

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Save model
joblib.dump(model, "model.pkl")
