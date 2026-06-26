import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report


# ==============================
# Load Dataset
# ==============================

DATASET_PATH = "dataset/landmarks/gesture_dataset.csv"

if not os.path.exists(DATASET_PATH):
    print("Dataset not found!")
    exit()

df = pd.read_csv(DATASET_PATH)

print("=" * 50)
print("Dataset Loaded Successfully")
print("=" * 50)

print(df.head())

# ==============================
# Features & Labels
# ==============================

X = df.iloc[:, :-1]
y = df.iloc[:, -1]

encoder = LabelEncoder()
y = encoder.fit_transform(y)

# ==============================
# Train Test Split
# ==============================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y,
)

# ==============================
# Random Forest
# ==============================

print("\nTraining Random Forest...\n")

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
)

model.fit(X_train, y_train)

# ==============================
# Prediction
# ==============================

predictions = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    predictions,
)

print("=" * 50)
print(f"Accuracy : {accuracy * 100:.2f}%")
print("=" * 50)

print("\nClassification Report\n")
print(
    classification_report(
        y_test,
        predictions,
        target_names=encoder.classes_,
    )
)

# ==============================
# Save Model
# ==============================

os.makedirs(
    "trained_models",
    exist_ok=True,
)

joblib.dump(
    model,
    "trained_models/gesture_model.pkl",
)

joblib.dump(
    encoder,
    "trained_models/label_encoder.pkl",
)

print("\nModel Saved Successfully!")

print("trained_models/gesture_model.pkl")
print("trained_models/label_encoder.pkl")