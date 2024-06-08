# Cyberbullying Tweet Prediction

## Overview
This project focuses on predicting cyberbullying tweets using machine learning techniques. The objective is to develop models that can accurately identify whether a tweet contains cyberbullying content or not. 

## Dataset Information
The dataset used for this project consists of tweets labeled as either cyberbullying or non-cyberbullying. It contains features such as text content of the tweet and labels indicating whether it is cyberbullying or not.

### Data Structure:
The dataset has the following structure:

- **Text**: Content of the tweet
- **Label**: Binary label indicating whether the tweet is cyberbullying (1) or not (0)

## Methodologies
This project employs the following methodologies:

1. **Data Preprocessing**: 
   - Text cleaning and preprocessing to remove noise and irrelevant information.
   - Feature extraction techniques such as TF-IDF or word embeddings.
   
2. **Model Building**: 
   - Implementation of various machine learning models such as logistic regression, random forest, or deep learning models like LSTM.
   - Hyperparameter tuning to optimize model performance.

3. **Model Evaluation**: 
   - Evaluation of models using metrics such as accuracy, precision, recall, and F1-score.
   - Cross-validation to ensure the robustness of the models.

4. **Deployment**: 
   - Deployment of the best-performing model as a web application using Flask.

## Deployment
To deploy the model and related files, follow these steps:

1. **Clone the Repository**: 
   ```
   git clone <repository_url>
   ```
   Replace `<repository_url>` with the URL of the repository.

2. **Navigate to the Deployment Directory**: 
   ```
   cd deployment
   ```

3. **Install Dependencies**: 
   ```
   pip install -r requirements.txt
   ```

4. **Run the Application**: 
   - Ensure that Python and all required dependencies are installed (specified in `requirements.txt`).
   - Run `app.py` using Python:
     ```
     python app.py
     ```

   This will start the application locally.
