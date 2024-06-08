# Bank Marketing Term Deposit Prediction

## Overview
This project focuses on predicting whether bank customers in Vietnam will subscribe to a term deposit product. By analyzing customer behavior and demographic information, the goal is to develop a predictive model that can identify potential subscribers, enabling the bank to target its marketing efforts more effectively.

## Dataset Information
The dataset comprises marketing campaign data from a bank in Vietnam, with 42,639 rows and 16 columns. The target feature (`term_deposit`) indicates whether a client will subscribe to a term deposit product (0 for not subscribing and 1 for subscribing). 

### Data Structure:
The dataset has the following structure:

- **ID**: Client ID
- **age**: Age of the client
- **job**: Job type of the client
- **marital**: Marital status of the client
- **education**: Education level of the client
- **default**: Whether the client has defaulted on credit card payments
- **housing**: Whether the client has a housing loan
- **loan**: Whether the client has a personal loan
- **balance**: Account balance of the client
- **month**: Month of the last contact with the client
- **day**: Day of the last contact with the client
- **duration**: Duration of the last contact with the client (in seconds)
- **campaign**: Number of contacts performed during the marketing campaign
- **pdays**: Number of days since the client was last contacted by the marketing team
- **previous**: Number of contacts performed before the marketing campaign
- **term_deposit**: Whether the client will subscribe to a term deposit (0 for not subscribing, 1 for subscribing)

## Objective
The objective of this project is to maximize marketing efforts for a term deposit product by accurately predicting customer subscriptions. By leveraging machine learning techniques, the bank can identify key factors that influence subscription decisions and tailor its marketing strategies accordingly.

## Conclusion
Based on the modeling performed, the tuned XGBoosting model emerged as the best performer in predicting customer subscriptions to term deposits. With an accuracy rate of up to 88%, a classification rate of 89%, and a very low prediction error rate of 7%, the model demonstrates promising results.

Key features such as housing loan status and personal loan status were identified as the most important indicators of whether a client will subscribe to a term deposit. Additionally, factors such as job type, marital status, and duration of marketing team contact played significant roles in determining subscription likelihood.

### Marketing Strategy Recommendations:

1. **Targeted Surveys**: Conduct in-depth surveys or direct inquiries to understand why clients join or leave the bank. Offer rewards for completing surveys to encourage participation and gather valuable insights for business strategy.

2. **Demographic-Based Offers**: Tailor marketing offers based on public information such as product trends and consumer income per demographic. Offer trending products to clients with high consumerism levels and provide bonuses related to household products for married clients.

3. **Enhanced Customer Service**: Prioritize excellent customer service to retain clients and minimize churn. Monitor client progress and offer beneficial solutions to address financial concerns.

4. **Other Tactics**:
   - Collaborate with other companies/banks.
   - Customize marketing based on client shopping behavior.
   - Utilize online/onsite/telephone marketing channels.
   - Highlight success stories of satisfied clients.

## Cloning the Repository
To clone this repository and run the project locally, follow these steps:

1. Open your terminal or command prompt.
2. Navigate to the directory where you want to clone the repository.
3. Run the following command:
   ```
   git clone <repository_url>
   ```
   Replace `<repository_url>` with the URL of this repository.

