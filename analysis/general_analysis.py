import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
df = pd.read_csv("../scraping/books_clean.csv")

# Basic Statistics
num_books = df.shape[0]
num_ratings = df["rating"].value_counts().sort_index()
avg_price = df["price"].mean()
median_price = df["price"].median()
min_price = df["price"].min()
max_price = df["price"].max()

# Define cheap vs expensive books
median_price_threshold = df["price"].median()
df["price_category"] = df["price"].apply(lambda x: "Cheap" if x < median_price_threshold else "Expensive")
price_category_counts = df["price_category"].value_counts()

# Average price per rating
avg_price_per_rating = df.groupby("rating")["price"].mean()

# Most expensive & cheapest book per rating
max_prices = df.groupby("rating")["price"].max()
min_prices = df.groupby("rating")["price"].min()

# Print summary statistics
print(f"Total Books: {num_books}")
print("\nNumber of Books per Rating:")
print(num_ratings)
print(f"\nAverage Price: £{avg_price:.2f}")
print(f"Median Price: £{median_price:.2f}")
print(f"Min Price: £{min_price:.2f}")
print(f"Max Price: £{max_price:.2f}")
print("\nCheap vs Expensive Book Counts:")
print(price_category_counts)
print("\nAverage Price per Rating:")
print(avg_price_per_rating)
print("\nMost Expensive Books per Rating:")
print(max_prices)
print("\nCheapest Books per Rating:")
print(min_prices)

# Visualizations
plt.figure(figsize=(8,5))
sns.barplot(x=num_ratings.index, y=num_ratings.values, palette="viridis")
plt.xlabel("Book Rating (Stars)")
plt.ylabel("Number of Books")
plt.title("Number of Books per Rating")
plt.show()

plt.figure(figsize=(8,5))
sns.boxplot(x=df["rating"], y=df["price"], palette="coolwarm")
plt.xlabel("Book Rating (Stars)")
plt.ylabel("Book Price (£)")
plt.title("Price Distribution per Rating")
plt.show()

