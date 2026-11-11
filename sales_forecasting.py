#                                                LOADING DATA


import pandas as pd #for handling dataset
import numpy as np #for mathematical calculations
import matplotlib.pyplot as plt #for making graphs
import seaborn as sns # for Statistical graphs
from google.colab import drive
import pandas as pd

drive.mount('/content/drive')
df = pd.read_excel("/content/drive/MyDrive/Online Retail.xlsx")

print("Dataset loaded successfully!")
######################################################################################################################################################################################################################################


#                                                         DATA UNDERSTANDING + EDA


#############################################################################################################################################################################
df.head() #it will display the first five row of dataset
print("row, column:", df.shape) #it will give tuple(row,column)
df.info() #it will give the information about column names,data types,non-null counts,etc
df.describe() #statistical information of Numerical columns that help to identify outliers
print(df.columns.tolist()) #we get column names in list form
missing_values = df.isnull().sum() #count missing values

print(missing_values)
missing_percentage = (df.isnull().sum() / len(df)) * 100
print(missing_percentage.round(2))
#how much percent values are missing
duplicate_count = df.duplicated().sum() # help to count the duplicate values

print("Total Duplicate Rows:", duplicate_count)
#Duplicate records can lead to double counting of transactions.
# How many different customers, products, and countries are in our data.

print("Unique customers:", df["CustomerID"].nunique())
print("Unique products:", df["StockCode"].nunique())
print("Unique countries:", df["Country"].nunique())# We check negative and zero quantities to find returns or invalid sales records in the data.
# Negative quantity signifies items were returned/cancelled.
# Zero quantity signifies no item was actually sold, so it is generally treated as an invalid/non-sale record.

print("Negative quantities before removing cancellations:", (df["Quantity"] < 0).sum())
print("Zero quantities before removing cancellations:", (df["Quantity"] == 0).sum())
cancelled_rows = df[df["InvoiceNo"].astype(str).str.startswith("C")]

print("Cancellation rows:", len(cancelled_rows))
print("Unique cancelled invoices:", cancelled_rows["InvoiceNo"].nunique())
# We check zero or negative UnitPrice to find invalid price records.
# Because a product normally should not have a negative price or a zero selling price.

print("Zero/negative UnitPrice:", (df["UnitPrice"] <= 0).sum())
# Plotting Distribution of Unit Price
plt.figure(figsize=(8, 4))

plt.hist(df["UnitPrice"], bins=50)

plt.xlabel("Unit Price")
plt.ylabel("Frequency")
plt.title("Distribution of Unit Price")

plt.show()
#                                           INSIGHTS FROM THE GRAPH

# Most UnitPrices are very close to 0
# The data has a very wide range of prices, with some extremely large values.
# There are also some negative/zero prices, which we identified separately as invalid records.
# The distribution is highly skewed, meaning a small number of extreme prices are pulling the graph far to the right.
# These extreme values can make analysis difficult, so we will handle invalid prices during data cleaning.
# Plotting Distribution of Quantity
plt.figure(figsize=(8, 4))

plt.hist(df["Quantity"], bins=50)

plt.xlabel("Quantity")
plt.ylabel("Frequency")
plt.title("Distribution of Quantity")

plt.show()
#                                           INSIGHTS FROM THE GRAPH

# Most quantities are close to 0,
# The quantity values have a very large range, with some extremely high and low values.
# There are negative quantities, which can represent returns/cancellations.
# There are some very large positive quantities, which are unusual compared with most transactions.
# So the quantity distribution is highly skewed and contains some extreme values.
# This is why we need to check and handle these unusual quantities during data cleaning.
# Converting InvoiceDate into datetime format
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# Revenue- how much money each transaction makes
df["Revenue"] = df["Quantity"] * df["UnitPrice"]
df["Month"] = df["InvoiceDate"].dt.to_period("M")

monthly_revenue = (df.groupby("Month")["Revenue"].sum())
# Note: This monthly revenue is calculated from the original transaction data before preprocessing.
# Returns/cancellations are therefore included in this. Just for EDA purpose
# Plotting Monthly revenue

plt.figure(figsize=(12, 5))

monthly_revenue.plot()

plt.xlabel("Month")
plt.ylabel("Revenue")
plt.title("Monthly Revenue")
plt.xticks(rotation=45)

plt.show()
#                                           INSIGHTS FROM THE GRAPH

# Revenue falls from December 2010 to February 2011.
# It increases in March, then falls again in April.
# From May to August, revenue stays fairly stable, around 0.7 million.
# Revenue rises sharply in September and October.
# November has the highest revenue, around 1.45 million.
# Revenue drops sharply in December 2011.
# The December 2011 drop should be treated carefully because the dataset only contains data up to December 9, 2011, so it is only a partial month, not a full month.
# Overall, the graph shows that monthly revenue changes significantly over time, which supports the need for the forecasting part of the project.
# We find country-wise revenue to understand which countries are contributing most to the sales

country_revenue = (
    df.groupby("Country")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
# Plotting Country revenue

plt.figure(figsize=(10, 5))

country_revenue.plot(kind="bar")

plt.xlabel("Country")
plt.ylabel("Revenue")
plt.title("Top 10 Countries by Revenue")
plt.xticks(rotation=45)

plt.show()
#                                           INSIGHTS FROM THE GRAPH

# United Kingdom has by far the highest revenue, much more than all the other countries.
# Netherlands, EIRE, Germany, and France are the next highest contributors.
# Australia, Switzerland, Spain, Belgium, and Sweden contribute much less revenue.
# This shows that the sales are highly concentrated in a few countries, especially the United Kingdom.
# This helps us understand where most of the business comes from
