# Write your MySQL query statement below
SELECT Patients.patient_id, Patients.patient_name, Patients.conditions
FROM Patients
WHERE Patients.conditions LIKE '% DIAB1%' OR Patients.conditions LIKE 'DIAB1%'; 