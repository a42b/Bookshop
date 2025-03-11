# Do higher ratings lead to higher book prices

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("../scraping/books_clean.csv")

pearson_corr = df[["rating", "price"]].corr().iloc[0, 1]
print(f"Pearson Correlation: {pearson_corr:.2f}")

plt.figure(figsize=(8, 5))
sns.regplot(x=df["rating"], y=df["price"], scatter_kws={"alpha": 0.5}, line_kws={"color": "red"})
plt.xlabel("Book Rating (Stars)")
plt.ylabel("Book Price (£)")
plt.title(f"Price vs Rating (Pearson Correlation: {pearson_corr:.2f})")
plt.show()
