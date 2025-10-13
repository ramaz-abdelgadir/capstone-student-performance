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
#### student_id,
#### weekly_self_study_hours,
#### attendance_percentage,
#### class_participation,
#### total_score,
#### grade

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
Ethical, legal, and social responsibility are essential components of all data analytics work — particularly when handling information about students. This section outlines how privacy, bias, and fairness were considered throughout the project and how potential issues were addressed.

### Data Privacy and Anonymity

The dataset used (Student Performance Dataset) did not include any personally identifiable information (PII) such as student names, IDs, addresses, or contact details.

All analysis focused solely on anonymised attributes — such as study time, attendance, class participation, and grades — ensuring no individual student could be identified.

Data handling followed the principles of the UK General Data Protection Regulation (GDPR), which prioritises minimal data use and secure processing.

The dataset was stored locally in secure folders and not shared publicly without anonymisation.

### Bias and Fairness

Efforts were made to identify and minimise analytical bias. For example:

Statistical summaries and visualisations were reviewed to ensure no attribute (e.g., attendance or participation) was overrepresented or misinterpreted.

Hypotheses were tested using objective metrics (e.g., mean grade comparisons) rather than subjective assumptions about student behaviour.

When discussing relationships such as “higher attendance leads to better grades”, conclusions were carefully framed as correlations, not causations, to avoid misleading interpretations.

The analysis aimed to represent all study time and attendance levels fairly, ensuring balanced insight across the dataset.

### Legal and Social Implications

The analysis and dashboard were developed solely for educational and research purposes, not for real-world decision-making about actual students.

All content aligns with ethical academic practice and fair use of open data under Kaggle’s terms of use.

The project promotes data literacy and transparency by demonstrating how ethical analytics can support student success rather than penalise individuals.

### Responsible AI and Automation

Generative AI (ChatGPT) was used responsibly to assist in:

Writing documentation and explanations.

Debugging Power BI visuals and Python code.

Generating clear, unbiased narratives and summaries.

All AI-assisted outputs were reviewed, verified, and edited by the author to ensure factual accuracy and integrity.

The AI tools did not access or process private data; they were used only for design and learning support.


## 📊 Dashboard Design

The Power BI dashboard was designed to communicate insights about student performance clearly and interactively, enabling both technical users (data analysts, educators) and non-technical stakeholders (teachers, administrators) to explore key factors that influence academic outcomes.

The design follows the information hierarchy principle — starting from high-level KPIs on the Overview page and progressively allowing deeper analytical exploration through filters, drill-downs, and visual interactions.

##  Interactivity and Widgets

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

  * During the development and deployment of the Power BI dashboard, a few activation and interaction issues were encountered.
  * While testing predictive visuals, the “+” expand option in the Decomposition Tree did not appear.

  * If I had more time, I would have further refined the Power BI dashboard by addressing minor issues that occurred during the activation and publishing stages. Specifically:

I would explore alternative solutions for visuals that occasionally failed to load (particularly AI visuals such as the Decomposition Tree).

I would optimise data refresh automation and workspace configuration in the Power BI Service to ensure smoother deployment.

I would also test additional advanced features such as conditional formatting in KPIs, tooltips for better insight communication, and cloud-based collaboration options.

These enhancements would ensure the dashboard is more robust, automated, and ready for long-term use. Despite these challenges, the current dashboard successfully meets the main project objectives and demonstrates the ability to analyse, visualise, and interpret data effectively.

## Development Roadmap
During the development of the Student Performance Analysis project, several challenges were encountered, especially when integrating multiple data analysis tools and new learning topics:

* Time Constraints:
The most significant challenge was limited time. While the main goals were achieved, some advanced Power BI features and deeper statistical tests could not be fully explored. To manage this, the focus remained on building a functional and visually clear dashboard that demonstrated the core hypotheses effectively.

* New Concepts and Tools:
This project introduced several new areas — including Power BI’s DAX calculations, conditional columns, and AI visuals like the Decomposition Tree. At first, these were unfamiliar, but with guidance from tutorials, documentation, and AI assistance (ChatGPT and Copilot), the features were gradually mastered.

* Activation and Visual Issues in Power BI:
Occasional technical problems (e.g., visuals not loading, slicers freezing, and Pro account activation) were resolved through troubleshooting, reapplying data refreshes, and revisiting data model connections.

* Data Cleaning and Sampling:
The raw dataset originally contained over 1,000,000 rows, which slowed performance. This was resolved by sampling 10,000 rows, cleaning missing values, and optimising column data types for faster analysis.

Based on this project experience, several areas for professional growth have been identified:

### Power BI Advanced Features:
Deeper exploration of advanced DAX measures, dynamic tooltips, and drill-through pages to enhance interactivity.

#### Machine Learning Integration:
Extending the student performance analysis with Python machine learning models (e.g., Linear Regression or Decision Trees) to predict future grades based on attendance and study habits.

#### Automation & Cloud Deployment:
Learning to automate data refreshes using Power BI Service and linking the dashboard to cloud databases for real-time updates.

#### Improved Project Management:
Using GitHub Projects and issue tracking more effectively to manage workflow, commits, and feedback loops.

#### Enhanced Data Storytelling:
Developing stronger data narrative and visual design skills to communicate complex results to non-technical audiences.


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

Content Sources

Dataset:
The Student Performance Dataset was sourced from Kaggle
 and used for educational purposes under the dataset’s open-access license.
The dataset was modified and cleaned for analysis and dashboard creation.

Code References:

Python tutorials and snippets were adapted from official documentation for libraries such as:

Pandas Documentation

NumPy Documentation

Matplotlib Documentation

Seaborn Documentation

AI assistance (ChatGPT/Copilot) was used for ideation, code optimisation, visualisation design, and explanatory markdown text throughout the Jupyter Notebook and Power BI project.

Statistical test examples (mean, median, t-test, standard deviation, probability) were derived from open educational sources such as W3Schools and GeeksforGeeks for Python data analysis practice.

Power BI & DAX:

Official Microsoft Learn resources were referenced for DAX syntax and Power BI dashboard design.

Conditional column logic and KPI creation were guided by Power BI community examples and tutorials.



Conclusion & Future Work
1️⃣ Project Summary

This project successfully demonstrated the end-to-end process of data analysis — from data cleaning and transformation to visualisation and insight generation — using the Student Performance Dataset.
Through the combination of Python-based preprocessing and a Power BI interactive dashboard, meaningful insights were derived about how study time, attendance, and class participation relate to overall student achievement.

The dashboard allows users to explore performance patterns, compare groups, and validate hypotheses through clear visuals such as:

KPI cards for key metrics (average grade, attendance, study hours, pass rate).

Bar and scatter plots showing the relationship between study time, participation, and grades.

Donut charts and decomposition trees providing overall summaries and predictive insights.

The project also met its primary objective — to use data analytics techniques to support evidence-based decision-making in education and demonstrate how insights can improve student engagement and academic outcomes.

Future Work and Improvements

If given additional time and resources, several enhancements could be implemented to extend the project’s scope and impact:

#### Machine Learning Models:
Build predictive models (e.g., Linear Regression, Decision Tree, or Random Forest) to forecast student grades and identify at-risk learners.

#### Automated Dashboard Updates:
Connect Power BI to live databases or cloud sources (e.g., Azure SQL or SharePoint) to refresh the dashboard automatically.

#### Deeper Statistical Analysis:
Conduct hypothesis testing and correlation analysis to quantify the strength of each relationship and validate findings with greater accuracy.

#### Enhanced Interactivity:
Add dynamic filters, tooltips, and drill-through pages for department-level or term-based comparisons.

#### Expanded Dataset:
Integrate additional student attributes such as gender, study program, or school region to widen the analytical perspective.

#### Ethical Monitoring:
Continue ensuring fairness, bias mitigation, and compliance with educational data privacy standards.