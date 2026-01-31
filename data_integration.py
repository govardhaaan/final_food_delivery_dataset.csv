import pandas as pd
import json
import sqlite3
import os

def process_data():
    print("--- Starting ETL Process ---")

    # Step 1: Load CSV Data
    if os.path.exists('orders.csv'):
        orders_df = pd.read_csv('orders.csv')
        print("✔ Orders data loaded.")
    else:
        print("✘ orders.csv not found.")
        return

    # Step 2: Load JSON Data
    if os.path.exists('users.json'):
        with open('users.json', 'r') as f:
            users_data = json.load(f)
        users_df = pd.DataFrame(users_data)
        print("✔ Users data loaded.")
    else:
        print("✘ users.json not found.")

    # Step 3: Load SQL Data
    if os.path.exists('restaurants.sql'):
        conn = sqlite3.connect(':memory:')
        with open('restaurants.sql', 'r') as f:
            sql_script = f.read()
        conn.executescript(sql_script)
        restaurants_df = pd.read_sql_query("SELECT * FROM restaurants", conn)
        conn.close()
        print("✔ Restaurants data loaded from SQL.")
    else:
        print("✘ restaurants.sql not found.")

    # Step 4: Merge the Data (Left Join)
    # Merge orders with users on user_id
    final_df = orders_df.merge(users_df, on='user_id', how='left')

    # Merge with restaurants on restaurant_id
    # Using suffixes to differentiate between restaurant names if they exist in both tables
    final_df = final_df.merge(restaurants_df, on='restaurant_id', how='left', suffixes=('', '_info'))

    # Step 5: Data Cleaning
    final_df['order_date'] = pd.to_datetime(final_df['order_date'], dayfirst=True)

    # Step 6: Create Final Dataset
    output_file = 'final_food_delivery_dataset.csv'
    final_df.to_csv(output_file, index=False)
    
    print(f"\n--- Process Complete ---")
    print(f"Final dataset saved as: {output_file}")
    print(f"Total records processed: {len(final_df)}")

if __name__ == "__main__":
    process_data()
