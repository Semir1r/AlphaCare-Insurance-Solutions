# Weekly Project Tasks

This README outlines the tasks for the week, along with their objectives, key performance indicators (KPIs), and minimum essential steps for successful completion. The tasks are organized as follows:

## Task 1: Git and GitHub

### Objectives:
- Create a Git repository to host all project code.
- Implement Git version control and CI/CD using GitHub Actions.

### Key Performance Indicators (KPIs):
- Dev Environment Setup.
- Demonstrated relevant skills in version control and project management.

### Tasks:
1. **Repository Setup**:
   - Create a GitHub repository for the week.
   - Include a detailed README.
2. **Branch Management**:
   - Create a branch named `task-1`.
   - Commit changes at least three times a day with descriptive messages.
3. **Exploratory Data Analysis (EDA)**:
   - **Data Summarization**:
     - Calculate descriptive statistics for features such as `TotalPremium` and `TotalClaim`.
     - Confirm data types for categorical variables and dates.
   - **Data Quality Assessment**:
     - Identify missing values.
   - **Univariate Analysis**:
     - Plot histograms and bar charts.
   - **Bivariate/Multivariate Analysis**:
     - Analyze correlations between variables such as `TotalPremium` and `TotalClaims` by `ZipCode`.
   - **Visualization**:
     - Produce three insightful and visually appealing plots.
   - **Outlier Detection**:
     - Use box plots to detect outliers.
4. **CI/CD Integration**:
   - Set up a GitHub Actions workflow for CI/CD.

---

## Task 2: Data Version Control (DVC)

### Objectives:
- Use DVC for efficient and scalable data management.

### Key Performance Indicators (KPIs):
- Properly configured local remote storage.
- Versioned data managed effectively.

### Tasks:
1. **Environment Setup**:
   - Install DVC (`pip install dvc`).
   - Initialize DVC in the project directory (`dvc init`).
2. **Remote Storage Configuration**:
   - Create a local storage directory (`mkdir /path/to/your/local/storage`).
   - Add the storage as a DVC remote (`dvc remote add -d localstorage /path/to/your/local/storage`).
3. **Data Management**:
   - Track datasets with DVC (`dvc add <data.csv>`).
   - Commit `.dvc` files to the Git repository.
   - Push data to the local remote (`dvc push`).
4. **Branch Management**:
   - Create a branch named `task-2`.
   - Commit changes with descriptive messages.
5. **Branch Merge**:
   - Merge `task-1` into `main` via Pull Request (PR).

---

## Task 3: A/B Hypothesis Testing

### Objectives:
- Validate hypotheses using statistical testing.

### Key Performance Indicators (KPIs):
- Effective hypothesis testing and interpretation.
- Evidence-backed decision-making.

### Tasks:
1. **Branch Management**:
   - Create a branch named `task-3`.
   - Commit changes with descriptive messages.
2. **Hypothesis Testing**:
   - Null Hypotheses:
     - No risk differences across provinces.
     - No risk differences between zip codes.
     - No significant profit margin differences between zip codes.
     - No significant risk differences between women and men.
   - Select KPIs and segment data into control (Group A) and test (Group B).
   - Conduct statistical tests (e.g., chi-squared, t-tests, z-tests).
   - Analyze p-values to accept or reject hypotheses.
3. **Analysis and Reporting**:
   - Document findings and insights.
   - Interpret results within a business context.
4. **Branch Merge**:
   - Merge `task-2` into `main` via PR.

---

## Task 4: Statistical Modeling

### Objectives:
- Build and evaluate predictive models for `TotalPremium` and `TotalClaims`.

### Key Performance Indicators (KPIs):
- Effective model building and evaluation.
- Insightful feature importance analysis.

### Tasks:
1. **Branch Management**:
   - Create a branch named `task-4`.
   - Commit changes with descriptive messages.
2. **Data Preparation**:
   - Handle missing data.
   - Engineer new features.
   - Encode categorical variables.
   - Split data into training and testing sets (e.g., 80:20 ratio).
3. **Model Building**:
   - Implement Linear Regression, Random Forest, and XGBoost.
4. **Model Evaluation**:
   - Evaluate models using metrics like accuracy, precision, recall, and F1-score.
5. **Feature Importance**:
   - Use SHAP or LIME to analyze feature influence.
6. **Branch Merge**:
   - Merge `task-3` into `main` via PR.

---

## General Guidelines:
- Maintain consistent and descriptive commit messages.
- Use branches effectively to manage tasks.
- Leverage GitHub PRs for merging completed tasks into the main branch.
- Document insights and findings for all tasks in a clear and concise manner.
- Ensure all work is reproducible and well-documented for future reference.

## Prerequisites

1. Clone this repository:
   ```bash
   git clone <https://github.com/Semir1r/AlphaCare-Insurance-Solutions.git>
   cd <AlphaCare-Insurance-Solutions>
   
2. **Install the required dependencies**
   ```bash
    pip install -r requirements.txt