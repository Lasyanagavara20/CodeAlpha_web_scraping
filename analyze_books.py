import pandas as pd
import matplotlib.pyplot as plt
import re

# Load the CSV file
df = pd.read_csv("all_books.csv")

# Step 1: View raw price samples
print("Sample raw price values:")
print(df['Price'].head(10))
print("Unique values (raw):", df['Price'].unique()[:10])

# Step 2: Clean price using regex
def clean_price(val):
    if isinstance(val, str):
        val = re.sub(r"[^\d.]", "", val)  # Remove all non-digit characters except .
        try:
            return float(val)
        except:
            return None
    return None

df['Price'] = df['Price'].apply(clean_price)

# Step 3: Show cleaned prices and average
print("\nCleaned price sample:")
print(df['Price'].head())
print("Average price: £", round(df['Price'].mean(), 2))

# Step 4: Check bad rows (if any)
print("\nBad rows with missing or bad prices:")
print(df[df['Price'].isna()])

# Step 5: Plot price distribution
plt.figure(figsize=(8, 5))
plt.hist(df['Price'].dropna(), bins=20, color='skyblue', edgecolor='black')
plt.title('Book Price Distribution')
plt.xlabel('Price (£)')
plt.ylabel('Number of Books')
plt.grid(True)
plt.tight_layout()
plt.savefig("price_distribution.png")
plt.show()

# Step 6: Top 10 Most & Least Expensive Books
print("\n💰 Top 10 Most Expensive Books:")
print(df.sort_values(by="Price", ascending=False)[['Title', 'Price']].head(10))

print("\n🪙 Top 10 Cheapest Books:")
print(df.sort_values(by="Price")[['Title', 'Price']].head(10))

#Rating Distribution
print("\n⭐ Rating Distribution:")
print(df['Rating'].value_counts())

#Plot rating distribution
plt.figure(figsize=(6, 4))
df['Rating'].value_counts().plot(kind='bar', color='orange', edgecolor='black')
plt.title('Book Ratings')
plt.xlabel('Rating')
plt.ylabel('Number of Books')
plt.grid(axis='y')
plt.tight_layout()
plt.show()
# Count availability
print("\n📦 Book Availability:")
print(df['Availability'].value_counts())

# Optional: Plot availability
plt.figure(figsize=(5, 4))
df['Availability'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['#90ee90', '#ffcccb'])
plt.title('Availability of Books')
plt.ylabel('')
plt.tight_layout()
plt.show()
# Export cleaned data to Excel
df.to_excel("cleaned_books_data.xlsx", index=False)
print("\n📁 Cleaned data saved as 'cleaned_books_data.xlsx'")


