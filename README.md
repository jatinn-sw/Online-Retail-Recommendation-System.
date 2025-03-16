# Online Retail Recommendation System

This project focuses on building a recommendation system for an online retail store using two different approaches. The goal is to provide personalized product recommendations to customers based on their purchase history and behavior. The dataset used is the "Online Retail" dataset, which contains transactional data for an online retail store.

## Dataset Information
The dataset used in this project is from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Online+Retail), which contains:
- **Transactions**: Customer purchases from an online retail store.
- **Columns**:
  - `InvoiceNo`: Invoice number (unique identifier for each transaction).
  - `StockCode`: Product code (unique identifier for each product).
  - `Description`: Product description.
  - `Quantity`: Quantity of the product purchased.
  - `InvoiceDate`: Date and time of the transaction.
  - `UnitPrice`: Price of the product per unit.
  - `CustomerID`: Unique identifier for each customer.
  - `Country`: Country where the transaction occurred.

## Project Overview

The project is divided into two main approaches:

1. **Popularity-Based Recommendation System**
2. **Item-to-Item and User-to-User Collaborative Filtering Recommendation System**

Each approach is implemented using Python and leverages libraries such as Pandas, Seaborn, Matplotlib, and Scikit-learn.

## Approach 1: Popularity-Based Recommendation System

### Description
This approach focuses on recommending products based on their overall popularity. The system identifies the most frequently purchased items globally, by country, and by month. It then provides recommendations based on these popular items.

### Key Steps:
1. **Data Preprocessing**: 
   - Load and clean the dataset.
   - Handle missing values, especially in the `CustomerID` column.
   - Convert the `InvoiceDate` to a datetime format.

2. **Exploratory Data Analysis (EDA)**:
   - Analyze the number of transactions by country.
   - Visualize sales trends over time.
   - Identify the most popular items globally and by country.

3. **Recommendation Function**:
   - The system provides recommendations based on global popularity, country-specific popularity, or monthly trends.

### Example Usage:
- **Global Recommendations**: Recommends the top 10 most popular items globally.
- **Country-Specific Recommendations**: Recommends popular items for a specific country (e.g., United Kingdom).
- **Monthly Recommendations**: Recommends popular items for a specific month (e.g., December 2011).

## Approach 2: Item-to-Item and User-to-User Collaborative Filtering Recommendation System

### Description
This approach uses collaborative filtering to recommend products. It includes two types of filtering:
- **Item-to-Item Filtering**: Recommends items that are similar to the ones a user has already purchased.
- **User-to-User Filtering**: Recommends items based on the purchase history of similar users.

### Key Steps:
1. **Data Preprocessing**:
   - Load and clean the dataset.
   - Handle missing values in the `CustomerID` column.
   - Create a customer-item matrix to represent purchases.

2. **Item-to-Item Similarity**:
   - Compute the cosine similarity between items based on customer purchase history.
   - Generate recommendations for items similar to a given product.

3. **User-to-User Similarity**:
   - Compute the cosine similarity between users based on their purchase history.
   - Generate recommendations for a user based on the purchase history of similar users.

4. **Heatmap Visualization**:
   - Visualize the item-to-item and user-to-user similarity matrices using heatmaps.

### Example Usage:
- **Item-to-Item Recommendations**: Given a product (e.g., StockCode `23150`), the system recommends similar items.
- **User-to-User Recommendations**: Given a customer (e.g., CustomerID `12703`), the system recommends products based on the purchase history of similar users.
