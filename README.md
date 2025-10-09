#  Student Performance Project

**Student Performance** is a comprehensive data analysis tool designed to streamline data exploration, analysis, and visualisation. The tool supports multiple data formats and provides an intuitive interface for both novice and expert data scientists.

# ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)


## Dataset Content
* The dataset used for this project is titled “Student Performance Dataset”, sourced from Kaggle, https://www.kaggle.com/datasets/nabeelqureshitiii/student-performance-dataset?resource=download&select=student_performance.csv It contains anonymised records of students’ academic behaviour and performance, collected to understand factors influencing achievement.

The dataset is cleaned, structured, and stored in CSV format under the project’s Data/cleaned/ folder (student_performance_cleaned.csv).
Each record represents one student, with attributes describing their learning habits, attendance, engagement, and academic results.

Dataset Size and Sampling

Original dataset: 1,000,000 rows

Reason for sampling:
The raw dataset contained 1 million records, which caused long processing and loading times during data transformation and visualisation in Power BI and Jupyter Notebook.

Solution:
A stratified random sample of 10,000 rows (1%) was extracted to maintain a balanced representation of different grades and participation levels while optimising performance.

Final working dataset: 10,000 rows × 6 columns (~2 MB)
The columns are:
### student_id,
### weekly_self_study_hours,
### attendance_percentage,
### class_participation,
### total_score,
### grade

Storage location:

Raw dataset → Data/1_raw/student_performance.csv

Cleaned and sampled dataset → Data/cleaned/student_performance_sample.csv

## Business Requirements
* The purpose of this project is to analyse the academic behaviour and performance of students to help educators identify the factors that most influence final grades.
By exploring relationships between study habits, attendance, participation, and achievement, the project provides data-driven insights that can guide teaching strategies, student support, and academic planning.

Primary Business Objectives

1. Understand academic drivers: Determine how self-study hours, attendance, and class participation influence student grades.

2. Predict academic outcomes: Build statistical and machine-learning models to estimate student performance and identify at-risk learners.

3. Support data-informed decisions: Present actionable insights in an interactive Power BI dashboard for teachers and administrators.

4. Encourage student engagement: Use insights to design interventions that promote better attendance, active participation, and consistent study habits.

## Hypothesis and how to validate?
1. Students with higher study time will achieve higher average scores.

2. Students who participate more in class have higher education levels tend to perform better.

3. There is a significant difference in average scores between students with and without good attendance level.

## Validation approach:

* Method: Correlation and group comparison.

* Python: Compute correlation between weekly_self_study and grade, and visualise with scatterplot or boxplot.

* Power BI: Create a line or bar chart with weekly_self_study on the axis and average grade as values.

* Method: Correlation and grouped mean comparison (ANOVA if participation is categorical).

* Python: Compare mean grade across different participation levels.

* Power BI: Use a clustered column chart with class_participation as axis and average grade as values.

* Method: Correlation and independent samples T-test (if you categorise attendance).

* Python: Categorise attendance (e.g., ≥90 % = “Good”, <90 % = “Low”) and test grade differences.

* Power BI: Compare average grades by attendance level using a column chart.

## Project Plan
### Overview

The project followed a structured data analytics lifecycle, starting from data acquisition to insight generation and dashboard design.
Each stage was designed to ensure data accuracy, reproducibility, and alignment with business goals — identifying key behavioural factors influencing student achievement.

### 1. Data Collection

The dataset was sourced from Kaggle’s Student Performance Dataset, containing 1 million records of anonymised student data.

The raw file (student_performance.csv) was stored in the repository under Data/1_raw/.

### 2. Data Processing (Cleaning & Preparation)

To ensure efficiency and accuracy, an ETL pipeline was built in Python (Jupyter Notebook).

#### Key steps:

1. Removed missing or duplicate rows.

2. Standardised column names.

3. Created derived features:

4. StudyTimeBand (grouped weekly hours)

ParticipationLevel (Low–Very High)

attendance_level (Good/Low)

Validated column types (decimal, text, category).

Created a stratified random sample of 10,000 rows (1%) to reduce processing time while maintaining balanced grade distribution.

### 3. Data Analysis & Exploration (EDA)

Exploratory Data Analysis (EDA) was conducted to uncover trends and relationships among variables.

Techniques applied:

Descriptive statistics (mean, median, standard deviation).

Correlation analysis (between study time, participation, and grades).

Visualisation using bar charts, scatter plots, and boxplots.

Hypothesis testing for statistical significance.

Examples of visualisations:

Average Grade by Study Time Band

Average Grade by Attendance Level

Participation Level vs Grade Distribution

 Tools used:
Power BI (for visuals), Python (Matplotlib, Seaborn for validation plots)

### 4. Hypothesis Validation

Three hypotheses were defined and validated using statistical and visual methods.

### 5. Dashboard Design & Interpretation

An interactive dashboard was built in Power BI to communicate insights to both technical and non-technical audiences.

Key dashboard pages:

Overview Page: Summary KPIs (average grade, attendance rate, study time).

Behavioural Insights Page: Study time, attendance, and participation comparisons.

Trends Page: Correlation visuals and performance insights.

The dashboard visually demonstrates how student engagement factors influence achievement.

 Tool used:
Power BI (with filters, slicers, cards, and clustered column charts)

### 6. Reflection and Interpretation

After analysis, insights were interpreted to support educational recommendations:

Encouraging consistent attendance and regular self-study.

Promoting classroom participation to improve performance outcomes.

Limitations, such as data sampling size and generalisation scope, were acknowledged, and alternative approaches (e.g., using regression models or larger data samples) were suggested for future work.

## The rationale to map the business requirements to the Data Visualisations
Each business requirement in this project was translated into specific, evidence-based data visualisations.
The goal was to ensure that every visual provided a direct and actionable insight supporting data-driven decision-making.
The following table and explanations describe how and why each chart or visual directly supports the project’s analytical goals.

| **Business Requirement (BR)**                                                      | **Question / Hypothesis**                                           | **Data Visualisation(s)**                                                                                                                 | **Rationale / Insight Gained**                                                                                                                                 |
| ---------------------------------------------------------------------------------- | ------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **BR-01:** Determine whether higher weekly self-study hours lead to higher grades. | *Students who spend more time on self-study achieve higher grades.* | **Scatter plot / Line chart**: `weekly_self_study` (X-axis) vs. `grade` (Y-axis).<br>**Trendline** to show correlation.                   | Clearly shows whether study time has a positive or flat relationship with grade. Helps educators identify the ideal study range for improvement.               |
| **BR-02:** Understand the impact of attendance on academic performance.            | *Students with higher attendance achieve better grades.*            | **Column chart**: Average `grade` by `attendance_level` (“Good” vs “Low”).<br>**Card visual** for average grade difference.               | Allows direct comparison of grade means between good and poor attendance groups. Makes statistical T-test result visually intuitive.                           |
| **BR-03:** Evaluate whether classroom participation influences grades.             | *Students who participate more in class tend to perform better.*    | **Clustered bar chart**: `class_participation` vs. average `grade`.<br>**Boxplot** to show grade variability across participation levels. | Highlights whether engagement (participation score) consistently corresponds to higher grades. Identifies performance spread among active vs passive students. |
| **BR-04:** Identify which factors together most influence student grades.          | *Combined impact of study, attendance, and participation.*          | **Correlation heatmap / Decomposition tree** showing `grade` vs. predictors.<br>**Scatter matrix** (optional).                            | Displays multivariate relationships to identify key predictors driving performance. Enables data-driven prioritisation for interventions.                      |
| **BR-05:** Provide an overview of key performance indicators (KPIs).               | *Summarise overall academic trends and averages.*                   | **Card visuals:** Average Grade, Average Attendance %, Average Study Hours.<br>**Donut chart:** Grade distribution.                       | Offers management a quick snapshot of overall student performance and progress. Simplifies complex analytics into clear KPIs for reporting.                    |


## Analysis techniques used
1. The analysis followed a logical progression, ensuring clarity and reproducibility:

2. Data Cleaning & Preparation → Ensured dataset accuracy and completeness (handled missing values, encoded variables).

2. Exploratory Data Analysis (EDA) → Used visuals and summary statistics to discover patterns and correlations.

3. Hypothesis Testing → Used statistical methods (T-test, ANOVA) to confirm or reject assumptions.

4. Predictive Modelling → Applied regression and decision tree models to quantify and predict performance outcomes.

5. Segmentation (Clustering) → Grouped students by similar learning patterns for actionable insights.

6. Visual Communication → Presented findings through Power BI for stakeholder interpretation.

Justification:
This structured approach mirrors the CRISP-DM model and allows each phase to build logically on the previous one — from understanding the problem to delivering interpretable, evidence-based results.

## Reflection:
Generative AI acted as a collaborative assistant — helping to speed up development and improve code quality — but human oversight remained essential to ensure context accuracy, ethical integrity, and data validity.

## Ethical considerations
Ethical, legal, and social responsibility are essential components of all data analytics work — particularly when handling information about students.
This section outlines how privacy, bias, and fairness were considered throughout the project and how potential issues were addressed.

## Dashboard Design
It’s tailored to your Student Performance dataset (student_id, weekly_self_study, attendance, class_participation, grade) and describes the visuals, layout, interactivity, and communication rationale for both technical and non-technical audiences.

### 📊 Dashboard Design

The Power BI dashboard was designed to communicate insights about student performance clearly and interactively, enabling both technical users (data analysts, educators) and non-technical stakeholders (teachers, administrators) to explore key factors that influence academic outcomes.

The design follows the information hierarchy principle — starting from high-level KPIs on the Overview page and progressively allowing deeper analytical exploration through filters, drill-downs, and visual interactions.

### Interactivity and Widgets

Slicers / Filters: Enable users to dynamically view performance based on attendance or participation levels.

Buttons: Navigate between pages and reset filters.

Tooltips: Provide contextual explanations of metrics when hovering over visuals.

Cards: Summarise key KPIs such as Average Grade or Correlation Score for instant insight.

Custom Themes: Use consistent colour schemes (blue for study, green for attendance, orange for participation) to aid comprehension.

## Unfixed Bugs
Throughout the project, several minor issues and limitations were identified.
Where possible, workarounds were implemented — however, some remain unfixed due to framework constraints or deliberate prioritisation of higher-value tasks.
* my notebook was using the Agg backend. I had to switch to the  inline backend by the following code:
 #### %matplotlib inline
 #### import matpoltlib
 #### print("backend:", matplotlib.get_backend)

  * when trying to push any updates the notebook is trying to find the data file but can't locate it because the working directory is not set correctly. To fix this Co Pilot helped by first checking the current state and then updating the path detection logic.

## Development Roadmap
* What challenges did you face, and what strategies were used to overcome these challenges?
* What new skills or tools do you plan to learn next based on your project experience? 

## Deployment
### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. From the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.


## Main Data Analysis Libraries
* Pandas

Purpose: Data cleaning, manipulation, and analysis.

* NumPy

Purpose: Numerical operations and array-based calculations.

* Matplotlib

Purpose: Basic plotting and custom visualisation design.

* Seaborn

Purpose: Advanced visualisation and statistical plots.

* SciPy

Purpose: Hypothesis testing and advanced statistical analysis.

* Scikit-learn

Purpose: Machine learning modelling and evaluation.

* Plotly (Optional for Power BI / Jupyter Integration)

Purpose: Interactive charts for data exploration and integration with Power BI or HTML dashboards.

* Power BI (External Tool)

Purpose: Interactive visualisation and dashboard development.


## Credits 

* In this section, you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism. 
* You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign-Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

- The photos used on the home and sign-up page are from This Open-Source site
- The images used for the gallery page were taken from this other open-source site



## Acknowledgements (optional)
* Thank the people who provided support through this project.
