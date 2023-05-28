%sql
-- Create a temporary table using Databricks SQL
CREATE OR REPLACE TEMPORARY VIEW customers_data
USING DELTA
OPTIONS (path "dbfs:/databricks-datasets/tpch/delta-001/customer");

-- Display the content of the table
SELECT * FROM customers_data;
