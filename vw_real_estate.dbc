%sql

-- Create a temporary view
CREATE OR REPLACE TEMPORARY VIEW vw_real_estate
USING csv
OPTIONS (
  path "/mnt/real_estate_short_sample_5k/real_estate_short_sample_5k.csv",
  header "true"
);
