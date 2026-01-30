CREATE OR REPLACE TABLE mart.patient_procedures AS
SELECT
  patient_id,
  COUNT(DISTINCT procedure_code) AS procedure_count
FROM staging.procedures_clean
GROUP BY patient_id;
