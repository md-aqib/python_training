import pandas as pd

# 1. Load the CSV file
df = pd.read_csv('phone_dataset.csv')

# 2. Print the first 5 rows
print("First 5 rows:")
print(df.head())

# 3. Get the shape of the data
print("\nShape of the data (rows, columns):")
print(df.shape)

# 4. Get information about the data
print("\nInformation about the data:")
print(df.info())

# 5. Check for null values
print("\nNull values in each column:")
print(df.isnull().sum())

# 6. Replace null values in rating column with mean
if 'rating' in df.columns:
    mean_rating = df['rating'].mean()
    df['rating'].fillna(mean_rating, inplace=True)

# 7. Replace null values in os column with mode
if 'os' in df.columns:
    mode_os = df['os'].mode()[0]
    df['os'].fillna(mode_os, inplace=True)

# 8. Check for duplicated values
print("\nDuplicated rows:")
print(df.duplicated().sum())

# 9. Replace '?' in entire DataFrame with empty string ''
df.replace('?', '', inplace=True)

# 10. Check the data types of the columns
print("\nData types of the columns:")
print(df.dtypes)

# 11. Replace ',' in price column and convert to int
if 'price' in df.columns:
    df['price'] = df['price'].astype(str).str.replace(',', '')  # remove commas
    df['price'] = df['price'].astype(int)  # convert to integer

# Final check
print("\nCleaned data (first 5 rows):")
print(df.head())
