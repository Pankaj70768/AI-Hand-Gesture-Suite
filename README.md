![GitHub stars](https://img.shields.io/github/stars/Pankaj70768/AI-Hand-Gesture-Suite?style=for-the-badge)

![GitHub forks](https://img.shields.io/github/forks/Pankaj70768/AI-Hand-Gesture-Suite?style=for-the-badge)

![GitHub last commit](https://img.shields.io/github/last-commit/Pankaj70768/AI-Hand-Gesture-Suite?style=for-the-badge)

![Repo Size](https://img.shields.io/github/repo-size/Pankaj70768/AI-Hand-Gesture-Suite?style=for-the-badge)

<h1 align="center">🤖 AI Hand Gesture Suite</h1>

<p align="center">
Real-Time AI Powered Hand Gesture Recognition & Media Controller
</p>

<p align="center">

<img src="https://readme-typing-svg.demolab.com?font=Poppins&size=28&duration=3500&pause=1000&color=00BFFF&center=true&vCenter=true&width=900&lines=AI+Hand+Gesture+Recognition;MediaPipe+%2B+Machine+Learning;Random+Forest+Accuracy+99.58%25;Real-Time+Media+Controller;Built+with+Python+%7C+OpenCV+%7C+Scikit-Learn" />

</p>

---

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)

![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green?style=for-the-badge&logo=opencv)

![MediaPipe](https://img.shields.io/badge/MediaPipe-Hand%20Tracking-orange?style=for-the-badge)

![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-red?style=for-the-badge&logo=scikitlearn)

![Random Forest](https://img.shields.io/badge/Accuracy-99.58%25-success?style=for-the-badge)

![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

</p>

---

# 📖 About

AI Hand Gesture Suite is a real-time gesture recognition system that detects hand gestures using **MediaPipe** and classifies them using a **Machine Learning (Random Forest)** model.

The recognized gestures are mapped to media controls such as:

- ▶ Play / Pause
- 🔊 Volume Up
- 🔉 Volume Down
- ⏭ Next Track
- ⏮ Previous Track
- 🔇 Mute

The project also includes a custom dataset collector, ML model training pipeline, live prediction module, and performance evaluation.

---

# 🎥 Live Demo

<p align="center">
<img src="results/screenshots/live_prediction.png" width="900">
</p>

---

# ✨ Features

- 📷 Real-Time Webcam Detection
- ✋ Hand Landmark Detection using MediaPipe
- 🤖 Machine Learning Gesture Recognition
- 📊 Automatic Dataset Collection
- 🌲 Random Forest Classifier
- 📈 Model Comparison (RF / SVM / KNN)
- 📉 Confusion Matrix
- ⚡ Fast Real-Time Prediction
- 🎵 Gesture Controlled Media Player

---

# 🎮 Supported Gestures

| Gesture | Action |
|---------|---------|
| ✋ Open Palm | Play / Pause |
| 👍 Thumb Up | Volume Up |
| 👎 Thumb Down | Volume Down |
| ✌ Peace | Next Track |
| ✊ Fist | Previous Track |
| 👌 OK | Mute |

---

# 📂 Project Structure

```text
AI-Hand-Gesture-Suite
│
├── assets
├── controllers
├── core
├── dataset
├── logs
├── models
├── results
│   ├── screenshots
│   ├── demo
│   └── graphs
├── tests
├── trained_models
├── ui
├── utils
│
├── compare_models.py
├── train_model.py
├── main.py
└── README.md
```

---

# ⚙️ Installation

```bash
git clone https://github.com/Pankaj70768/AI-Hand-Gesture-Suite.git

cd AI-Hand-Gesture-Suite

pip install -r requirements.txt
```

Train Model

```bash
python train_model.py
```

Run

```bash
python main.py
```

---

# 🧠 Machine Learning Pipeline

```text
Dataset Collection
        │
        ▼
Feature Extraction
        │
        ▼
Data Preprocessing
        │
        ▼
Random Forest Training
        │
        ▼
Model Evaluation
        │
        ▼
Real-Time Gesture Prediction
        │
        ▼
Media Controller
```

---

# 📊 Model Comparison

| Model | Accuracy |
|-------|----------|
| 🌲 Random Forest | **99.58%** |
| 🔷 KNN | **99.16%** |
| ⚪ SVM | **97.90%** |

🏆 **Best Model:** Random Forest

<p align="center">
<img src="results/screenshots/model_comparison.png" width="800">
</p>

---

# 📉 Confusion Matrix

<p align="center">
<img src="results/screenshots/confusion_matrix.png" width="800">
</p>

---

# 📸 Dataset Collection

<p align="center">
<img src="results/screenshots/dataset_collection.png" width="800">
</p>

---

# 🎵 Media Control Demo

<p align="center">
<img src="results/screenshots/media_control.png" width="800">
</p>

---

# 🚀 Future Improvements

- 🖱 Virtual Mouse
- ⌨ Virtual Keyboard
- 💡 Brightness Control
- 🎤 Voice Commands
- 📊 Custom Gesture Training
- 📱 Smart Home Automation

---

# 🛠 Tech Stack

- Python
- OpenCV
- MediaPipe
- NumPy
- Pandas
- Scikit-Learn
- Matplotlib
- Joblib

---

# 👨‍💻 Author

**Pankaj**

B.Tech CSE (AI & ML)

GitHub → https://github.com/Pankaj70768

---

<p align="center">

### ⭐ If you found this project useful, please give it a Star ⭐

</p>
