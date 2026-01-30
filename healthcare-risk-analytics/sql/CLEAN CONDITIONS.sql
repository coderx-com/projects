CREATE OR REPLACE TABLE staging.conditions_clean AS
SELECT
  patient AS patient_id,
  encounter AS encounter_id,
  code AS condition_code,
  description AS condition_desc,
  DATE(start) AS condition_start_date,
  DATE(stop) AS condition_end_date
FROM raw.conditions;
