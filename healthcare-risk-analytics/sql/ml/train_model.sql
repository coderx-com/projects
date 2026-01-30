CREATE OR REPLACE MODEL predictions.high_utilizer_model
OPTIONS(
  model_type = 'logistic_reg',
  input_label_cols = ['high_utilizer'],
  auto_class_weights = TRUE
) AS
SELECT
  age,
  gender,
  total_encounters,
  inpatient_visits,
  outpatient_visits,
  avg_length_of_stay,
  condition_count,
  procedure_count,
  high_utilizer
FROM features.patient_features;
