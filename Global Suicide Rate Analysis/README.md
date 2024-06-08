[➡️➡️➡️ DASHBOARD p0-ftds020-rmt-m1-destiratnakomala](https://lookerstudio.google.com/reporting/902f1672-693e-42d2-8db3-909953cbda9f)

## ANALISIS PERILAKU DAN TINGKAT KASUS BUNUH DIRI GLOBAL PADA TAHUN 2001-2020

### Problem Statements
Persekutuan kementerian kesehatan negara ingin membuat kebijakan dan menanggulangi kasus bunuh diri masyarakat global yang semakin merajai kehidupan manusia di berbagai belahan dunia.

Namun, diperlukan informasi data mengenai kasus-kasus bunuh diri secara global sebagai acuan pembuatan kebijakan tersebut.

Oleh karena itu, salah satu kementerian kesehatan ingin mencari informasi mengenai perilaku dan tingkat kasus bunuh diri di dunia untuk periode 2001 hingga 2020 agar dapat membuat kebijakan sesuai dengan informasi kasus bunuh diri. Hal ini diharapkan dapat membantu orang-orang yang berpotensi melakukan bunuh diri dan dapat dilakukan pencegahan sebelum terlambat.

Berikut adalah problem statement untuk milestone ini:
- Apakah kasus bunuh diri meningkat setiap tahunnya?
- Berapa persen rata-rata kasus bunuh diri untuk tiap masing-masing faktor (umur, jenis kelamin, besar GDP)?
- Siapa yang paling rentan melakukan bunuh diri berdasarkan usia dan jenis kelamin?
- Apakah ada hubungan antara kasus bunuh diri dengan GDP suatu negara?

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

