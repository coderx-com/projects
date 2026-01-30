CREATE OR REPLACE TABLE staging.medications_clean AS
SELECT
  patient AS patient_id,
  encounter AS encounter_id,
  code AS medication_code,
  description AS medication_desc,
  DATE(start) AS medication_start_date,
  DATE(stop) AS medication_end_date
FROM raw.medications;
