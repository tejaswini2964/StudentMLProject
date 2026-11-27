# 🎓 Student Performance Predictor

A Machine Learning web application that predicts students' Mathematics scores based on demographic information, parental education, lunch type, test preparation, and academic performance in reading and writing.

The project uses Python and Scikit-learn to build a regression model and Streamlit to provide an interactive user interface for real-time predictions.

## 🚀 Live Demo

**Try the application here:**

[Student Performance Predictor – Live Application](https://student-performance-predictor12.streamlit.app/)

## 📌 Project Overview

The objective of this project is to develop a Machine Learning model that identifies patterns in student-related data and predicts Mathematics scores based on selected student attributes.

Users can enter student details through an interactive web interface and receive an estimated Mathematics score.

## ✨ Features

- Predicts Mathematics scores using Machine Learning.
- Interactive web interface built with Streamlit.
- Handles numerical and categorical input features.
- Includes data preprocessing and feature transformation.
- Uses regression algorithms for model training and evaluation.
- Deployed online for public access.

## 📂 Dataset Information

The project uses a Student Performance dataset containing demographic, educational, and academic attributes.

**Input Features:**
- Gender
- Race / Ethnicity
- Parental Level of Education
- Lunch Type
- Test Preparation Course
- Reading Score
- Writing Score

**Target Variable:**
- Mathematics Score (`math_score`)

## ⚙️ Machine Learning Workflow

1. **Data Ingestion:** Load the student dataset and split it into training and testing sets.
2. **Data Preprocessing:** Handle numerical and categorical features using appropriate transformations.
3. **Feature Transformation:** Apply preprocessing pipelines to prepare the input data.
4. **Model Training:** Train and evaluate regression models.
5. **Model Evaluation:** Compare model performance using the R² score.
6. **Prediction Pipeline:** Load the trained model and preprocessor to generate predictions.
7. **Deployment:** Deploy the prediction application using Streamlit Community Cloud.

## 📊 Model Performance

| Metric | Result |
|---|---:|
| R² Score | 0.8804 |
| Model Type | Regression |
| Target Variable | Mathematics Score |

The selected regression model achieved an R² score of approximately **88.04%** on the test dataset.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Pandas | Data manipulation |
| NumPy | Numerical operations |
| Scikit-learn | Preprocessing and machine learning |
| CatBoost | Regression algorithm |
| XGBoost | Regression algorithm |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| Streamlit | Web application and deployment |
| Git & GitHub | Version control and project hosting |

## 📁 Project Structure

```text
StudentMLProject/
│
├── artifacts/
│   ├── data.csv
│   ├── train.csv
│   ├── test.csv
│   ├── model.pkl
│   └── preprocessor.pkl
│
├── notebook/
│   └── data/
│       └── stud.csv
│
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   │
│   ├── pipeline/
│   │   ├── predict_pipeline.py
│   │   └── train_pipeline.py
│   │
│   ├── exception.py
│   ├── logger.py
│   └── utils.py
│
├── templates/
│   ├── home.html
│   └── index.html
│
├── app.py
├── streamlit_app.py
├── requirements.txt
├── setup.py
├── README.md
└── .gitignore
```

## 💻 Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/tejaswini2964/StudentMLProject.git
```

### 2. Navigate to the project directory

```bash
cd StudentMLProject
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Streamlit application

```bash
streamlit run streamlit_app.py
```

The application will be available locally at:

`http://localhost:8501`

## 🌐 Deployment

The application is deployed using **Streamlit Community Cloud** and connected to the GitHub repository for source code management.

**Live URL:** https://student-performance-predictor12.streamlit.app/

## 🎯 Learning Outcomes

Through this project, I gained practical experience in:

- Building an end-to-end Machine Learning project.
- Data ingestion and preprocessing.
- Working with numerical and categorical features.
- Training and evaluating regression models.
- Creating reusable prediction pipelines.
- Developing interactive ML applications using Streamlit.
- Deploying Machine Learning applications to the cloud.

## 👩‍💻 Author

**Guluguluri Tejaswini**

GitHub: [tejaswini2964](https://github.com/tejaswini2964)

---

