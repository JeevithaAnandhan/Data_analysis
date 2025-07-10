# Step 1: Load and explore the dataset
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the CSV file (replace 'posts' with your exact file name if needed)
df = pd.read_csv('posts.csv')  # or 'posts.csv'

# Display the first 5 rows
print("📄 First 5 rows of the dataset:")
print(df.head())

# Check the column names
print("\n🧾 Columns in the dataset:")
print(df.columns)

# Display basic info: data types, non-null values, memory usage
print("\nℹ️ Dataset Info:")
print(df.info())

# Summary statistics for numeric and object columns
print("\n📊 Summary statistics:")
print(df.describe(include='all'))
# Step 2: Clean the data

# Drop Post_id since it's just an identifier
df.drop(columns=['Post_id'], inplace=True)

# Check for duplicates (if any)
df.drop_duplicates(inplace=True)

# Check again for null values (though you don't have any)
print("\n✅ Missing Values After Cleaning:")
print(df.isnull().sum())

# Encode Post_Type using one-hot encoding
df_encoded = pd.get_dummies(df, columns=['Post_Type'], drop_first=True)

print("\n📄 Cleaned and Encoded Data:")
print(df_encoded.head())
sns.countplot(x='Post_Type', data=df)
plt.title("Count of Each Post Type")
plt.xlabel("Post Type")
plt.ylabel("Number of Posts")
plt.show()

# Likes vs Post Type
sns.boxplot(x='Post_Type', y='likes', data=df)
plt.title("Likes Distribution by Post Type")
plt.show()

# Comments vs Post Type
sns.boxplot(x='Post_Type', y='comments', data=df)
plt.title("Comments Distribution by Post Type")
plt.show()

# Likes vs Comments
sns.scatterplot(x='comments', y='likes', hue='Post_Type', data=df)
plt.title("Comments vs Likes")
plt.xlabel("Comments")
plt.ylabel("Likes")
plt.show()
df_encoded.to_csv("cleaned_posts.csv", index=False)
print("✅ Cleaned file saved as 'cleaned_posts.csv'")



