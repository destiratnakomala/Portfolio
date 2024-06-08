[➡️➡️➡️ DASHBOARD p0-ftds020-rmt-m1-destiratnakomala](https://lookerstudio.google.com/reporting/902f1672-693e-42d2-8db3-909953cbda9f)

## ANALYSIS OF BEHAVIOR AND GLOBAL SUICIDE RATES FROM 2001 TO 2020

### Problem Statements
The health ministry of various countries wants to create policies and tackle the growing global suicide rates impacting people worldwide.

However, data on global suicide cases is needed as a reference for making these policies.

Therefore, one of the health ministries seeks to gather information on the behavior and suicide rates worldwide from 2001 to 2020 to develop policies based on this data. This is aimed at helping individuals at risk of suicide and preventing it before it is too late.

Here are the problem statements for this milestone:
- Has the number of suicide cases increased annually?
- What is the average percentage of suicide cases for each factor (age, gender, GDP)?
- Who is most at risk of suicide based on age and gender?
- Is there a relationship between suicide rates and a country's GDP?

## Repository Structure


```
Global_Suicide_Rate_Analysis/
│
├── Data_BunuhDiri_v1.csv                     # Main dataset file
│
├── Global_Suicide_Rate_Analysis.ipynb        # Main Jupyter notebook for analysis and modeling
│
├── README.md                                 # Project description and instructions
│
├── Suicide_Rate_Overview_1985_to_2021.csv    # Additional dataset file
│
├── World_Capital_GPS.csv                     # Dataset for world capitals' GPS coordinates
│
└── url.txt                                   # Additional URLs or references
```

## Steps to Follow

### 1. Data Preprocessing
- Load the datasets and handle missing values.
- Encode categorical variables if necessary.
- Normalize/scale numerical features.
- Merge datasets based on relevant keys.

### 2. Exploratory Data Analysis (EDA)
- Visualize the distribution of suicide rates over the years.
- Analyze correlations between suicide rates and other factors (age, gender, GDP).
- Identify key trends and patterns in the data.

### 3. Statistical Analysis
- Calculate average suicide rates for different age groups and genders.
- Determine the percentage of suicide cases for each factor (age, gender, GDP).
- Identify the most vulnerable groups based on age and gender.

### 4. Hypothesis Testing
- Test the hypothesis regarding the increase in suicide rates over the years.
- Analyze the relationship between suicide rates and GDP using correlation analysis and regression models.

## Instructions to Run

### Prerequisites
- Python 3.x
- Required Python packages (listed in `requirements.txt`)

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Global_Suicide_Rate_Analysis.git
   cd Global_Suicide_Rate_Analysis
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Jupyter notebook for data preprocessing, EDA, and statistical analysis:
   ```bash
   jupyter notebook Global_Suicide_Rate_Analysis.ipynb
   ```

## Conclusion
This project aims to provide an in-depth analysis of global suicide rates from 2001 to 2020. By understanding the patterns and relationships between suicide rates and various factors such as age, gender, and GDP, policymakers can develop more effective strategies to prevent suicides and support at-risk populations.

## Future Work
- Incorporate more recent data for a continuous analysis.
- Explore advanced machine learning models to predict future suicide rates.
- Conduct a geographical analysis to identify regional trends and hotspots.
- Collaborate with mental health professionals to interpret the findings and develop intervention strategies.

## Commit Messages
- `Initial commit with project structure and datasets.`
- `Add data preprocessing and EDA notebook.`
- `Implement and evaluate statistical analysis.`
- `Add hypothesis testing and regression analysis.`
- `Update README.md with project details.`

## Additional Resources
- [World Health Organization (WHO) - Suicide Data](https://www.who.int/data/gho/data/themes/mental-health/suicide-rates)
- [Our World in Data - Suicide](https://ourworldindata.org/suicide)
```

