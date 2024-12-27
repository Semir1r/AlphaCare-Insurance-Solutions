# AlphaCare Insurance Analysis

This repository hosts the code and data for analyzing AlphaCare Insurance data. The project focuses on comprehensive Exploratory Data Analysis (EDA) and utilizes Data Version Control (DVC) to ensure efficient tracking of data versions and reproducibility.

## Branches
- `main`: The main branch containing the finalized and reviewed code.
- `task-1`: A branch dedicated to the analysis performed on day 1.
- `task-2`: A branch for subsequent tasks and analyses.

---

## Task-1: Exploratory Data Analysis (EDA)

### Steps:
1. **Data Summarization**
   - **Descriptive Statistics**: Calculated measures such as mean, standard deviation, and variability for numerical features (e.g., `TotalPremium`, `TotalClaim`).
   - **Data Structure**: Reviewed and confirmed data types for all columns.

2. **Data Quality Assessment**
   - Checked for and documented missing values.

3. **Univariate Analysis**
   - Plotted histograms for numerical features.
   - Used bar charts to analyze distributions of categorical columns.

4. **Bivariate and Multivariate Analysis**
   - Explored correlations between `TotalPremium` and `TotalClaims` across `ZipCode` using scatter plots and correlation matrices.

5. **Data Comparison**
   - Analyzed trends in insurance cover type, premium, and auto make over geographical locations.

6. **Outlier Detection**
   - Used box plots to detect outliers in numerical features.

7. **Visualization**
   - Created three visually appealing plots that summarize insights from the EDA.

---

## Task-2: Data Version Control (DVC)

### Steps:
1. **Install DVC**
   - Installed DVC using `pip install dvc`.

2. **Initialize DVC**
   - Initialized DVC in the project directory with `dvc init`.

3. **Set Up Local Remote Storage**
   - Created a local storage directory: `/path/to/your/local/storage`.
   - Added it as a DVC remote: `dvc remote add -d localstorage /path/to/your/local/storage`.

4. **Add and Track Data**
   - Added datasets to the project directory.
   - Tracked datasets using `dvc add <data.csv>`.

5. **Commit Changes**
   - Committed `.dvc` files (metadata about the tracked data) to the Git repository.

6. **Push Data to Local Remote**
   - Pushed tracked data to the local remote storage using `dvc push`.

7. **Version Control**
   - Created and managed different versions of the data.

---

## Repository Guidelines

- Commit code changes at least three times daily with descriptive messages.
- Use Pull Requests (PRs) to merge changes into the `main` branch.

---

## Prerequisites

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   
2. **Install the required dependencies**
   ```bash
    pip install -r requirements.txt