from flask import Flask, request, jsonify, render_template
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

app = Flask(__name__, static_folder='static', template_folder='templates')

# Load and preprocess data
file_path = 'OnlineRetail.csv'
df = pd.read_csv(file_path)

# Drop rows with missing CustomerID or StockCode
filtered_df = df.dropna(subset=['CustomerID', 'StockCode'])

# Create user-item matrix (CustomerID x StockCode)
user_item_matrix = pd.pivot_table(
    filtered_df, 
    index='CustomerID', 
    columns='StockCode', 
    values='Quantity', 
    aggfunc='sum', 
    fill_value=0
)

# Compute cosine similarity between users
user_sim = cosine_similarity(user_item_matrix)
user_sim_df = pd.DataFrame(user_sim, index=user_item_matrix.index, columns=user_item_matrix.index)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend')
def recommend():
    customer_id = request.args.get('customer_id')
    if customer_id is None:
        return jsonify({'error': 'customer_id is required'}), 400
    try:
        customer_id = float(customer_id)
    except ValueError:
        return jsonify({'error': 'Invalid customer_id'}), 400
    if customer_id not in user_item_matrix.index:
        return jsonify({'error': 'Customer not found'}), 404

    # Find similar users
    sim_scores = user_sim_df.loc[customer_id]
    sim_scores = sim_scores.drop(customer_id)  # Remove self
    top_users = sim_scores.sort_values(ascending=False).head(5).index

    # Aggregate items bought by similar users
    similar_users_items = user_item_matrix.loc[top_users].sum()
    user_items = user_item_matrix.loc[customer_id]
    # Recommend items not already bought by the user
    recommendations = similar_users_items[user_items == 0].sort_values(ascending=False).head(5)

    # Get product descriptions
    stockcode_to_desc = filtered_df.set_index('StockCode')['Description'].to_dict()
    recs = [
        {
            'StockCode': code,
            'Description': stockcode_to_desc.get(code, 'Unknown')
        }
        for code in recommendations.index
    ]
    return jsonify({'recommendations': recs})

if __name__ == '__main__':
    app.run(debug=True, port=5500) 