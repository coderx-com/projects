CREATE OR REPLACE TABLE staging.patients_clean AS
SELECT
  id AS patient_id,
  gender,
  race,
  ethnicity,
  DATE(birthdate) AS birth_date,
  DATE(deathdate) AS death_date,
  DATE_DIFF(CURRENT_DATE(), DATE(birthdate), YEAR) AS age,
  state,
  county,
  zip
FROM raw.patients;
