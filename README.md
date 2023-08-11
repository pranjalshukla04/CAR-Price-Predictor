# CAR Price Prediction Web App 🚗

<p align="center">
  <a href="https://pranjal-shukla-car-price-predictor.streamlit.app/" target="_blank" rel="noopener noreferrer">
    <img src="https://github.com/pranjalshukla04/CAR-Price-Predictor/blob/main/Images/here.gif" alt="Explore the App">
  </a>
</p>



## Table of Contents
- [About](#about)
- [Demo](#demo)
- [Feature Details](#feature-details)
- [Usage](#usage)
- [Features](#features)
- [Model Performance](#model-performance)
- [How It Works](#how-it-works)
- [Data Preprocessing](#data-preprocessing)
- [Feature Engineering](#feature-engineering)
- [Model Training](#model-training)
- [Technologies](#technologies)
- [Contributing](#contributing)

## About
Welcome to the Car Price Prediction Web App! This project showcases the deployment of a machine learning model for predicting car prices using the XGBoost algorithm. The app enables users to input various car details and receive accurate price predictions, making sophisticated predictive analytics accessible and engaging.

## Demo
<p align="center">
  <img src="https://github.com/pranjalshukla04/CAR-Price-Predictor/raw/main/SS1.png" alt="Demo" width="1000" />
</p>

## Feature Details
1. **Ex-Showroom Price**: The current price of the car in lakhs (Indian currency).
2. **Distance Driven**: The total distance completed by the car in kilometers.
3. **Fuel Type**: The type of fuel the car uses (Petrol, Diesel, CNG).
4. **Seller Type**: Whether you are a dealer or an individual.
5. **Transmission Type**: The type of transmission (Manual, Automatic) of the car.
6. **Number of Owners**: The number of previous owners the car had.
7. **Purchase Year**: The year in which the car was purchased.

## Usage
1. 🚀 Open the web app in your browser.
2. 📝 Enter specific car details such as ex-showroom price, distance driven, and fuel type.
3. 🎯 Click the "Predict" button to receive a calculated car price estimate.
4. 🎉 Benefit from real-time predictions and visual cues.

## Features
- 🏁 User-friendly interface for predicting car prices.
- 🛠 Interactive widgets to input comprehensive car details.
- ⚙ Real-time predictions powered by the XGBoost model.
- 🎈 Visual cues including celebratory animations and informative warnings.

## Model Performance
Evaluate the model's performance against different algorithms:

| Model            | R2 Score   |
| ---------------- | ---------- |
| Linear Regression| 0.679      |
| Random Forest    | 0.707      |
| Gradient Boost   | 0.882      |
| XGBoost          | 0.886      |

## How It Works
The web app leverages the power of machine learning to provide accurate car price predictions. When users input car details, the XGBoost model processes the data and calculates an estimated price based on a combination of features. The app's user-friendly interface and real-time predictions make it easy to explore potential car prices.

## Data Preprocessing
The raw data underwent preprocessing to handle missing values, scale features, and encode categorical variables. This process ensured the data's quality and suitability for model training.

## Feature Engineering
Additional features were engineered to enhance the model's predictive power. These new features capture important aspects of the car's characteristics, contributing to better predictions.

## Model Training
The model was trained using the XGBoost algorithm on the preprocessed and engineered data. Multiple regression models were evaluated, and the XGBoost model was selected based on its high R2 score and predictive performance.

## Technologies
- 🐍 **Python**: The core programming language driving the app's functionality.
- 📈 **XGBoost**: A powerful machine learning algorithm for regression tasks.
- 🌐 **Streamlit**: A framework for creating interactive web applications.
- 🎨 **HTML/CSS**: Enhanced styling for an engaging user experience.
- 🌀 **Git**: Version control and collaborative development.

## Contributing
Contributions are warmly welcomed! If you discover bugs or have suggestions for improvements, please create an issue or submit a pull request.

---

**Disclaimer**: Please note that the car price predictions presented by the app are generated from a sample XGBoost model and may not reflect current market values. Use the estimates at your discretion and perform thorough research for accurate pricing.

**Project Status**: This project is actively maintained and open for contributions. Feel free to join us in shaping its future!

## Explore our CAR Price Predictor app in action by clicking the following link: 
## 🚀 https://pranjal-shukla-car-price-predictor.streamlit.app/
