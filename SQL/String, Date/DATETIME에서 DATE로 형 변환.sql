/*
ANIMAL_INS 테이블에 등록된 모든 레코드에 대해, 각 동물의 아이디와 이름, 들어온 날짜1를 조회하는 SQL문을 작성해주세요.
이때 결과는 아이디 순으로 조회해야 합니다.
*/

-- 코드를 입력하세요
SELECT animal_id, name, DATE_FORMAT(datetime, "%Y-%m-%d") AS 날짜
FROM animal_ins
ORDER BY animal_id

-- DATE_FORMAT(DATETIME, '형식')

-- %Y: (4자리 연도),    %y: (2자리 연도)
-- %M: (영어-월),       %m: (월)
-- %D: (일-th),        %d: (일)
-- %H: (24시간),       %h: (12시간)
-- %i, %s