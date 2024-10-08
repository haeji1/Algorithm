# 연도별 가장 큰 대장균 크기 구하기
WITH MAX_SIZE_OF_COLONY AS (
    SELECT MAX(SIZE_OF_COLONY) AS SIZE, YEAR(DIFFERENTIATION_DATE) AS YEAR
    FROM ECOLI_DATA
    GROUP BY YEAR
)

SELECT YEAR, (M.SIZE - E.SIZE_OF_COLONY) AS YEAR_DEV, E.ID
FROM ECOLI_DATA E JOIN MAX_SIZE_OF_COLONY M
ON YEAR(E.DIFFERENTIATION_DATE) = M.YEAR
ORDER BY YEAR, YEAR_DEV
