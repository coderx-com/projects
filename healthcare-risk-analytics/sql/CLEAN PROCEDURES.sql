CREATE OR REPLACE TABLE staging.procedures_clean AS
SELECT
  patient AS patient_id,
  encounter AS encounter_id,
  code AS procedure_code,
  description AS procedure_desc,
  DATE(start) AS procedure_date
FROM raw.procedures;
