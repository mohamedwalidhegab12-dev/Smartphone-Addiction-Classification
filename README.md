<div align="center">

# 📱 Smartphone Addiction Classification

### AI-Powered Behavioral Risk Classification & Digital Wellbeing Dashboard

<br>

<p>
An end-to-end Machine Learning application that analyzes
smartphone usage, behavioral patterns, lifestyle indicators,
and personal factors to classify smartphone addiction levels.
</p>

<br>

<a href="https://github.com/mohamedwalidhegab12-dev/Smartphone-Addiction-Classification">
  <img src="https://img.shields.io/badge/VIEW%20SOURCE%20CODE-181717?style=for-the-badge&logo=github&logoColor=white">
</a>

<a href="https://drive.google.com/file/d/1kOx3PsbFDuoRvDmxOYxmjiYP-2O0vgNs/view?usp=sharing">
  <img src="https://img.shields.io/badge/WATCH%20DEMO-4285F4?style=for-the-badge&logo=google-drive&logoColor=white">
</a>

<br><br>

<img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/Scikit--Learn-SVM-F7931E?style=flat-square&logo=scikit-learn&logoColor=white">
<img src="https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=flat-square&logo=streamlit&logoColor=white">
<img src="https://img.shields.io/badge/Plotly-Interactive%20Analytics-3F4F75?style=flat-square&logo=plotly&logoColor=white">
<img src="https://img.shields.io/badge/Pandas-Data%20Processing-150458?style=flat-square&logo=pandas&logoColor=white">
<img src="https://img.shields.io/badge/Joblib-Model%20Persistence-111827?style=flat-square">

<br><br>

<strong>Understand the behavior • Classify the risk • Visualize the patterns</strong>

</div>

---

# 🧭 Table of Contents

- [Overview](#-overview)
- [Problem Statement](#-problem-statement)
- [Solution](#-solution)
- [Key Features](#-key-features)
- [System Workflow](#-system-workflow)
- [Input Dimensions](#-input-dimensions)
- [Behavioral Analytics](#-behavioral-analytics)
- [Machine Learning Pipeline](#-machine-learning-pipeline)
- [Feature Engineering](#-feature-engineering)
- [Prediction Engine](#-prediction-engine)
- [Demo](#-demo)
- [Technology Stack](#-technology-stack)
- [Project Architecture](#-project-architecture)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [How to Run](#-how-to-run)
- [Engineering Highlights](#-engineering-highlights)
- [Future Improvements](#-future-improvements)
- [Contributors](#-contributors)
- [Disclaimer](#-disclaimer)

---

# 🧠 Overview

**Smartphone Addiction Classification** is an end-to-end Machine Learning
project that transforms behavioral and smartphone usage information into
an interpretable addiction-level classification.

The project combines:

```text
Behavioral Data
       ↓
Feature Engineering
       ↓
Categorical Encoding
       ↓
Trained SVM Model
       ↓
Classification
       ↓
Severity Interpretation
       ↓
Interactive Streamlit Dashboard
```

The system is not limited to a simple prediction label.

It also provides a visual behavioral analysis layer that allows users
to understand their smartphone usage patterns through interactive charts.

---

# 🎯 Problem Statement

Smartphone usage has become an important part of everyday life.

However, excessive usage can be associated with behavioral and lifestyle
patterns such as:

- Increased daily smartphone usage
- Frequent phone checking
- High social-media consumption
- Excessive gaming
- Smartphone usage before sleep
- Reduced physical activity
- Sleep-related changes
- Academic performance differences
- Emotional and behavioral indicators

The objective of this project is to use these signals to build a
Machine Learning classification system capable of identifying
different smartphone addiction levels.

---

# 💡 Solution

The proposed solution combines Machine Learning with an interactive
behavioral analytics dashboard.

Users provide information about:

- Personal characteristics
- Smartphone usage behavior
- Lifestyle indicators
- Emotional indicators
- Time allocation

The system then:

1. Processes the provided information.
2. Creates derived behavioral features.
3. Encodes categorical inputs.
4. Aligns the features with the trained model schema.
5. Sends the final feature vector to the SVM classifier.
6. Produces the predicted addiction level.
7. Converts the result into a visual severity index.
8. Displays an interpretable AI insight.

---

# ✨ Key Features

<table>
<tr>

<td width="50%" valign="top">

## 🤖 Machine Learning

- Support Vector Machine classification
- Pre-trained model deployment
- Joblib model persistence
- Feature-schema alignment
- Categorical feature encoding

</td>

<td width="50%" valign="top">

## 🌐 Interactive Dashboard

- Streamlit web application
- Responsive layout
- Dark professional interface
- Glassmorphism cards
- Gradient visual identity

</td>

</tr>

<tr>

<td width="50%" valign="top">

## 📊 Behavioral Analytics

- Time Distribution
- Life Balance Radar
- Weekday vs Weekend
- Interactive Plotly visualizations
- Live analytics based on user inputs

</td>

<td width="50%" valign="top">

## 🎯 Prediction Interpretation

- Addiction classification
- Severity Index
- AI-generated insight
- Visual result card
- Risk-oriented recommendation

</td>

</tr>

<tr>

<td width="50%" valign="top">

## 🧩 Feature Engineering

The system derives additional behavioral
features from the entered information.

Examples:

- Total Time
- Non-Educational Time
- Social Media Ratio

</td>

<td width="50%" valign="top">

## ⚡ Real-Time Interaction

Changes made to the input controls are reflected
directly in the behavioral analytics before running
the final prediction.

</td>

</tr>

</table>

---

# 🔄 System Workflow

<div align="center">

<table>
<tr>

<td align="center">

### 01

👤

<br>

<strong>User Input</strong>

<br><br>

Personal  
Usage  
Health  
Lifestyle

</td>

<td align="center">

→

</td>

<td align="center">

### 02

⚙️

<br>

<strong>Feature Engineering</strong>

<br><br>

Derived  
Behavioral  
Features

</td>

<td align="center">

→

</td>

<td align="center">

### 03

🔤

<br>

<strong>Encoding</strong>

<br><br>

Categorical  
Variables

</td>

<td align="center">

→

</td>

<td align="center">

### 04

🤖

<br>

<strong>SVM Model</strong>

<br><br>

Classification

</td>

<td align="center">

→

</td>

<td align="center">

### 05

📊

<br>

<strong>Dashboard</strong>

<br><br>

Result  
Analytics  
Severity

</td>

</tr>
</table>

</div>

---

# 👤 Input Dimensions

The dashboard organizes the user inputs into clear behavioral categories.

## 1. Personal Profile

The application collects:

- Gender
- Age
- Academic Performance
- Parental Control Level
- Family Communication

---

## 2. Usage Patterns

The application captures:

- Daily Usage Hours
- Weekend Usage Hours
- Phone Checks Per Day
- Hours Used Before Sleep
- Usage Purposes

Supported usage purposes include:

```text
Social Media
Gaming
Educational
Browsing
Other
```

---

## 3. Health & Lifestyle Indicators

The dashboard includes:

- Anxiety Level
- Depression Level
- Self-Esteem Level
- Daily Sleep Hours
- Exercise Hours

---

## 4. Detailed Time Allocation

The application separately tracks:

- Social Media Hours
- Gaming Hours
- Education Hours

This information is also used to generate derived behavioral features.

---

# 📊 Behavioral Analytics

One of the main strengths of the project is that the dashboard does
not wait until the prediction stage to provide information.

The entered data is immediately translated into interactive analytics.

---

## 🍩 01 — Time Distribution

A donut chart visualizes the distribution of the entered time between:

```text
Social Media
Gaming
Education
```

This provides an immediate visual representation of how smartphone-related
time is allocated.

---

## 🕸️ 02 — Life Balance Radar

The radar chart combines five dimensions:

```text
Anxiety
Depression
Academic Performance
Exercise
Sleep
```

The values are normalized to create a single visual behavioral profile.

This allows multiple lifestyle dimensions to be viewed simultaneously.

---

## 📈 03 — Weekday vs Weekend

The dashboard compares:

```text
Daily Usage
      VS
Weekend Usage
```

This makes it easier to identify changes in smartphone behavior
between regular days and weekends.

---

# 🧠 Machine Learning Pipeline

The Machine Learning workflow follows an end-to-end process.

```text
                    ┌─────────────────────┐
                    │   Raw Dataset       │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Data Exploration    │
                    │ & Preprocessing     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Feature Engineering │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Categorical         │
                    │ Encoding            │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Model Training      │
                    │ SVM Classifier      │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Model Persistence   │
                    │ .pkl Assets         │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Streamlit           │
                    │ Deployment          │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Real-Time           │
                    │ Prediction          │
                    └─────────────────────┘
```

---

# 🧩 Feature Engineering

The application creates additional behavioral variables before
sending the data to the model.

## Total Time

```python
Total_Time =
Time_on_Social_Media
+
Time_on_Gaming
+
Time_on_Education
```

---

## Non-Educational Time

```python
Non_Educational_Time =
Time_on_Social_Media
+
Time_on_Gaming
```

---

## Social Media Ratio

```python
Social_Media_Ratio =
Time_on_Social_Media / Total_Time
```

When `Total_Time` is zero, the application safely uses:

```python
0
```

instead of performing an invalid division.

---

# 🔤 Categorical Feature Handling

The application converts categorical information into model-compatible
features.

### Gender

The selected gender is transformed into a corresponding encoded feature.

Example:

```text
Gender_Male
Gender_Female
Gender_Other
```

### Usage Purposes

Selected purposes are represented using corresponding binary features.

Example:

```text
Phone_Usage_Purpose_Social Media
Phone_Usage_Purpose_Gaming
Phone_Usage_Purpose_Educational
Phone_Usage_Purpose_Browsing
Phone_Usage_Purpose_Other
```

The final input is then aligned with the exact feature structure expected
by the trained model.

---

# 🤖 Prediction Engine

The deployed classifier is loaded from the saved SVM model:

```python
model = joblib.load("svm_final.pkl")
```

The expected feature schema is loaded separately:

```python
cols = joblib.load("columns.pkl")
```

Before prediction, the generated DataFrame is reindexed against the
expected model columns.

```python
final_input = df_final.reindex(
    columns=expected_columns,
    fill_value=0
)
```

The final prediction is then generated using:

```python
res = model.predict(final_input)[0]
```

---

# 🎯 Severity Interpretation

The application converts the predicted classification into a visual
severity representation.

| Classification | Severity Index | Interpretation |
|---|---:|---|
| Low / Balanced | 15 | Safe — Balanced habits |
| Moderate | 55 | Warning — Enter danger zone |
| Strong / High | 92 | Critical — Digital Detox recommended |

The severity index is displayed through an interactive Plotly gauge.

> **Important:** The severity index is an application-level visualization
> derived from the predicted class. It is not a clinical score.

---

# 🎬 Project Demo

<div align="center">

<a href="https://drive.google.com/file/d/1kOx3PsbFDuoRvDmxOYxmjiYP-2O0vgNs/view?usp=sharing">

<img
src="https://drive.google.com/thumbnail?id=1kOx3PsbFDuoRvDmxOYxmjiYP-2O0vgNs&sz=w1200"
width="900"
alt="Smartphone Addiction Classification Demo">

</a>

<br><br>

<a href="https://drive.google.com/file/d/1kOx3PsbFDuoRvDmxOYxmjiYP-2O0vgNs/view?usp=sharing">

<img
src="https://img.shields.io/badge/▶%20WATCH%20FULL%20DEMO-4285F4?style=for-the-badge&logo=google-drive&logoColor=white"
alt="Watch Full Demo">

</a>

<br><br>

<sub>
The demo showcases the complete dashboard workflow,
behavioral analytics, model prediction, and severity visualization.
</sub>

</div>

---

# 🖥️ Dashboard Experience

The dashboard was intentionally designed as an AI product interface
rather than a traditional Machine Learning form.

### Visual Design

```text
Dark Background
      +
Glassmorphism Cards
      +
Gradient Typography
      +
Interactive Charts
      +
Responsive Layout
      +
Visual Prediction
```

The application uses custom CSS to create:

- Glass-style cards
- Rounded components
- Gradient headings
- Responsive typography
- Interactive buttons
- Dark visual theme
- Consistent spacing

---

# 🏗️ Project Architecture

```text
┌─────────────────────────────────────────────────────────────┐
│                    SMARTPHONE ADDICTION                     │
│                         SYSTEM                              │
└───────────────────────────────┬─────────────────────────────┘
                                │
               ┌────────────────┴────────────────┐
               │                                 │
               ▼                                 ▼
      ┌─────────────────┐              ┌─────────────────┐
      │  ML Development │              │  Application    │
      └────────┬────────┘              └────────┬────────┘
               │                                │
               ▼                                ▼
      ┌─────────────────┐              ┌─────────────────┐
      │ Jupyter         │              │ Streamlit       │
      │ Notebook        │              │ Dashboard       │
      └────────┬────────┘              └────────┬────────┘
               │                                │
               ▼                                ▼
      ┌─────────────────┐              ┌─────────────────┐
      │ Preprocessing   │              │ User Inputs     │
      │ & Features      │              │ & Analytics     │
      └────────┬────────┘              └────────┬────────┘
               │                                │
               ▼                                ▼
      ┌─────────────────┐              ┌─────────────────┐
      │ SVM Training    │◄─────────────┤ Feature         │
      │                 │              │ Alignment       │
      └────────┬────────┘              └────────┬────────┘
               │                                │
               ▼                                │
      ┌─────────────────┐                        │
      │ svm_final.pkl   │────────────────────────┘
      └────────┬────────┘
               │
               ▼
      ┌─────────────────────────────┐
      │ Addiction Classification    │
      │ + Severity Interpretation   │
      └─────────────────────────────┘
```

---

# 🛠️ Technology Stack

<div align="center">

| Technology | Role |
|---|---|
| 🐍 **Python** | Core programming language |
| 🧠 **Scikit-Learn** | Machine Learning / SVM |
| 🌐 **Streamlit** | Interactive web dashboard |
| 📊 **Plotly** | Interactive visual analytics |
| 🐼 **Pandas** | Data manipulation |
| 🔢 **NumPy** | Numerical processing |
| 💾 **Joblib** | Model & asset persistence |
| 📓 **Jupyter Notebook** | Data Science workflow |

</div>

---

# 📁 Project Structure

```text
Smartphone-Addiction-Classification/
│
├── 📓 Smart_Phone_Addiction_Leval.ipynb
│   └── Machine Learning development & analysis
│
├── 🌐 Stream.py
│   └── Streamlit application
│
├── 📊 teen_phone_addiction_dataset.csv
│   └── Smartphone addiction dataset
│
├── 🤖 svm_final.pkl
│   └── Trained SVM classifier
│
├── 🧩 columns.pkl
│   └── Expected model feature schema
│
├── 🔤 gender_encoder.pkl
│   └── Gender encoding asset
│
├── 🔤 purpose_encoder.pkl
│   └── Usage-purpose encoding asset
│
├── 📦 requirements.txt
│   └── Python dependencies
│
└── 📖 README.md
    └── Project documentation
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/mohamedwalidhegab12-dev/Smartphone-Addiction-Classification.git

cd Smartphone-Addiction-Classification
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ How to Run

Start the Streamlit application:

```bash
streamlit run Stream.py
```

The application will start locally and open in your browser.

---

# 🧑‍💻 How to Use the Application

### Step 01 — Enter Personal Information

Provide:

- Gender
- Age
- Academic Performance
- Parental Control
- Family Communication

---

### Step 02 — Configure Usage Patterns

Set:

- Daily Usage
- Weekend Usage
- Phone Checks
- Screen Time Before Sleep
- Usage Purposes

---

### Step 03 — Enter Health Indicators

Configure:

- Anxiety
- Depression
- Self-Esteem
- Sleep
- Exercise

---

### Step 04 — Allocate Usage Time

Specify:

- Social Media
- Gaming
- Education

---

### Step 05 — Analyze Behavioral Patterns

Review:

- Time Distribution
- Life Balance Radar
- Weekday vs Weekend

---

### Step 06 — Run the AI Classifier

Click:

```text
🚀 ANALYZE ADDICTION LEVEL
```

---

### Step 07 — Review the Result

The system displays:

```text
Diagnosis Result
       +
AI Insight
       +
Severity Index
```

---

# 💡 Engineering Highlights

## 01 — Training / Inference Separation

The Machine Learning workflow is developed inside the Jupyter Notebook,
while the Streamlit application focuses on inference.

This prevents the dashboard from retraining the model during normal use.

---

## 02 — Persisted ML Assets

The trained model and feature schema are stored as reusable artifacts.

```text
svm_final.pkl
columns.pkl
gender_encoder.pkl
purpose_encoder.pkl
```

This allows the application to load the trained assets directly.

---

## 03 — Feature Schema Alignment

The application explicitly aligns the generated input with the expected
training feature structure.

```python
final_input = df_final.reindex(
    columns=expected_columns,
    fill_value=0
)
```

This helps ensure that inference uses the same feature layout expected
by the trained model.

---

## 04 — Cached Model Loading

Streamlit resource caching is used for model assets:

```python
@st.cache_resource
def load_assets():
    ...
```

This avoids repeatedly loading the model during application interaction.

---

## 05 — Real-Time Analytics

The visual analytics are generated directly from the user's current
input values.

This means the dashboard provides immediate behavioral feedback even
before the final prediction is requested.

---

## 06 — Responsive UI

The application includes responsive CSS behavior for smaller screens,
helping the interface remain usable across different viewport sizes.

---

# 📌 What Makes This Project Different?

Many Machine Learning projects stop at:

```text
Dataset → Model → Accuracy
```

This project goes further:

```text
Dataset
   ↓
Data Science
   ↓
Feature Engineering
   ↓
Machine Learning
   ↓
Model Persistence
   ↓
Interactive Dashboard
   ↓
Behavioral Analytics
   ↓
Prediction
   ↓
Severity Visualization
   ↓
User-Oriented Interpretation
```

The result is a complete **Machine Learning application**, rather than
only a notebook-based experiment.

---

# 🚀 Future Improvements

Potential next steps include:

- [ ] Model comparison dashboard
- [ ] Prediction confidence visualization
- [ ] SHAP explainability
- [ ] Feature importance dashboard
- [ ] Historical prediction tracking
- [ ] User accounts
- [ ] Database integration
- [ ] Personalized recommendations
- [ ] Automated retraining pipeline
- [ ] Cloud deployment
- [ ] PDF report generation
- [ ] CSV export
- [ ] Longitudinal behavioral monitoring
- [ ] Advanced digital wellbeing recommendations

---

# 👥 Contributors

<div align="center">

<table>

<tr>

<td align="center" width="50%">

## Mohamed Walid

**AI & Data Science**

Machine Learning  
Feature Engineering  
Streamlit Development  
Dashboard Design

</td>

<td align="center" width="50%">

## Nahed Sheta

**Machine Learning**

Data Science  
Model Development  
Project Development

</td>

</tr>

</table>

</div>

---

# 🎓 Project Context

This project demonstrates the practical integration of:

```text
Data Science
      +
Machine Learning
      +
Feature Engineering
      +
Data Visualization
      +
Software Development
      +
Interactive UI
```

The project was developed to transform a behavioral classification
problem into a usable AI-powered application.

---

# ⚠️ Disclaimer

This application is an educational Machine Learning project.

The classification results and severity index are generated from the
trained model and the application's interpretation logic.

They should **not** be considered a medical, psychological, or clinical
diagnosis.

For professional assessment, qualified specialists should be consulted.

---

# 📜 License

This project is intended for educational, research, and portfolio purposes.

---

<div align="center">

<br>

# 📱 Smartphone Addiction Classification

### Analyze • Classify • Visualize

<br>

<img src="https://img.shields.io/badge/AI%20%26%20Machine%20Learning-Project-6C5CE7?style=for-the-badge">
<img src="https://img.shields.io/badge/Interactive-Streamlit%20Dashboard-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white">

<br><br>

<strong>Built with Python • Scikit-Learn • Streamlit • Plotly</strong>

<br><br>

<sub>
Developed by Mohamed Walid & Nahed Sheta
</sub>

<br><br>

</div>
