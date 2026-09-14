Medical Insurance Cost Analysis and Interactive Dashboard
DS602 – Statistical Methods | Lab-4
Project link - https://mysiteds.streamlit.app/

This project focuses on analyzing medical insurance costs using statistical methods and presenting the results through an interactive Streamlit dashboard.

The project includes data cleaning, exploratory data analysis, descriptive statistics, hypothesis testing, multiple linear regression using OLS, regression diagnostics, and live insurance charge prediction.

1. Project Objective

The main objective of this project is to study how demographic and lifestyle factors are related to medical insurance charges.

The analysis focuses on variables such as age, BMI, children, sex, smoking status, and region. Statistical tests and regression techniques are used to understand important relationships in the dataset.

2. Dataset

The project uses the Medical Insurance Cost dataset.

Dataset file: data/insurance.csv

The dataset contains the following variables:

Variable	Description
age	Age of the beneficiary
sex	Sex of the beneficiary
bmi	Body Mass Index
children	Number of children/dependents
smoker	Smoking status
region	Residential region
charges	Medical insurance charges

The target variable for the regression model is charges.

The original dataset contained 1,338 records. One duplicate record was removed during data cleaning, resulting in 1,337 records for the final analysis.

3. Technologies Used

The project was developed using Python.

Main libraries used:

Pandas
NumPy
SciPy
Statsmodels
Matplotlib
Seaborn
Scikit-learn
Streamlit
Plotly
Joblib

These libraries were used for data processing, statistical analysis, visualization, regression modeling, diagnostics, and dashboard development.

4. Project Structure

The project contains the following main files:

data/insurance.csv – dataset
models/insurance_model.pkl – saved regression model
analysis.ipynb – statistical analysis and experiments
app.py – Streamlit dashboard
requirements.txt – required Python libraries
README.md – project documentation
Lab4_DS602_MSc.pdf – assignment reference
5. Data Cleaning

The dataset was checked for:

Missing values
Duplicate records
Data types
Dataset dimensions
Numerical and categorical variables

No missing values were found.

One duplicate record was identified and removed.

Final dataset size:

1337 rows × 7 columns

6. Exploratory Data Analysis

Exploratory Data Analysis was performed to understand the data and identify important patterns.

The analysis includes:

Dataset inspection
Summary statistics
Distribution plots
KDE plots
Scatter plots
Correlation matrix
Group-wise comparison

The numerical variables considered were age, BMI, children, and charges.

7. Descriptive Statistics

The following descriptive measures were calculated:

Mean
Median
Standard deviation
Interquartile range
Skewness
Kurtosis
Variable	Mean	Median	Standard Deviation	IQR	Skewness	Kurtosis
Age	39.22	39.00	14.04	24.00	0.05	-1.24
BMI	30.66	30.40	6.10	8.41	0.28	-0.05
Children	1.10	1.00	1.21	2.00	0.94	0.20
Charges	13279.12	9386.16	12110.36	11911.37	1.52	1.60

Insurance charges have noticeable positive skewness because some observations have much higher charges than the majority of the dataset.

8. Visualization

Different visualizations were created to understand the dataset.

Distribution Analysis

Histograms with KDE were created for:

Age
BMI
Children
Charges
Bivariate Analysis

Scatter plots were used to examine relationships such as:

BMI vs Charges
Age vs Charges
Children vs Charges

Smoking status was also used to compare the relationship between BMI and charges.

Correlation Analysis

The correlation between numerical variables and charges was:

Variable	Correlation with Charges
Age	0.30
BMI	0.20
Children	0.07

Age has the strongest correlation with charges among the three variables, although the relationship is still moderate rather than very strong.

9. Hypothesis Testing

Hypothesis testing was performed using a significance level of:

α = 0.05

The decision rule used throughout the analysis is:

p-value < 0.05 → Reject H₀

p-value ≥ 0.05 → Fail to Reject H₀

Two main statistical tests were performed.

10. Hypothesis Test 1 – Smoker Status vs Charges

The first test compares insurance charges between smokers and non-smokers.

Hypotheses

H₀: There is no significant difference in insurance charges between smokers and non-smokers.

H₁: There is a significant difference in insurance charges between smokers and non-smokers.

Group Results
Group	Count	Average Charges
Smokers	274	32050.23
Non-smokers	1063	8440.66
Shapiro-Wilk Test

For smokers:

p-value = 3.62 × 10⁻⁹

For non-smokers:

p-value = 1.50 × 10⁻²⁸

Both p-values are below 0.05, so the normality assumption was rejected.

Levene's Test

Test statistic = 332.4714

p-value = 1.67 × 10⁻⁶⁶

The p-value is below 0.05, so equal variance was also rejected.

Mann-Whitney U Test

Because the normality assumption was not satisfied, the Mann-Whitney U test was used.

U statistic = 283859.0

p-value = 5.747 × 10⁻¹³⁰

Conclusion

The p-value is much smaller than 0.05, so H₀ is rejected.

There is a statistically significant difference in insurance charges between smokers and non-smokers. Smokers have substantially higher average insurance charges.

11. Hypothesis Test 2 – Charges Across Regions

A One-Way ANOVA was performed to compare insurance charges across the four regions.

The regions were:

Northeast
Northwest
Southeast
Southwest
Average Charges
Region	Mean Charges
Northeast	13406.38
Northwest	12450.84
Southeast	14735.41
Southwest	12346.94
Hypotheses

H₀: The mean insurance charges are equal across all regions.

H₁: At least one region has a different mean insurance charge.

ANOVA Result

F statistic = 2.9261

p-value = 0.0327628803

Conclusion

Since the p-value is below 0.05, H₀ is rejected.

There is a statistically significant difference in insurance charges across the regions.

The ANOVA test only tells us that at least one group differs. A post-hoc test would be needed to determine exactly which regions are significantly different.

12. Multiple Linear Regression

Multiple Linear Regression was used to estimate insurance charges using several predictors at the same time.

The model can be represented as:

Y = β₀ + β₁X₁ + β₂X₂ + ... + βₖXₖ + ε

Here, the dependent variable is charges.

The predictors include:

Age
BMI
Children
Sex
Smoker
Region

Categorical variables were converted into dummy variables before fitting the model.

13. OLS Regression

The regression model was fitted using Ordinary Least Squares through Statsmodels.

Important model results were:

R-squared = 0.751

Adjusted R-squared = 0.749

F-statistic = 500.0

The model explains approximately 75.1% of the variation in insurance charges.

14. Important Regression Results
Predictor	Coefficient	p-value
Age	256.7646	< 0.001
BMI	339.2504	< 0.001
Children	474.8205	0.001
Sex Male	-129.4815	0.698
Smoker Yes	≈ 23850	< 0.001
Region Northwest	-349.2265	0.464
Region Southeast	-1035.2656	0.031
Region Southwest	-960.0814	0.045
15. Regression Interpretation

Age has a positive coefficient, meaning insurance charges tend to increase as age increases while keeping other variables constant.

BMI also has a positive coefficient, indicating that higher BMI is associated with higher predicted charges.

The coefficient for children is positive, meaning an additional dependent is associated with an increase in predicted charges.

Smoking status has a very strong positive coefficient. This indicates that smokers have considerably higher predicted insurance charges compared with non-smokers, after controlling for the other variables.

The p-value for sex is 0.698, which is greater than 0.05. Therefore, sex is not statistically significant in this regression model.

16. Regression Diagnostics

Regression diagnostics were performed to check the assumptions and behaviour of the OLS model.

The analysis includes:

Residuals vs Fitted plot
Q-Q plot
Jarque-Bera test
Breusch-Pagan test
VIF analysis
17. Residuals vs Fitted Plot

The residuals vs fitted plot was used to examine whether the residuals show systematic patterns.

This helps assess:

Linearity
Constant variance
Possible model problems

The plot is included in the analysis and dashboard for visual inspection.

18. Q-Q Plot

The Q-Q plot was used to examine whether the regression residuals approximately follow a normal distribution.

The residuals deviate from the reference line, particularly in the tails, indicating that the residuals are not perfectly normally distributed.

19. Jarque-Bera Test

The Jarque-Bera test was performed on the regression residuals.

Statistic = 716.5524

p-value = 2.527045383262612e-156

Since the p-value is below 0.05, the null hypothesis of normally distributed residuals is rejected.

Therefore, the regression residuals are not normally distributed.

20. Variance Inflation Factor

VIF was used to check for possible multicollinearity among the continuous predictors.

The main continuous predictors considered were:

Age
BMI
Children

VIF helps determine whether predictors have strong linear relationships with each other.

21. Streamlit Dashboard

The project includes an interactive Streamlit dashboard.

The dashboard is divided into three main sections.

Data Exploration

This section allows the user to:

View the dataset
Apply filters
View summary statistics
Explore distributions
View scatter plots
Examine correlations
Hypothesis Testing Lab

This section provides an interactive interface for statistical testing.

Users can select variables and perform appropriate statistical tests.

The dashboard displays:

Test statistic
p-value
Significance level
Statistical decision
Interpretation
Live Prediction and Diagnostics

This section allows users to enter:

Age
Sex
BMI
Number of children
Smoking status
Region

The application then generates a predicted insurance charge.

Diagnostic results are also displayed to help understand the regression model.

22. Live Prediction

The saved OLS model is used to generate insurance charge predictions.

The prediction changes according to the values entered by the user.

The dashboard also provides a 95% prediction interval to represent uncertainty around an individual prediction.

23. Main Findings

The main findings from the analysis are:

Insurance charges are positively skewed.
Smokers have much higher average insurance charges than non-smokers.
The difference between smoker and non-smoker charges is statistically significant.
Insurance charges differ significantly across regions according to the One-Way ANOVA.
Age has a positive relationship with insurance charges.
BMI has a positive relationship with insurance charges.
Smoking status is one of the strongest predictors in the regression model.
The OLS model has an R-squared of approximately 0.751.
The regression residuals are not normally distributed according to the Jarque-Bera test.
24. Installation and Running

Open the project folder in VS Code.

Install the required packages using:

pip install -r requirements.txt

Then start the dashboard using:

streamlit run app.py

The application will normally be available at:

http://localhost:8501

25. Analysis Notebook

The analysis.ipynb notebook contains the statistical analysis performed during the project.

It includes:

Data loading
Data cleaning
Descriptive statistics
Data visualization
Correlation analysis
Hypothesis Test 1
Hypothesis Test 2
OLS regression
Regression diagnostics
Jarque-Bera test
VIF analysis
26. Conclusion

This project demonstrates the application of statistical methods to the Medical Insurance Cost dataset.

The analysis combines exploratory data analysis, descriptive statistics, hypothesis testing, multiple linear regression, OLS modeling, and regression diagnostics.

The results show that smoking status has a particularly strong relationship with medical insurance charges. Age and BMI also contribute to the prediction of insurance costs.

The Streamlit dashboard makes the analysis interactive by allowing users to explore the dataset, perform statistical tests, examine regression results, and generate live insurance charge predictions.

Overall, the project provides a complete workflow from data cleaning and statistical analysis to interactive visualization and prediction.

27. Academic Information

Course: DS602 – Statistical Methods

Lab: Lab-4 – Applied Statistical Modeling & Interactive Web Dashboard

Dataset: Medical Insurance Cost Dataset

Target Variable: charges

Significance Level: α = 0.05

Student ID: 202618063