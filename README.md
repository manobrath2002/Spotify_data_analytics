## Project Objective

Analyze the Spotify dataset to uncover insights on song popularity, artist trends, and track characteristics. This project involves data cleaning, loading the prepared data into an SQL database, and building a Power BI dashboard to visualize music data insights.

---

## Project Structure

### 1. Dataset Processing

- Use Python to load the dataset into a pandas DataFrame.
- Handle missing values and standardize formats for numerical and categorical fields (e.g., song duration, popularity scores, genres).
- Create derived columns if needed (e.g., categorizing song lengths, popularity tiers).
- Save the cleaned dataset, ready for SQL loading.

---

### 2. SQL Database Integration

- Set up an SQL database with tables representing different aspects, such as `song_details`, `artist_info`, and `track_metrics`.
- Use Python (e.g., `SQLAlchemy` or pandas `to_sql`) to load the cleaned data into SQL tables.
- Ensure the database supports queries for analyzing song popularity, artist trends, and song characteristics (such as duration and genre).

---

### 3. Power BI Dashboard

- Connect Power BI to the SQL database.
- Design visualizations to provide insights such as:
    - Top artists and songs by popularity.
    - Trends in song features (e.g., duration, tempo, energy).
    - Popular genres and their characteristics.
- Ensure the dashboard is interactive, with filters for date ranges, artists, and genres.

---

**4. Real-Time Updates**

- Configure Power BI to refresh periodically to capture any new data added to the SQL database.
- Ensure data consistency between the SQL database and Power BI dashboard.

 **5. GitHub Repository**

- Create a GitHub repository with the following:
    - **Python Code**: Scripts for data processing and SQL loading.
    - **Documentation**: A README file with project details, setup instructions, and descriptions of each step.
    - **SQL Schema**: SQL code for setting up the database schema, including table creation and data integrity rules.
 
## Key Features  
- **Data Cleaning and Processing**: Ensure high data quality for actionable insights.  
- **SQL Database Integration**: Centralized data storage for efficient access and manipulation.  
- **Interactive Dashboard**: Visualize critical metrics with user-friendly, dynamic reports.  
- **Real-Time Updates**: Stay up-to-date with live data changes for accurate decision-making.  

---

## Technologies Used  
- **Python**: Data cleaning and preprocessing.  
- **MySQL**: Database design and management.  
- **Power BI**: Data visualization and dashboard creation.
---
 ### 
 ![Screenshot 2024-12-22 002635](https://github.com/user-attachments/assets/0e7bcd58-6d41-43d2-bb30-7f154d8d0c25)
 ###  
 ![Screenshot 2024-12-22 002656](https://github.com/user-attachments/assets/a74cdc51-fc49-469a-a5a3-ebdcbc22f65c)


