# Netflix-Data-Analysis
Netflix data analysis and visualization using Python, Pandas, and Matplotlib.


#  Netflix Data Analysis & Visualization

A Python-based data analysis and visualization project using the **Netflix Titles dataset**.
This project uses **Pandas** for data loading and cleaning and **Matplotlib** for creating different visualizations from Netflix content data.

#  Project Overview

The project analyzes Netflix movies and TV shows and visualizes information such as:

* Movies vs TV Shows
* Content ratings
* Movie duration distribution
* Content released over the years
* Top 10 countries by number of shows
* Comparison of movies and TV shows released over the years

#  Technologies Used

* Python
* Pandas
* Matplotlib

#  Dataset

The dataset used in this project was obtained from **Kaggle**.

**Dataset:** Netflix Movies and TV Shows Dataset

The dataset contains information about Netflix titles, including:

* Title type (Movie / TV Show)
* Release year
* Rating
* Country
* Duration
* Other title-related information

The dataset is used for data cleaning, analysis, and visualization using **Pandas** and **Matplotlib**.


The dataset contains information about Netflix titles, including content type, release year, rating, country, and duration.

#  Data Cleaning

Missing values are removed from important columns:

```python
df = df.dropna(
    subset=["type", "release_year", "rating", "country", "duration"]
)
```

#  Visualizations

# 1. Movies vs TV Shows

A bar chart is used to compare the number of movies and TV shows available in the dataset.

# 2. Content Rating Distribution

A pie chart shows the percentage distribution of different content ratings.

# 3. Movie Duration Distribution

A histogram is used to analyze the distribution of movie durations in minutes.

# 4. Release Year Analysis

A scatter plot shows the number of Netflix titles released across different years.

# 5. Top 10 Countries

A horizontal bar chart displays the top 10 countries based on the number of shows.

# 6. Movies vs TV Shows Over the Years

Two line plots compare the number of movies and TV shows released across different years.

#  Project Structure

```text
netflix-data-analysis-matplotlib/
│
├── matplotlib_project.py
├── netflix_titles.csv
│
├── movies_vs_tvshows.png
├── content rating.png
├── movie_duration_histogram.png
├── release_yeasr scatter.png
├── top_10_ountry.png
├── movies_tvshows_comparision.png
│
└── README.md
```

#  How to Run

# 1. Clone the repository

```bash
git clone https://github.com/your-username/netflix-data-analysis-matplotlib.git
```

# 2. Go to the project folder

```bash
cd netflix-data-analysis-matplotlib
```

### 3. Install required libraries

```bash
pip install pandas matplotlib
```

# 4. Run the Python file

```bash
python matplotlib_project.py
```

The program will generate the visualizations and save them as PNG files.

#  Key Concepts Practiced

* Reading CSV files with Pandas
* Data cleaning
* Filtering DataFrames
* Value counting
* GroupBy operations
* Data transformation
* Bar charts
* Pie charts
* Histograms
* Scatter plots
* Line plots
* Saving Matplotlib figures

# 🎯 Purpose

This project was created to practice **Python data analysis and visualization** using a real-world dataset.



⭐ If you found this project useful, consider giving it a star!
