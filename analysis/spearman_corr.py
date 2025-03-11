# Measures monotonic relationships between two numeric variables

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("../scraping/books_clean.csv")

df["price_rank"] = df["price"].rank()
df["rating_rank"] = df["rating"].rank()

spearman_corr = df[["price_rank", "rating_rank"]].corr().iloc[0, 1]
print(f"Spearman Correlation: {spearman_corr:.2f}")

plt.figure(figsize=(8, 5))
sns.scatterplot(x=df["rating_rank"], y=df["price_rank"], alpha=0.5)
plt.xlabel("Book Rating Rank")
plt.ylabel("Book Price Rank")
plt.title(f"Price vs Rating (Spearman Correlation: {spearman_corr:.2f})")
plt.show()


