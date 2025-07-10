# 📊 User Post Analysis using Python

This project is a basic data analysis task performed on a dataset of social media posts (Reels, Carousels, etc.). The dataset includes metrics like comments and likes per post. The project includes data cleaning, preprocessing, visualization, and insights generation using Python and libraries such as Pandas, Matplotlib, and Seaborn.

---

## 📁 Dataset Overview

The dataset (`posts.csv`) contains the following columns:

- `Post_id`: Unique ID of each post
- `Post_Type`: Type of post (e.g., Reel, Carousel)
- `comments`: Number of comments
- `likes`: Number of likes

---

## 🔧 Technologies Used

- Python 3.x
- Pandas
- Seaborn
- Matplotlib
- VS Code
- Git & GitHub

---

## 🧼 Preprocessing Steps

- Removed irrelevant `Post_id`
- Checked and removed duplicates
- Verified missing values
- Applied One-Hot Encoding on `Post_Type`
- Saved the cleaned data as `cleaned_posts.csv`

---

## 📊 Data Visualization

The following visualizations were performed:
- Count of each `Post_Type`
- Boxplot of likes per `Post_Type`
- Boxplot of comments per `Post_Type`
- Scatterplot showing relationship between `likes` and `comments`

---

## 📈 Insights

- Reels received more likes on average than Carousels.
- Some Reels with high comments didn’t have proportionally high likes.
- Carousels showed more consistent engagement (lower outliers).

---

## 📁 Files Included

| File Name             | Description                           |
|-----------------------|---------------------------------------|
| `test.py`         | Python script for data analysis       |
| `posts.csv`           | Raw dataset                           |
| `cleaned_posts.csv`   | Cleaned & encoded dataset             |
---

## 🙋‍♀️ Author

**Jeevitha A**  
B.Tech (Information Technology), 3rd Year

---

## 📌 License

This project is intended for academic use only.

---

## 🚀 How to Run

1. Clone this repo:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
