# Airline Passenger Satisfaction Prediction

## Project Description
This project involves building a classification model to predict airline customer satisfaction based on various features such as demographic factors, flight-related delays, and service quality ratings. The objective is to identify key areas for improvement to enhance customer satisfaction and promote the airline's services to a broader audience.

## Dataset Information
The dataset includes the following information:
- **Customer Satisfaction (`satisfaction`)**: 
  - 0: Dissatisfied
  - 1: Satisfied
- **Demographic Factors**:
  - Gender
  - Age
- **Time Factors**:
  - Departure Delay in Minutes
  - Arrival Delay in Minutes
  - Departure/Arrival time convenient
- **Service Quality Ratings**:
  - Food and drink
  - Gate location
  - Inflight wifi service
  - Inflight entertainment
  - Online support
  - Ease of Online booking
  - On-board service
  - Leg room service
  - Baggage handling
  - Checkin service
  - Cleanliness
  - Online boarding
  - Seat comfort
  - Class
  - Customer Type
  - Type of Travel
  - Flight Distance

## Objective
Aiming to improve service quality and increase passenger numbers, the airline seeks to focus on which services to enhance. By predicting passenger satisfaction, we can identify areas needing improvement. The models used include Logistic Regression, K-Nearest Neighbors (KNN), Decision Tree, Random Forest, and Support Vector Classifier (SVC), targeting a recall and accuracy above 80%.

## Repository Structure

```
Airline_Passenger_Satisfaction/
│
├── deployment/
│ ├── airline.jpg # Image for the application (optional)
│ ├── app.py # streamlit application for model deployment
│ ├── eda.py # Script for exploratory data analysis
│ ├── prediction.py # Script for making predictions
│ └── requirements.txt # Dependencies for deployment
│
├── Airline_Passengers_Satisfaction.ipynb # Main Jupyter notebook for analysis and modeling
│
├── INVISTICO.csv # Dataset file
│
├── P2FP_desti_ratna_komala.ipynb # Additional notebook (if needed)
│
├── README.md # Project description and instructions
│
└── url.txt # Additional URLs or references
```
## Steps to Follow

### 1. Data Preprocessing
- Load the dataset and handle missing values.
- Encode categorical variables.
- Normalize/scale numerical features.
- Split the data into training and testing sets.

### 2. Exploratory Data Analysis (EDA)
- Visualize the distribution of each feature.
- Analyze correlations between features.
- Identify key trends and patterns in the data.

### 3. Model Building
- Implement Logistic Regression, KNN, Decision Tree, Random Forest, and SVC.
- Train the models on the training set.
- Evaluate the models using accuracy and recall on the test set.
- Tune hyperparameters to optimize model performance.

### 4. Feature Importance
- Analyze feature importance for tree-based models.
- Identify the most significant features impacting customer satisfaction.

## Instructions to Run

### Prerequisites
- Python 3.x
- Required Python packages (listed in `deployment/requirements.txt`)

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Airline_Passenger_Satisfaction.git
   cd Airline_Passenger_Satisfaction
   ```

2. Install the required packages:
   ```bash
   pip install -r deployment/requirements.txt
   ```

3. Run the Jupyter notebook for data preprocessing, EDA, and model building:
   ```bash
   jupyter notebook Airline_Passengers_Satisfaction.ipynb
   ```

## Evaluation Metrics
- **Accuracy**: Measure of correct predictions over total predictions.
- **Recall**: Measure of correctly identified positive samples.

## Conclusion
This project aims to build a reliable prediction model to identify key factors influencing customer satisfaction in the airline industry. By focusing on these areas, the airline can enhance its service quality, ultimately leading to increased customer satisfaction and loyalty.

## Future Work
- Implement additional models and compare their performance.
- Explore advanced feature engineering techniques.
- Conduct a deeper analysis on the misclassified samples to identify potential improvements.

## Commit Messages
- `Initial commit with project structure and dataset.`
- `Add data preprocessing and EDA notebook.`
- `Implement and evaluate classification models.`
- `Add feature importance analysis.`
- `Update README.md with project details.`
```

