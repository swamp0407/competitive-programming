SELECT PF_CODE AS "都道府県コード",
    PF_NAME AS "都道府県名",
    n1 AS "1位 国名",
    n1a AS "1位 人数",
    n2 AS "2位 国名",
    n2a AS "2位 人数",
    n3 AS "3位 国名",
    n3a AS "3位 人数",
    SUM(AMT) AS "合計人数"
FROM FOREIGNER f
    INNER JOIN NATIONALITY n ON f.NATION_CODE = n.NATION_CODE
    INNER JOIN PREFECTURE p ON f.PF_CODE = p.PF_CODE
    INNER JOIN (
        SELECT nn.NATION_CODE,
            nn.NATION_NAME AS n1,
            nn.NATION_NAME AS n1a
        FROM NATIONALITY nn
            INNER JOIN FOREIGNER ff ON ff.NATION_CODE = nn.NATION_CODE
        WHERE AMT = (
                SELECT MAX(AMT)
                FROM
            )
    ) AS sn1 ON sn1.NATION_CODE = n.NATION_CODE
    INNER JOIN (
        SELECT nn.NATION_CODE,
            nn.NATION_NAME AS n2,
            nn.NATION_NAME AS n2a
        FROM NATIONALITY nn
            INNER JOIN FOREIGNER ff ON ff.NATION_CODE = nn.NATION_CODE
        WHERE AMT = MAX(AMT)
    ) AS sn2 ON sn2.NATION_CODE = n.NATION_CODE
    INNER JOIN (
        SELECT nn.NATION_CODE,
            nn.NATION_NAME AS n3,
            nn.NATION_NAME AS n3a
        FROM NATIONALITY nn
            INNER JOIN FOREIGNER ff ON ff.NATION_CODE = nn.NATION_CODE
        WHERE AMT = MAX(AMT)
    ) AS sn3 ON sn3.NATION_CODE = n.NATION_CODE
WHERE f.NATION_CODE <> "113"
GROUP BY p.PF_CODE,
    p.PF_NAME
ORDER BY "合計人数" DESC,
    f.P