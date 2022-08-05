SELECT PF_CODE AS "都道府県コード",
    PF_NAME AS "都道府県名",
    -- MAXがないと rnk = 2以下はすべて　nullか 0になる 
    MAX(
        CASE
            WHEN rnk = 1 THEN NATION_NAME
            ELSE null
        END
    ) AS "1位 国名",
    MAX(
        CASE
            WHEN rnk = 1 THEN AMT
            ELSE 0
        END
    ) AS "1位 人数",
    MAX(
        CASE
            WHEN rnk = 2 THEN NATION_NAME
            ELSE null
        END
    ) AS "2位 国名",
    MAX(
        CASE
            WHEN rnk = 2 THEN AMT
            ELSE 0
        END
    ) AS "2位 人数",
    MAX(
        CASE
            WHEN rnk = 3 THEN NATION_NAME
            ELSE null
        END
    ) AS "3位 国名",
    MAX(
        CASE
            WHEN rnk = 3 THEN AMT
            ELSE 0
        END
    ) AS "3位 人数",
    SUM(AMT) AS "合計人数"
FROM (
        SELECT p.PF_CODE,
            p.PF_NAME,
            n.NATION_NAME,
            f.AMT,
            rank() over (
                partition by p.PF_CODE
                order by AMT desc,
                    n.NATION_CODE
            ) as rnk
        FROM FOREIGNER f
            INNER JOIN NATIONALITY n ON f.NATION_CODE = n.NATION_CODE
            INNER JOIN PREFECTURE p ON f.PF_CODE = p.PF_CODE
        WHERE f.NATION_CODE <> "113"
        GROUP BY 1,
            2,
            3,
            4
    )
GROUP BY PF_CODE,
    PF_NAME
ORDER BY "合計人数" DESC,
    PF_CODE