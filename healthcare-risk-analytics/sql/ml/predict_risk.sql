CREATE OR REPLACE TABLE predictions.patient_risk_scores AS
SELECT
  patient_id,
  predicted_high_utilizer,
  predicted_high_utilizer_probs[OFFSET(1)] AS risk_score
FROM ML.PREDICT(
  MODEL predictions.high_utilizer_model,
  (
    SELECT
      patient_id,
      age,
      gender,
      total_encounters,
      inpatient_visits,
      outpatient_visits,
      avg_length_of_stay,
      condition_count,
      procedure_count
    FROM features.patient_features
  )
);
