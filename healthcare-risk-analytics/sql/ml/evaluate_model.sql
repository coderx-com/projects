SELECT *
FROM ML.EVALUATE(
  MODEL predictions.high_utilizer_model,
  (
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
    FROM features.patient_features
  )
);
