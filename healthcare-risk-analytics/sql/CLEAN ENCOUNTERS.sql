CREATE OR REPLACE TABLE staging.encounters_clean AS
SELECT
  id AS encounter_id,
  patient AS patient_id,
  encounterclass,
  DATE(start) AS encounter_start_date,
  DATE(stop) AS encounter_end_date,
  reasondescription,
  DATE_DIFF(DATE(stop), DATE(start), DAY) AS length_of_stay_days
FROM raw.encounters;
