import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import accuracy_score

from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay

dataset = pd.read_csv(
    "dataset/landmarks/gesture_dataset.csv"
)

X = dataset.iloc[:, :-1]

y = dataset.iloc[:, -1]

encoder = LabelEncoder()

y = encoder.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y,
)

models = {

    "Random Forest":
    RandomForestClassifier(
        n_estimators=200,
        random_state=42,
    ),

    "SVM":
    SVC(),

    "KNN":
    KNeighborsClassifier(
        n_neighbors=5
    )

}

accuracies = {}

print("=" * 50)
print("MODEL COMPARISON")
print("=" * 50)

for name, model in models.items():

    print(f"\nTraining {name}...")

    model.fit(
        X_train,
        y_train,
    )

    prediction = model.predict(
        X_test
    )

    accuracy = accuracy_score(
        y_test,
        prediction,
    )

    accuracies[name] = accuracy * 100

    print(
        f"{name} Accuracy : {accuracy*100:.2f}%"
    )

print("\n" + "=" * 50)
print("FINAL RESULT")
print("=" * 50)

best_model = max(
    accuracies,
    key=accuracies.get
)

for model_name, score in accuracies.items():

    print(
        f"{model_name:15} : {score:.2f}%"
    )

print("\nBest Model :", best_model)

plt.figure(figsize=(8,5))

plt.bar(
    accuracies.keys(),
    accuracies.values()
)

plt.title(
    "Gesture Recognition Model Comparison"
)

plt.xlabel(
    "Models"
)

plt.ylabel(
    "Accuracy (%)"
)

plt.ylim(0,100)

for i, value in enumerate(
    accuracies.values()
):

    plt.text(
        i,
        value + 1,
        f"{value:.2f}%",
        ha="center",
    )

plt.tight_layout()

plt.savefig(
    "trained_models/model_comparison.png"
)

plt.show()

print("\nGenerating Confusion Matrix...")

best_model = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
)

best_model.fit(
    X_train,
    y_train,
)

prediction = best_model.predict(
    X_test
)

cm = confusion_matrix(
    y_test,
    prediction,
)

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=encoder.classes_,
)

disp.plot(
    cmap="Blues",
    values_format="d",
)

plt.title(
    "Random Forest Confusion Matrix"
)

plt.tight_layout()

plt.savefig(
    "trained_models/confusion_matrix.png"
)

plt.show()

print("Confusion Matrix Saved!")

