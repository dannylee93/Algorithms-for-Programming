-- 아픈 동물 찾기
SELECT animal_id, name
FROM animal_ins
WHERE intake_condition LIKE 'Sick'
ORDER BY animal_id ASC;