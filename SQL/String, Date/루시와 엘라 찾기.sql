/*
동물 보호소에 들어온 동물 중 이름이 Lucy, Ella, Pickle, Rogan, Sabrina, Mitty인 동물의 아이디와 이름, 성별 및 중성화 여부를 조회하는 SQL 문을 작성해주세요.
*/

-- 코드를 입력하세요
SELECT animal_id, name, sex_upon_intake
FROM animal_ins
WHERE name IN ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')


SELECT animal_id, name, sex_upon_intake
FROM animal_ins
WHERE name LIKE 'Lucy' OR name LIKE 'Ella' OR name LIKE 'Pickle'
OR name LIKE 'Rogan' OR name LIKE 'Sabrina' OR name LIKE'Mitty'