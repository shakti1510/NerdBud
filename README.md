# 🤓 NerdBud – AI Powered Personalized Learning Platform

NerdBud is an AI-driven personalized learning system designed to adapt programming education based on learner performance.  
It combines interactive quizzes, rule-based logic, and machine learning to decide whether a learner should **revise** or **advance**.

The project demonstrates an end-to-end AI system: data collection, feature engineering, model training, inference, UI, and deployment.

---

## 🚀 Features

- Interactive programming quizzes (Python – Beginner level)
- Tracks learner accuracy, response time, and attempts
- Rule-based + Machine Learning decision system
- Personalized feedback after every quiz
- User progress persistence across sessions
- Visual dashboard with charts and accuracy gauge
- Streamlit-based web interface
- Deployable on Hugging Face Spaces

---

## 🧠 System Architecture

```

User (Streamlit UI)
↓
Quiz Engine
↓
Performance Metrics
↓
Rule-Based AI
↓
Machine Learning Model
↓
Feedback & Recommendation
↓
User Progress Storage

```

---

## 🛠 Tech Stack

- **Language:** Python
- **Frontend:** Streamlit
- **Machine Learning:** Scikit-learn (Logistic Regression)
- **Data Handling:** Pandas, NumPy
- **Visualization:** Plotly, Matplotlib
- **Model Persistence:** Joblib
- **Deployment:** Hugging Face Spaces

---

## 📁 Project Structure

```

nerdbud/
├── app/
│   ├── streamlit_app.py
│   ├── quiz_engine.py
│   ├── ai_engine.py
│   └── utils.py
│
├── notebooks/
│   ├── 02_QuizEngine.ipynb
│   ├── 03_ProgressTracking.ipynb
│   ├── 04_RuleBasedAI.ipynb
│   ├── 05_DatasetBuilder.ipynb
│   ├── 06_ModelTraining.ipynb
│   ├── 07_Evaluation.ipynb
│   └── 08_NerdBud_UI.ipynb
│
├── data/
│   ├── quizzes/
│   │   └── python_basics.json
│   └── user_progress/
│
├── models/
│   └── nerdbud_model.pkl
│
├── requirements.txt
├── README.md
└── .gitignore

````

---

## 📥 How to Download the Project

```bash
git clone https://github.com/<your-username>/NerdBud.git
cd NerdBud
````

---

## 🧪 Setup Instructions (Local)

### 1️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run the Application

### 1. Run Streamlit App

```bash
streamlit run app/streamlit_app.py
```

After running the command, open the browser link shown in the terminal.

### 2. Run in Jupyter Notebook
```bash
Open 08_NerdBud_UI..ipynb Run all the cells. after Running the last cell, following the below provided steps
```


---

## 🧑‍🎓 How to Use NerdBud

1. Enter a **username**
2. Click **Start NerdBud**
3. Start the quiz
4. Answer all questions
5. View:

   * Accuracy (circular gauge)
   * Average response time
   * Number of attempts
   * Topic-wise performance
   * AI recommendation (Advance / Revise)
6. User progress is automatically saved

---

## 🤖 AI Decision Logic

* **Rule-Based AI:** Uses predefined thresholds on accuracy and response time
* **Machine Learning Model:** Logistic Regression trained on learner performance data
* **Features Used:** accuracy, avg_time, attempts
* Final recommendation is based on ML prediction

---

## 🌍 Deployment

NerdBud can be deployed on **Hugging Face Spaces** using Streamlit.
The trained model is included in the repository for runtime inference.

---

## 🔮 Future Enhancements

* Support for multiple programming languages
* Adaptive quiz difficulty
* Database-backed persistence
* Advanced ML models
* Authentication system

---

## 📜 License

This project is open-source and available under the MIT License.
