/*
보호소의 동물이 중성화되었는지 아닌지 파악하려 합니다.
중성화된 동물은 SEX_UPON_INTAKE 컬럼에 'Neutered' 또는 'Spayed'라는 단어가 들어있습니다.
동물의 아이디와 이름, 중성화 여부를 아이디 순으로 조회하는 SQL문을 작성해주세요.
이때 중성화가 되어있다면 'O', 아니라면 'X'라고 표시해주세요.
*/

-- 코드를 입력하세요
SELECT animal_id, name,
CASE
    WHEN sex_upon_intake LIKE "Neutered%" OR sex_upon_intake LIKE "Spayed%" THEN 'O'
    ELSE 'X'
END AS 중성화
FROM animal_ins
ORDER BY animal_id