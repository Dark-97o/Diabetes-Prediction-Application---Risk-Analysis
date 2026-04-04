# 🏥 End-to-End Diabetes Risk Prediction with Explainable AI

## 📑 Table of Contents
- [Overview](#overview)
- [Motivation](#motivation)
- [Key Features](#key-features)
- [Technical Aspect](#technical-aspect)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Run Locally](#run-locally)
- [Screenshots](#screenshots)
- [Team](#team)
- [Credits](#credits)

---

## 📌 Overview
This project is an advanced Machine Learning web application that predicts the likelihood of diabetes using medical parameters. It leverages the **Pima Indians Diabetes Dataset** to analyze patient health data and generate a **probability-based risk score**.

Unlike traditional ML models, this system integrates **Explainable AI (XAI)** to provide transparent and interpretable predictions, helping users understand *why* they are at risk through interactive visualizations and detailed risk factor analysis.

---

## 🎯 Motivation
Diabetes is a rapidly growing global health concern affecting millions worldwide. Early detection can significantly reduce complications and improve quality of life.

This project was built to:
- Move beyond "black-box" predictions  
- Provide **interpretable insights** into health risks
- Empower users to understand key contributing health factors  
- Make medical AI accessible and understandable to everyone

---

## 🚀 Key Features

### 🔢 1. Probability-Based Prediction
- Outputs **precise risk percentage** instead of binary result (Yes/No)
- Uses `predict_proba()` for confidence scoring
- Real-time risk assessment

### 📊 2. Interactive Risk Analysis Dashboard 🔥 NEW
- **Dynamic bar chart visualization** showing all health metrics
- **Color-coded risk indicators:**
  - 🔴 **Red** = High Risk (requires immediate attention)
  - 🟠 **Orange** = Medium Risk (monitor closely)
  - 🟢 **Green** = Normal Range (healthy)
- Built using **Chart.js** for smooth, real-time rendering

### 🔍 3. Intelligent Risk Factor Breakdown
- **Bilingual explanations** (Hindi + English) for better accessibility
- Detailed analysis of each health parameter:
  - Glucose levels
  - BMI (Body Mass Index)
  - Blood Pressure
  - Insulin levels
  - Age factor
  - Pregnancy history
  - Genetic predisposition (Diabetes Pedigree Function)
- Smart threshold-based risk categorization

### 🧠 4. Explainable AI (XAI)
- Breaks down prediction into **feature-level impact**
- Shows *why* each factor contributes to risk
- Improves trust and medical decision-making
- User-friendly interpretation of ML results

### 🧹 5. Smart Data Preprocessing
- Handles missing/invalid values (0 → NaN conversion)
- Uses **Mean/Median Imputation** for data cleaning
- Robust feature scaling and normalization
- Ensures model accuracy and reliability

### 🎨 6. Modern Responsive UI
- **Dual-theme design:**
  - Clean white card on gradient background (input form)
  - Dark glassmorphic theme (results page)
- Fully responsive for mobile, tablet, and desktop
- Smooth animations and transitions
- Intuitive user experience
- Print-friendly report generation

### 📱 7. Additional Features
- **Download Report** - Print/save results for medical records
- **Check Again** - Quick reset for new predictions
- **Health Metrics Card** - Summary of all input values
- **Loading animations** - Better user feedback

---

## ⚙️ Technical Aspect

### 🧾 Data Processing Pipeline
1. **Data Cleaning:**
   - Identified and removed invalid zero values in critical features:
     - Blood Pressure  
     - BMI  
     - Insulin  
     - Glucose
     - Skin Thickness
   
2. **Statistical Imputation:**
   - Applied mean/median imputation strategies
   - Preserved data distribution
   - Minimized bias in predictions

3. **Feature Engineering:**
   - Standardized feature scaling
   - Handled outliers appropriately

### 🤖 Machine Learning Model
- **Algorithm:** Random Forest Classifier
  - **Estimators:** 20 trees
  - **Criterion:** Gini impurity
  - **Max Depth:** Optimized through cross-validation
  - Balanced accuracy and inference speed
  - Robust to overfitting

### 🔗 Backend Architecture
- Model serialized using `pickle` for fast loading
- **Flask** RESTful API for predictions
- Session management for multi-user support
- Efficient request handling

### 📈 Risk Analysis Logic
```python
# Dynamic risk categorization
thresholds = {
    'glucose': {'high': 140, 'medium': 100},
    'bmi': {'high': 30, 'medium': 25},
    'bp': {'high': 90, 'medium': 80},
    'age': {'high': 45, 'medium': 35},
    'insulin': {'high': 200, 'medium': 100},
    'pregnancies': {'high': 6, 'medium': 3},
    'dpf': {'high': 0.8, 'medium': 0.5}
}
```
- Extracted feature importance from trained model
- Mapped dynamically to user input
- Visualized using Chart.js with color coding

### 🎯 Frontend Integration
- **Chart.js** for interactive visualizations
- **Vanilla JavaScript** for dynamic DOM manipulation
- **CSS3** for modern animations and glassmorphism effects
- **Responsive Grid Layout** for adaptive design

---

## 🛠️ Technologies Used

### Backend
![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-black.svg)
![NumPy](https://img.shields.io/badge/NumPy-1.21+-013243.svg)
![Pandas](https://img.shields.io/badge/Pandas-1.3+-150458.svg)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.0+-F7931E.svg)

### Frontend
![HTML5](https://img.shields.io/badge/HTML5-E34F26.svg?logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6.svg?logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E.svg?logo=javascript&logoColor=black)
![Chart.js](https://img.shields.io/badge/Chart.js-FF6384.svg?logo=chartdotjs&logoColor=white)

### Tools & Libraries
- **Pickle** - Model serialization
- **Jinja2** - Template engine
- **Google Fonts (Inter)** - Modern typography
- **Git** - Version control

---

## ⚡ Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Git

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/diabetes-prediction-xai.git
cd diabetes-prediction-xai
```

### Step 2: Create Virtual Environment (Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Verify Model File
Ensure `diabetes-prediction-rfc-model.pkl` is in the root directory.

---

## 🚀 Run Locally

### Method 1: Standard Flask Run
```bash
python app.py
```

### Method 2: Flask CLI
```bash
export FLASK_APP=app.py  # Linux/macOS
set FLASK_APP=app.py     # Windows

flask run
```

### Access the Application
Open your browser and navigate to:
```
http://127.0.0.1:5000/
```

### Expected Output
```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
```

---

## 📸 Screenshots

### 1. Input Form
<img width="608" height="845" alt="Screenshot 2026-04-04 171411" src="https://github.com/user-attachments/assets/c102795b-62d0-48b7-9fb7-fde67b9d7e4b" />

Modern, clean interface for entering health metrics with:
- Organized two-column grid layout
- Input validation and placeholders
- Unit indicators for each field

### 2. Results Dashboard
<img width="974" height="342" alt="Screenshot 2026-04-04 171511" src="https://github.com/user-attachments/assets/4858aa5d-e638-4c2a-8513-ff2af9d55779" />
<img width="994" height="613" alt="Screenshot 2026-04-04 171524" src="https://github.com/user-attachments/assets/49d37907-df76-4d36-9316-13d5690d067c" />
<img width="982" height="591" alt="Screenshot 2026-04-04 171537" src="https://github.com/user-attachments/assets/31024d06-ed06-40b9-9466-9b5804b9266f" />
 
Comprehensive analysis page featuring:
- Risk probability with visual indicator
- Interactive bar chart of all metrics
- Color-coded risk factor breakdown
- Bilingual explanations
- Downloadable report option

---

## 📦 Project Structure
```
diabetes-prediction-xai/
│
├── app.py                          # Flask application
├── diabetes-prediction-rfc-model.pkl  # Trained ML model
├── requirements.txt                # Python dependencies
│
├── templates/
│   ├── index.html                  # Input form page
│   └── result.html                 # Results dashboard
│
├── static/
│   └── (optional static assets)
│
└── README.md                       # Project documentation
```

---

## 🧪 Model Training (Optional)

If you want to retrain the model:

```python
from sklearn.ensemble import RandomForestClassifier
import pickle
import pandas as pd

# Load and preprocess data
df = pd.read_csv('diabetes.csv')

# Handle zero values
columns_to_fix = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
df[columns_to_fix] = df[columns_to_fix].replace(0, np.nan)
df.fillna(df.median(), inplace=True)

# Train model
X = df.drop('Outcome', axis=1)
y = df['Outcome']

model = RandomForestClassifier(n_estimators=20, random_state=42)
model.fit(X, y)

# Save model
pickle.dump(model, open('diabetes-prediction-rfc-model.pkl', 'wb'))
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 Future Enhancements

- [ ] Add LIME/SHAP for advanced explainability
- [ ] Integrate real-time data from wearables
- [ ] Multi-language support (Spanish, French, etc.)
- [ ] User authentication and history tracking
- [ ] PDF report generation
- [ ] Mobile app version (React Native/Flutter)
- [ ] API endpoint for third-party integration
- [ ] A/B testing for model improvements

---

## 👥 Team

**Rakesh Bangra**  
- Role: AIML Engineer
- Contributions: Model development, UI/UX design, XAI implementation

---

## 🙏 Credits

- **Dataset:** [Pima Indians Diabetes Database](https://www.kaggle.com/uciml/pima-indians-diabetes-database) (UCI Machine Learning Repository)
- **Chart.js:** Interactive visualization library
- **Google Fonts:** Inter typeface
- **Flask Community:** Framework and documentation
- **Scikit-Learn:** Machine learning tools

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📧 Contact

For queries or suggestions:
- **Email:** contact.bangra@gmail.com
- **GitHub:** [@mrincredibletx](https://github.com/mrincredibletx)
- **LinkedIn:** [Rakesh Bangra](https://linkedin.com/in/yourprofile)

---

## ⭐ Acknowledgments

Special thanks to:
- UCI Machine Learning Repository for the dataset
- The open-source community
- Medical professionals who provided domain insights
- Beta testers for valuable feedback

---

<div align="center">

### Made with ❤️

**Star ⭐ this repository if you found it helpful!**

</div>
