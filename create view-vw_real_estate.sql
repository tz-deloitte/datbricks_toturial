-- Databricks notebook source
-- MAGIC %sql
-- MAGIC
-- MAGIC -- Create a temporary view
-- MAGIC CREATE OR REPLACE TEMPORARY VIEW vw_real_estate
-- MAGIC USING csv
-- MAGIC OPTIONS (
-- MAGIC   path "/mnt/real_estate_short_sample_5k/real_estate_short_sample_5k.csv",
-- MAGIC   header "true"
-- MAGIC );
-- MAGIC

-- COMMAND ----------

select * from  vw_real_estate;