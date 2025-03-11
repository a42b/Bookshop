# Measures the strength and direction of the ordinal association between two numeric variables.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("../scraping/books_clean.csv")

kendall_corr = df[["rating", "price"]].corr(method="kendall").iloc[0, 1]
print(f"Kendall's Tau Correlation: {kendall_corr:.2f}")

plt.figure(figsize=(8, 5))
sns.regplot(x=df["rating"], y=df["price"], scatter_kws={"alpha":0.5}, line_kws={"color":"red"})
plt.xlabel("Book Rating (Stars)")
plt.ylabel("Book Price (£)")
plt.title(f"Price vs Rating (Kendall's Tau Correlation: {kendall_corr:.2f})")
plt.show()
