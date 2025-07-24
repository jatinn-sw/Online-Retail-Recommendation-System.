import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from tqdm import tqdm

# Load data
file_path = 'OnlineRetail.csv'
df = pd.read_csv(file_path)
df = df.dropna(subset=['CustomerID', 'StockCode'])

# Create user-item matrix
user_item_matrix = pd.pivot_table(
    df, 
    index='CustomerID', 
    columns='StockCode', 
    values='Quantity', 
    aggfunc='sum', 
    fill_value=0
)
user_sim = cosine_similarity(user_item_matrix)
user_sim_df = pd.DataFrame(user_sim, index=user_item_matrix.index, columns=user_item_matrix.index)

np.random.seed(42)
users = user_item_matrix.index.values
sample_users = np.random.choice(users, size=min(100, len(users)), replace=False)
hits = 0
total = 0

for user in tqdm(sample_users, desc='Evaluating'):
    user_items = user_item_matrix.loc[user]
    bought_items = user_items[user_items > 0].index.tolist()
    if len(bought_items) < 2:
        continue  # Need at least 2 items to test
    hidden_item = np.random.choice(bought_items)
    # Hide the item
    user_item_matrix_hidden = user_item_matrix.copy()
    user_item_matrix_hidden.loc[user, hidden_item] = 0
    # Recompute recommendations
    sim_scores = user_sim_df.loc[user]
    sim_scores = sim_scores.drop(user)
    top_users = sim_scores.sort_values(ascending=False).head(5).index
    similar_users_items = user_item_matrix_hidden.loc[top_users].sum()
    user_items_hidden = user_item_matrix_hidden.loc[user]
    recommendations = similar_users_items[user_items_hidden == 0].sort_values(ascending=False).head(5)
    if hidden_item in recommendations.index:
        hits += 1
    total += 1

accuracy = hits / total if total > 0 else 0
print(f'Hit Rate (Accuracy) on Top-5 Recommendations: {accuracy:.2%} ({hits}/{total})') 