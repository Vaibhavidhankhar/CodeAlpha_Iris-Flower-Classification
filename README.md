# 🌸 CodeAlpha: Iris Flower Classification

[![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3.2-orange?logo=flask)](https://flask.palletsprojects.com/)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-black?logo=github)](https://github.com/Vaibhavidhankhar/CodeAlpha_Iris-Flower-Classification.git)
[![Render](https://img.shields.io/badge/Render-Live%20App-brightgreen?logo=render)](https://the-iris-oracle.onrender.com)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3.0-lightgrey?logo=scikit-learn)](https://scikit-learn.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.1.1-lightblue?logo=pandas)](https://pandas.pydata.org/)
[![Joblib](https://img.shields.io/badge/Joblib-1.3.2-blueviolet)](https://joblib.readthedocs.io/)
[![HTML5](https://img.shields.io/badge/HTML5-orange?logo=html5)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-blue?logo=css3)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-yellow?logo=javascript)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)


Welcome to **CodeAlpha: Iris Flower Classification**, a complete machine learning project that predicts the species of an Iris flower (Setosa, Versicolor, or Virginica) using four key features — sepal length, sepal width, petal length, and petal width. This project covers the full ML workflow, from dataset exploration to model deployment.

🔗 **Live Sites & Links:**  
- GitHub Repository: [CodeAlpha Iris Flower Classification](https://github.com/Vaibhavidhankhar/CodeAlpha_Iris-Flower-Classification.git)  
- GitHub Pages (Project Showcase & Info): [Project Site](https://vaibhavidhankhar.github.io/CodeAlpha_Iris-Flower-Classification/)  
- Try the Live Predictor: [Iris Classifier](https://the-iris-oracle.onrender.com)
- Colab Notebook with Model (PROJECT_IrisFlowerClassification.ipynb): [Open in Colab](https://colab.research.google.com/github/Vaibhavidhankhar/CodeAlpha_Iris-Flower-Classification/blob/main/PROJECT_IrisFlowerClassification.ipynb)  
- Alternate Colab Notebook (CodeAlpha_IrisFlowerClassification.ipynb):[Open in Colab](https://colab.research.google.com/github/Vaibhavidhankhar/CodeAlpha_Iris-Flower-Classification/blob/main/CodeAlpha_IrisFlowerClassification.ipynb)

---

## 🌸 About the Iris Flower
Iris, derived from the Greek word for "rainbow", is a diverse genus of flowering plants. 
# Key characteristics include:
- Growth: Rhizomatous or bulbous
- Leaves: Sword-shaped or narrow
- Flowers: Six-lobed; outer sepals "falls", inner petals "standards"
- Colors: Wide range of rainbow hues
- Types: Bearded, Beardless, Bulbous, Yellow Flag, Blue Flag, and more

---

## 🌟 About the Project

This project demonstrates a **complete ML workflow**, including:

1. **Data Exploration & Analysis** – Understanding patterns in the dataset.  
2. **Data Preprocessing** – Scaling, encoding, and preparing data for modeling.  
3. **Model Building** – Training a classifier on the classic Iris dataset.  
4. **Evaluation & Testing** – Validating model accuracy and performance.  
5. **Deployment** – Making the model accessible online via Render.

It also educates users about the **Iris dataset** and key characteristics of Iris flowers.

---

## 🎬 Live Demo / GIF

![Demo GIF](walkthrough.gif)  

Click the "Try the Iris Classifier 🌿" button below on the project page to access the live ML predictor:

[Try the Iris Classifier 🌿](https://the-iris-oracle.onrender.com)

The application provides:

- Interactive input fields for sepal and petal measurements.  
- Instant prediction of the species with probabilities.  
- Clean, aesthetic interface inspired by a starry galaxy theme.  

---

## 🔗 Project Structure & Files

## 🌿 Project Structure

```text
🌿 CodeAlpha_Iris-Flower-Classification/
├── 🌼 IrisWebApp/
│   ├── 📝 app.py             # Main Flask application
│   ├── 💾 iris_model.pkl     # Trained ML model
│   ├── ⚖️ scaler.pkl         # Scaler for input features
│   ├── 🔤 label_encoder.pkl  # Label encoder for species
│   ├── 📄 templates/         # HTML pages for Flask
│   └── 🎨 static/            # CSS, JS, images, and assets
├── 🐍 venv/                  # Virtual environment for Python dependencies
├── 📦 requirements.txt       # Required Python packages
├── 🚀 Procfile               # For Render deployment
└── 📖 README.md              # Project documentation
```

---

## 🛠 Tools & Technologies Used

- **Programming Language:** Python 3.13  
- **Web Framework:** Flask  
- **Machine Learning Libraries:** scikit-learn, pandas, joblib  
- **Frontend:** HTML, CSS, JavaScript, Google Fonts  
- **Deployment:** Render & GitHub Pages  
- **Development Environment:** Bash & VSCode / Terminal  

---

## 🧰 How It Works

1. Users provide flower attributes: sepal length, sepal width, petal length, petal width.  
2. Inputs are **scaled** using the trained scaler (`scaler.pkl`).  
3. The **ML model** (`iris_model.pkl`) predicts the flower species.  
4. The **label encoder** (`label_encoder.pkl`) converts numeric predictions into species names.  
5. The prediction is displayed instantly on the web interface.  

---

## 📂 Dataset

- **Dataset:** Classic Iris dataset with 150 samples, evenly divided among three species.  
- **Features:** Sepal length, sepal width, petal length, petal width.  
- **Target:** Species (Setosa, Versicolor, Virginica)  
- **Source:** [Kaggle Iris Dataset](https://www.kaggle.com/datasets/saurabh00007/iriscsv?select=Iris.csv)  

---

## 🛠 Setup Instructions (Local Run)

1. **Clone the repository:**  
```bash
git clone https://github.com/Vaibhavidhankhar/CodeAlpha_Iris-Flower-Classification.git
cd CodeAlpha_Iris-Flower-Classification/IrisWebApp
```
2. **Create a virtual environment and activate it:**
```bash
python3 -m venv venv
source venv/bin/activate
```
3. **Install dependencies:**
```bash
pip install -r requirements.txt
```
4. **Run the Flask application locally:**
```bash
python app.py
```
5. **Open in browser:**
```bash
http://127.0.0.1:5000
```

---

## 📬 Contact & Connect
- Author: Vaibhavi Dhankhar
- Email: bhavi7677@gmail.com
- GitHub: Vaibhavi Dhankhar [CodeAlpha Iris Flower Classification](https://github.com/Vaibhavidhankhar/CodeAlpha_Iris-Flower-Classification.git)
- Project Page: GitHub Pages Site [Project Site](https://vaibhavidhankhar.github.io/CodeAlpha_Iris-Flower-Classification/)

---

## 💡 Notes
- The live predictor uses the trained model, scaler, and label encoder stored in .pkl files.
- Works on both desktop and mobile browsers.
- Starry-galaxy theme and responsive design make the interface visually appealing.
- Badges, GIFs/screenshots, and live links make this README an interactive project showcase.
