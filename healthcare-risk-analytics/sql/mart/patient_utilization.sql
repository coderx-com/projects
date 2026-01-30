CREATE OR REPLACE TABLE mart.patient_utilization AS
SELECT
  p.patient_id,
  p.age,
  p.gender,
  COUNT(DISTINCT e.encounter_id) AS total_encounters,
  COUNTIF(e.encounterclass = 'inpatient') AS inpatient_visits,
  COUNTIF(e.encounterclass = 'outpatient') AS outpatient_visits,
  AVG(e.length_of_stay_days) AS avg_length_of_stay,
  MAX(e.encounter_start_date) AS last_encounter_date
FROM staging.patients_clean p
LEFT JOIN staging.encounters_clean e
ON p.patient_id = e.patient_id
GROUP BY 1,2,3;
