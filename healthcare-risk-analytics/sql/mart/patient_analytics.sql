CREATE OR REPLACE TABLE mart.patient_analytics AS
SELECT
  u.patient_id,
  u.age,
  u.gender,
  u.total_encounters,
  u.inpatient_visits,
  u.outpatient_visits,
  u.avg_length_of_stay,
  COALESCE(c.condition_count, 0) AS condition_count,
  COALESCE(p.procedure_count, 0) AS procedure_count
FROM mart.patient_utilization u
LEFT JOIN mart.patient_conditions c
ON u.patient_id = c.patient_id
LEFT JOIN mart.patient_procedures p
ON u.patient_id = p.patient_id;
