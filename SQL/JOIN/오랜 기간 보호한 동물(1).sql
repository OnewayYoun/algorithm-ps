/*
아직 입양을 못 간 동물 중, 가장 오래 보호소에 있었던 동물 3마리의 이름과 보호 시작일을 조회하는 SQL문을 작성해주세요.
이때 결과는 보호 시작일 순으로 조회해야 합니다.
*/

-- 코드를 입력하세요
SELECT animal_ins.name, animal_ins.datetime
FROM animal_ins
LEFT JOIN animal_outs
on animal_ins.animal_id = animal_outs.animal_id
WHERE animal_outs.animal_id IS NULL
ORDER BY animal_ins.datetime
LIMIT 3;


-- 코드를 입력하세요
--SELECT animal_ins.name, animal_ins.datetime, animal_outs.animal_id
--FROM animal_ins
--LEFT JOIN animal_outs
--on animal_ins.animal_id = animal_outs.animal_id
--WHERE animal_outs.animal_id IS NULL
--ORDER BY animal_ins.datetime
--LIMIT 3;