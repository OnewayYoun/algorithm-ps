/*
보호소에서 중성화 수술을 거친 동물 정보를 알아보려 합니다.
보호소에 들어올 당시에는 중성화1되지 않았지만, 보호소를 나갈 당시에는 중성화된 동물의 아이디와 생물 종, 이름을 조회하는 아이디 순으로 조회하는 SQL 문을 작성해주세요.
*/

-- 코드를 입력하세요
SELECT animal_outs.animal_id, animal_outs.animal_type, animal_outs.name
FROM animal_outs
JOIN animal_ins
on animal_outs.animal_id = animal_ins.animal_id
WHERE animal_ins.SEX_UPON_INTAKE LIKE "Intact%"
AND (animal_outs.SEX_UPON_OUTCOME LIKE "Neutered%"
OR animal_outs.SEX_UPON_OUTCOME LIKE "Spayed%")
ORDER BY animal_outs.animal_id