# 🏠 California House Price Predictor — ML Web App

An end-to-end Machine Learning project that predicts housing prices in California using demographic and geographic features.  
The model is deployed as a production-ready web application with a REST API built using Flask.

---

## 🚀 Live Capabilities

- 🔮 Real-time house price prediction  
- 🌐 Interactive web interface  
- 📡 REST API for external integration  
- 🧠 Model trained on real-world dataset  
- 🧪 Postman testing support  

---

## 📖 Project Overview

This project demonstrates the complete ML lifecycle:

Data Analysis → Model Training → Evaluation → Deployment → API Exposure → UI Integration

The model estimates median house value based on features such as income, housing characteristics, population, and geographic location.

---

## 📊 Model Details

- **Algorithm:** Linear Regression  
- **Dataset:** California Housing Dataset (Scikit-learn)  
- **Problem Type:** Regression  

### 📈 Performance Metrics

- **R² Score:** 0.51  
- **Mean Squared Error (MSE):** 0.66 
- **Root Mean Squared Error (RMSE):** 0.81

> Linear Regression was selected as a baseline model for interpretability and fast deployment.

---

## 🧩 Features Used

- Median Income  
- House Age  
- Average Rooms  
- Average Bedrooms  
- Population  
- Average Occupancy  
- Latitude  
- Longitude  

---

## 🖥️ Web Application Features

- Clean responsive UI  
- Animated prediction result page  
- Input validation  
- Professional layout  
- Portfolio-ready presentation  

---

## 📡 REST API

### Endpoint


POST /api/predict


### Sample Request (JSON)

```json
{
  "MedInc": 8.3252,
  "HouseAge": 41,
  "AveRooms": 6.984,
  "AveBedrms": 1.023,
  "Population": 322,
  "AveOccup": 2.555,
  "Latitude": 37.88,
  "Longitude": -122.23
}
Sample Response
{
  "prediction": 4.526,
  "status": "success"
}
🧪 Postman Testing

Run the Flask application

Open Postman

Send POST request to:

http://127.0.0.1:5000/api/predict

Use JSON body with required features

⚙️ Project Structure
California_House_Prediction/
│
├── ml_flask/
│   ├── app.py
│   ├── california2.joblib
│   ├── templates/
│   │   ├── index.html
│   │   └── result.html
│   ├── static/
│   │   └── style.css
│
└── README.md
🛠️ Tech Stack

Python

Flask

Scikit-learn

NumPy

Joblib

HTML5

CSS3

▶️ How to Run Locally

1️⃣ Clone Repository
git clone https://github.com/your-username/your-repo-name.git
2️⃣ Navigate to Project
cd your-repo-name
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Run Application
python app.py

Open in browser:

http://127.0.0.1:5000
💼 Use Cases

Property price estimation

Real estate analysis

Investment decision support

Academic ML deployment demonstration

API integration practice

🎯 Learning Outcomes

This project demonstrates:

✔ End-to-end ML workflow
✔ Model evaluation techniques
✔ Web deployment using Flask
✔ REST API development
✔ Frontend integration
✔ Production-style project structure

👨‍💻 Author

Sanjana
Data Science & Machine Learning Enthusiast