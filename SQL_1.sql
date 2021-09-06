SELECT date, SUM(prod_price*prod_qty) AS ventes
FROM `TRANSACTION`
WHERE date >= '2020-01-01' AND date <= '2020-12-31'
GROUP BY date


