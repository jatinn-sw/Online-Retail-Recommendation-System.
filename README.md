# Online Retail Recommendation System

A web-based product recommendation system for online retail data, using collaborative filtering. Built with Python (Flask), HTML, CSS, and JavaScript.

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

## Features
- Collaborative filtering recommendations for retail customers
- Modern, responsive web UI
- Real-time recommendations by Customer ID
- Loading spinner, error handling, and smooth animations
- Accuracy evaluation script

## Setup Instructions

1. **Clone the repository and navigate to the project folder.**
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Flask app:**
   ```bash
   python app.py
   ```
4. **Open your browser:**
   Go to [http://localhost:5500](http://localhost:5500)

## Usage
- Enter a valid Customer ID given in the dataset to get product recommendations.
- Recommendations are based on similar users' purchase histories.


