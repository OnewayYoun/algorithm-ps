/*
입양을 간 동물 중, 보호 기간이 가장 길었던 동물 두 마리의 아이디와 이름을 조회하는 SQL문을 작성해주세요. 이때 결과는 보호 기간이 긴 순으로 조회해야 합니다.
*/

-- 코드를 입력하세요
SELECT animal_ins.animal_id, animal_ins.name
FROM animal_outs, animal_ins
WHERE animal_outs.animal_id = animal_ins.animal_id
ORDER BY animal_ins.datetime - animal_outs.datetime
LIMIT 2