/*
천재지변으로 인해 일부 데이터가 유실되었습니다. 입양을 간 기록은 있는데, 보호소에 들어온 기록이 없는 동물의 ID와 이름을 ID 순으로 조회하는 SQL문을 작성해주세요.
*/

-- 코드를 입력하세요
SELECT animal_outs.animal_id, animal_outs.name
FROM animal_outs
LEFT JOIN animal_ins
ON animal_outs.animal_id = animal_ins.animal_id
WHERE animal_ins.animal_id is NULL
ORDER BY animal_ins.animal_id