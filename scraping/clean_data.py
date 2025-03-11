import pandas as pd

input_file = "books_raw.csv"
output_file = "books_cleaned.csv"

def clean_data(input_file, output_file):
    df = pd.read_csv(input_file)
    
    df["price"] = df["price"].str.replace("£", "").astype(float)
    
    rating_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
    df["rating"] = df["rating"].map(rating_map)
    
    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    clean_data(input_file, output_file)