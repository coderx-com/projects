CREATE OR REPLACE TABLE staging.observations_clean AS
SELECT
  patient AS patient_id,
  encounter AS encounter_id,
  code AS observation_code,
  description AS observation_desc,
  SAFE_CAST(value AS FLOAT64) AS observation_value,
  units,
  DATE(date) AS observation_date
FROM raw.observations;
