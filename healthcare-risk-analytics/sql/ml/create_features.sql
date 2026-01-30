CREATE OR REPLACE TABLE features.patient_features AS
SELECT
  patient_id,
  age,
  gender,
  total_encounters,
  inpatient_visits,
  outpatient_visits,
  avg_length_of_stay,
  condition_count,
  procedure_count,
  IF(total_encounters >= 5, 1, 0) AS high_utilizer
FROM mart.patient_analytics;
