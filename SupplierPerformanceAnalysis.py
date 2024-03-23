import pandas as pd
from sqlalchemy import create_engine
from multiprocessing import Pool
import plotly.express as px

# Connection strings for cloud and on-prem databases
cloud_db_string = 'your_cloud_database_connection_string'
on_prem_db_string = 'your_on_premises_database_connection_string'

# Create SQLAlchemy engines
cloud_engine = create_engine(cloud_db_string)
on_prem_engine = create_engine(on_prem_db_string)

# Optimized SQL queries with subqueries to pre-filter data
# Adjust according to your schema and ensure indexes are used in joins
suppliers_sql = """
SELECT supplier_id, name
FROM suppliers
WHERE active = 1;  -- Example of pre-filtering to active suppliers
"""

# Assuming a similar structure for on-prem data
orders_sql = """
WITH filtered_orders AS (
  SELECT purchase_order_id, supplier_id, order_date, delivery_date, 
         quantity_ordered, quantity_received
  FROM purchase_orders
  WHERE order_date >= '2021-01-01' AND order_date <= '2021-12-31'
),
quality_scores AS (
  SELECT purchase_order_id, AVG(quality_score) AS quality_score
  FROM quality_assessments
  GROUP BY purchase_order_id
)
SELECT fo.supplier_id, fo.purchase_order_id, fo.order_date, fo.delivery_date, 
       fo.quantity_ordered, fo.quantity_received, qs.quality_score
FROM filtered_orders fo
LEFT JOIN quality_scores qs ON fo.purchase_order_id = qs.purchase_order_id;
"""

# Fetching data
suppliers_data = pd.read_sql(suppliers_sql, cloud_engine)
orders_data = pd.read_sql(orders_sql, on_prem_engine)

# Merge using pandas
supplier_data = pd.merge(suppliers_data, orders_data, on='supplier_id')

# Example of parallel processing for computing KPIs using Dask or multiprocessing
def compute_kpis(df):
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['delivery_date'] = pd.to_datetime(df['delivery_date'])
    df['delivery_delay'] = (df['delivery_date'] - df['order_date']).dt.days
    df['fulfillment_rate'] = df['quantity_received'] / df['quantity_ordered']
    return df

# Using multiprocessing for parallel KPI computation
if __name__ == '__main__':
    with Pool(processes=4) as pool:  # Adjust number of processes based on your machine
        df_split = np.array_split(supplier_data, 4)  # Splitting DataFrame into 4 parts for parallel processing
        df_processed_list = pool.map(compute_kpis, df_split)
        supplier_data_processed = pd.concat(df_processed_list)

# Compute average quality score
supplier_data_processed['average_quality_score'] = supplier_data_processed.groupby('supplier_id')['quality_score'].transform('mean')

# Visualization with Plotly
fig = px.bar(supplier_data_processed, x='name', y='fulfillment_rate', title='Supplier Fulfillment Rate')
fig.update_layout(xaxis_title="Supplier Name", yaxis_title="Fulfillment Rate")
fig.show()
