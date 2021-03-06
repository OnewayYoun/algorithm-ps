/*
동물 보호소에 들어온 동물 중 고양이와 개가 각각 몇 마리인지 조회하는 SQL문을 작성해주세요.
이때 고양이를 개보다 먼저 조회해주세요.
*/

-- 코드를 입력하세요
--SELECT animal_type, COUNT(*) AS count
--FROM animal_ins
--GROUP BY animal_type
--ORDER BY animal_type;

SELECT DISTINCT animal_type, COUNT(animal_type)
FROM animal_ins
GROUP BY animal_type
ORDER BY animal_type;