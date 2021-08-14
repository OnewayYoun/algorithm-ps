/*
동물 보호소에 가장 먼저 들어온 동물의 이름을 조회하는 SQL 문을 작성해주세요.
*/

-- 코드를 입력하세요
SELECT name
FROM animal_ins
ORDER BY datetime
LIMIT 1

-- SELECT name
-- FROM animal_ins
-- WHERE datetime IN(
--     SELECT MIN(datetime) AS datetime
--     FROM animal_ins
-- )