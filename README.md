# Food Delivery Data Integration Hackathon

## Project Overview
This project simulates a real-world data engineering task where data from three different sources (CSV, JSON, and SQL) is integrated into a single "Source of Truth" for business analysis.

## Dataset Components
1. **orders.csv**: Transactional data containing order IDs, dates, and amounts.
2. **users.json**: Master data containing user names, cities, and membership status.
3. **restaurants.sql**: Master data containing restaurant cuisines and ratings.

## ETL Process (Extract, Transform, Load)
- **Extract**: Loaded data using `pandas`, `json`, and `sqlite3` libraries.
- **Transform**: 
    - Performed a **Left Join** on `user_id` to link transactions to users.
    - Performed a **Left Join** on `restaurant_id` to link transactions to restaurant details.
    - Converted date strings to datetime objects for time-series analysis.
- **Load**: Exported the consolidated data to `final_food_delivery_dataset.csv`.

## Key Findings from the Final Dataset
- **Total Transactions**: 10,000
- **Total Revenue (Hyderabad)**: ₹1,889,367
- **Gold Member Contribution**: 50% of total orders.
- **Top Performing City (Gold)**: Chennai.
- **Highest Revenue Rating Range**: 4.6 – 5.0.

## How to Run
1. Ensure you have `orders.csv`, `users.json`, and `restaurants.sql` in the root directory.
2. Run the script:
   ```bash
   python merge_data.py
