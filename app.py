import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import statsmodels.api as sm


# Page settings
st.set_page_config(
    page_title="Medical Insurance Statistical Dashboard",
    layout="wide"
)


# Get project folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_PATH = os.path.join(
    BASE_DIR,
    "data",
    "insurance.csv"
)


# Load data
df = pd.read_csv(DATA_PATH)
df = df.drop_duplicates()


# Prepare data for OLS
df_model = pd.get_dummies(
    df,
    columns=["sex", "smoker", "region"],
    drop_first=True,
    dtype=int
)


# Features and target
X = df_model.drop("charges", axis=1)
y = df_model["charges"]


# Add constant
X = sm.add_constant(X)


# Train OLS model
model = sm.OLS(y, X).fit()


# Model columns
model_columns = X.columns.tolist()


# =========================================================
# TITLE
# =========================================================

st.title(
    "Medical Insurance Statistical Modeling Dashboard"
)

st.write(
    "This dashboard explores medical insurance data, "
    "performs hypothesis tests, and predicts insurance charges."
)


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.header("Data Filters")


age_range = st.sidebar.slider(
    "Age",
    int(df["age"].min()),
    int(df["age"].max()),
    (
        int(df["age"].min()),
        int(df["age"].max())
    )
)


bmi_range = st.sidebar.slider(
    "BMI",
    float(df["bmi"].min()),
    float(df["bmi"].max()),
    (
        float(df["bmi"].min()),
        float(df["bmi"].max())
    )
)


smoker_filter = st.sidebar.multiselect(
    "Smoker",
    df["smoker"].unique(),
    default=list(df["smoker"].unique())
)


region_filter = st.sidebar.multiselect(
    "Region",
    df["region"].unique(),
    default=list(df["region"].unique())
)


# Apply filters
filtered_df = df[
    (df["age"].between(
        age_range[0],
        age_range[1]
    )) &
    (df["bmi"].between(
        bmi_range[0],
        bmi_range[1]
    )) &
    (df["smoker"].isin(smoker_filter)) &
    (df["region"].isin(region_filter))
]


# =========================================================
# TABS
# =========================================================

tab1, tab2, tab3 = st.tabs(
    [
        "Data Exploration",
        "Hypothesis Testing Lab",
        "Live Prediction & Diagnostics"
    ]
)


# =========================================================
# TAB 1
# DATA EXPLORATION
# =========================================================

with tab1:

    st.subheader("Filtered Dataset")

    st.write(
        "Number of records:",
        len(filtered_df)
    )

    st.dataframe(filtered_df)


    # Summary statistics
    st.subheader("Summary Statistics")

    numeric_cols = [
        "age",
        "bmi",
        "children",
        "charges"
    ]

    summary = filtered_df[
        numeric_cols
    ].describe().round(2)

    st.dataframe(summary)


    # Distribution
    st.subheader(
        "Distribution of Insurance Charges"
    )

    fig, ax = plt.subplots(
        figsize=(8, 4)
    )

    sns.histplot(
        filtered_df["charges"],
        kde=True,
        ax=ax
    )

    ax.set_xlabel(
        "Insurance Charges"
    )

    ax.set_ylabel(
        "Frequency"
    )

    st.pyplot(fig)

    plt.close(fig)


    # BMI vs charges
    st.subheader(
        "BMI vs Insurance Charges"
    )

    fig, ax = plt.subplots(
        figsize=(8, 5)
    )

    sns.scatterplot(
        data=filtered_df,
        x="bmi",
        y="charges",
        hue="smoker",
        ax=ax
    )

    ax.set_title(
        "BMI vs Insurance Charges"
    )

    ax.set_xlabel("BMI")
    ax.set_ylabel("Insurance Charges")

    st.pyplot(fig)

    plt.close(fig)


    # Correlation
    st.subheader(
        "Correlation Matrix"
    )

    correlation = filtered_df[
        numeric_cols
    ].corr()

    fig, ax = plt.subplots(
        figsize=(7, 5)
    )

    sns.heatmap(
        correlation,
        annot=True,
        cmap="coolwarm",
        fmt=".2f",
        ax=ax
    )

    st.pyplot(fig)

    plt.close(fig)


# =========================================================
# TAB 2
# HYPOTHESIS TESTING
# =========================================================

with tab2:

    st.subheader(
        "Hypothesis Testing Lab"
    )


    categorical_factor = st.selectbox(
        "Select categorical factor",
        [
            "sex",
            "smoker",
            "region"
        ]
    )


    numerical_metric = st.selectbox(
        "Select numerical metric",
        [
            "charges",
            "age",
            "bmi",
            "children"
        ]
    )


    groups = filtered_df[
        categorical_factor
    ].dropna().unique()


    st.write(
        "Groups:",
        list(groups)
    )


    # Two group test
    if len(groups) == 2:

        group1 = filtered_df[
            filtered_df[categorical_factor] == groups[0]
        ][numerical_metric]

        group2 = filtered_df[
            filtered_df[categorical_factor] == groups[1]
        ][numerical_metric]


        if len(group1) > 3 and len(group2) > 3:

            shapiro1 = stats.shapiro(
                group1
            )

            shapiro2 = stats.shapiro(
                group2
            )

            levene_test = stats.levene(
                group1,
                group2
            )


            st.write(
                "Shapiro-Wilk p-value - Group 1:",
                shapiro1.pvalue
            )

            st.write(
                "Shapiro-Wilk p-value - Group 2:",
                shapiro2.pvalue
            )

            st.write(
                "Levene p-value:",
                levene_test.pvalue
            )


            # Select test
            if (
                shapiro1.pvalue >= 0.05
                and
                shapiro2.pvalue >= 0.05
            ):

                test_result = stats.ttest_ind(
                    group1,
                    group2,
                    equal_var=(
                        levene_test.pvalue >= 0.05
                    )
                )

                test_name = (
                    "Independent Samples t-test"
                )

            else:

                test_result = stats.mannwhitneyu(
                    group1,
                    group2,
                    alternative="two-sided"
                )

                test_name = (
                    "Mann-Whitney U Test"
                )


            st.write(
                "Test used:",
                test_name
            )

            st.write(
                "Test statistic:",
                round(
                    test_result.statistic,
                    4
                )
            )

            st.write(
                "p-value:",
                test_result.pvalue
            )


            if test_result.pvalue < 0.05:

                st.error(
                    "Reject H₀: Significant difference found."
                )

            else:

                st.success(
                    "Fail to Reject H₀: No significant difference found."
                )


    # ANOVA
    elif len(groups) >= 3:

        group_data = []

        for group in groups:

            data = filtered_df[
                filtered_df[categorical_factor] == group
            ][numerical_metric]

            group_data.append(data)


        anova_result = stats.f_oneway(
            *group_data
        )


        st.write(
            "Test used: One-Way ANOVA"
        )

        st.write(
            "F statistic:",
            round(
                anova_result.statistic,
                4
            )
        )

        st.write(
            "p-value:",
            anova_result.pvalue
        )


        if anova_result.pvalue < 0.05:

            st.error(
                "Reject H₀: Significant difference exists between groups."
            )

        else:

            st.success(
                "Fail to Reject H₀: No significant difference found."
            )


# =========================================================
# TAB 3
# LIVE PREDICTION
# =========================================================

with tab3:

    st.subheader(
        "Insurance Charge Prediction"
    )


    col1, col2 = st.columns(2)


    with col1:

        age = st.number_input(
            "Age",
            min_value=18,
            max_value=100,
            value=30
        )


        bmi = st.number_input(
            "BMI",
            min_value=10.0,
            max_value=60.0,
            value=25.0
        )


        children = st.number_input(
            "Children",
            min_value=0,
            max_value=10,
            value=0
        )


    with col2:

        sex = st.selectbox(
            "Sex",
            [
                "female",
                "male"
            ]
        )


        smoker = st.selectbox(
            "Smoker",
            [
                "no",
                "yes"
            ]
        )


        region = st.selectbox(
            "Region",
            [
                "northeast",
                "northwest",
                "southeast",
                "southwest"
            ]
        )


    # Prediction input
    input_data = pd.DataFrame(
        {
            "age": [age],
            "bmi": [bmi],
            "children": [children],
            "sex_male": [
                1 if sex == "male" else 0
            ],
            "smoker_yes": [
                1 if smoker == "yes" else 0
            ],
            "region_northwest": [
                1 if region == "northwest" else 0
            ],
            "region_southeast": [
                1 if region == "southeast" else 0
            ],
            "region_southwest": [
                1 if region == "southwest" else 0
            ]
        }
    )


    # Add constant
    input_data = sm.add_constant(
        input_data,
        has_constant="add"
    )


    # Match model columns
    input_data = input_data[
        model_columns
    ]


    # Get prediction
    prediction = model.get_prediction(
        input_data
    ).summary_frame(
        alpha=0.05
    )


    predicted_charge = prediction[
        "mean"
    ].iloc[0]


    st.metric(
        "Predicted Insurance Charge",
        f"${predicted_charge:,.2f}"
    )


    # Confidence interval
    st.write(
        "95% Confidence Interval"
    )

    st.write(
        f"${prediction['mean_ci_lower'].iloc[0]:,.2f} "
        f"to "
        f"${prediction['mean_ci_upper'].iloc[0]:,.2f}"
    )


    # Prediction interval
    st.write(
        "95% Prediction Interval"
    )

    st.write(
        f"${prediction['obs_ci_lower'].iloc[0]:,.2f} "
        f"to "
        f"${prediction['obs_ci_upper'].iloc[0]:,.2f}"
    )


    # Diagnostics
    st.subheader(
        "Residual Diagnostics"
    )


    fitted = model.fittedvalues
    residuals = model.resid


    # Residual vs fitted
    st.write(
        "Residuals vs Fitted Values"
    )

    fig, ax = plt.subplots(
        figsize=(8, 4)
    )

    ax.scatter(
        fitted,
        residuals
    )

    ax.axhline(
        0,
        linestyle="--"
    )

    ax.set_xlabel(
        "Fitted Values"
    )

    ax.set_ylabel(
        "Residuals"
    )

    ax.set_title(
        "Residuals vs Fitted Values"
    )

    st.pyplot(fig)

    plt.close(fig)


    # Q-Q plot
    st.write(
        "Q-Q Plot of Residuals"
    )

    fig, ax = plt.subplots(
        figsize=(8, 5)
    )

    sm.qqplot(
        model.resid,
        line="45",
        ax=ax
    )

    ax.set_title(
        "Q-Q Plot of Residuals"
    )

    st.pyplot(fig)

    plt.close(fig)


    # Jarque-Bera
    jb_test = stats.jarque_bera(
        model.resid
    )


    st.write(
        "Jarque-Bera Statistic:",
        round(
            jb_test.statistic,
            4
        )
    )

    st.write(
        "Jarque-Bera p-value:",
        jb_test.pvalue
    )


    if jb_test.pvalue < 0.05:

        st.warning(
            "Residuals are not normally distributed."
        )

    else:

        st.success(
            "Residuals are approximately normally distributed."
        )