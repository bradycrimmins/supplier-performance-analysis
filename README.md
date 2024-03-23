# Supplier Performance Analysis Tool

## Description
This Python script is designed to dynamically fetch and analyze supplier performance data from a mix of cloud and on-premises databases. It utilizes SQL queries optimized with Common Table Expressions (CTEs) and indexing to pre-filter data efficiently. The analysis includes computing Key Performance Indicators (KPIs) such as delivery delays and fulfillment rates and leverages multiprocessing for enhanced computation speed. The results are visualized using Plotly, providing insightful charts that highlight supplier fulfillment rates.

## Features
- **Dynamic Data Fetching**: Uses SQLAlchemy to connect to both cloud and on-premises SQL databases, fetching supplier and order data dynamically.
- **Optimized SQL Queries**: Incorporates advanced SQL techniques, including subqueries and CTEs, to efficiently filter and process data directly within the database.
- **Parallel Processing**: Employs Python's `multiprocessing` module to parallelize KPI computation, optimizing performance for large datasets.
- **Data Visualization**: Utilizes Plotly for generating interactive bar charts, showcasing supplier fulfillment rates and potentially other computed KPIs.
- **Scalability**: The script is designed to handle large volumes of data, making it suitable for enterprise-level supplier performance analysis.

## Requirements
- Python 3.6+
- SQLAlchemy
- Pandas
- Plotly
- Multiprocessing (part of the standard library)

## Setup
1. Ensure you have Python 3.6+ installed on your machine.
2. Install the required Python packages using pip:
   ```bash
   pip install sqlalchemy pandas plotly
   ```
3. Replace the `cloud_db_string` and `on_prem_db_string` placeholders in the script with your actual database connection strings.
4. Modify the SQL query strings according to your database schema and the data you wish to analyze.

## Usage
1. Run the script in a Python environment. The script can be executed in any environment where Python is supported, such as a local development environment or a server.
2. The script will automatically connect to the specified databases, fetch the necessary data, compute KPIs, and generate a visualization of the supplier fulfillment rates.
3. The final Plotly chart will be displayed in your default web browser, providing an interactive way to explore the data.

## Customization
- The SQL queries within the script can be customized to fit your specific database schema and the particular insights you're seeking.
- The KPI computation functions can be modified or expanded to include additional performance metrics relevant to your analysis needs.
- The Plotly visualization code can be adjusted to change the chart type, style, or to visualize different KPIs based on your requirements.

## Note
This script assumes access to cloud and on-premises databases that are accessible through SQLAlchemy-compatible connection strings. Ensure that your database user has the necessary permissions to execute the specified queries.
