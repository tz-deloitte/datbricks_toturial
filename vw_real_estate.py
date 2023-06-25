# Databricks notebook source
# MAGIC %sql
# MAGIC -- Create a temporary view
# MAGIC CREATE OR REPLACE TEMPORARY VIEW vw_real_estate
# MAGIC
# MAGIC USING csv
# MAGIC OPTIONS (
# MAGIC   path "/mnt/real_estate_short_sample_5k/real_estate_short_sample_5k.csv",
# MAGIC   header "true"
# MAGIC );
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Query the view
# MAGIC SELECT *
# MAGIC FROM vw_real_estate;
