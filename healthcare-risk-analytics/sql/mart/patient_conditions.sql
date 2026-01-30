CREATE OR REPLACE TABLE mart.patient_conditions AS
SELECT
  patient_id,
  COUNT(DISTINCT condition_code) AS condition_count
FROM staging.conditions_clean
GROUP BY patient_id;
