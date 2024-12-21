## Objective

Analyze the Spotify dataset to uncover insights on song popularity, artist trends, and track characteristics. This project involves data cleaning, loading the prepared data into an SQL database, and building a Power BI dashboard to visualize music data insights.

---

## Project Overview

### 1. Dataset Processing

**Task**: Prepare the Spotify dataset for analysis.

**Requirements**:

- Use Python to load the dataset into a pandas DataFrame.
- Handle missing values and standardize formats for numerical and categorical fields (e.g., song duration, popularity scores, genres).
- Create derived columns if needed (e.g., categorizing song lengths, popularity tiers).
- Save the cleaned dataset, ready for SQL loading.

---

### 2. SQL Database Integration

**Task**: Store the processed data in an SQL database.

**Requirements**:

- Set up an SQL database with tables representing different aspects, such as `song_details`, `artist_info`, and `track_metrics`.
- Use Python (e.g., `SQLAlchemy` or pandas `to_sql`) to load the cleaned data into SQL tables.
- Ensure the database supports queries for analyzing song popularity, artist trends, and song characteristics (such as duration and genre).

---

### 3. Power BI Dashboard-

Task: Create a Power BI dashboard connected to the SQL database.

Requirements:

- Connect Power BI to the SQL database.
- Design visualizations to provide insights such as:
    - Top artists and songs by popularity.
    - Trends in song features (e.g., duration, tempo, energy).
    - Popular genres and their characteristics.
- Ensure the dashboard is interactive, with filters for date ranges, artists, and genres.

---

4. Real-Time Updates

Task: Enable real-time updates in Power BI for the SQL database.

**Requirements**:

- Configure Power BI to refresh periodically to capture any new data added to the SQL database.
- Ensure data consistency between the SQL database and Power BI dashboard.

 5. GitHub Repository



**Requirements**:

- Create a GitHub repository with the following:
    - **Python Code**: Scripts for data processing and SQL loading.
    - **Documentation**: A README file with project details, setup instructions, and descriptions of each step.
    - **SQL Schema**: SQL code for setting up the database schema, including table creation and data integrity rules.
