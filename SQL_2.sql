SELECT t.client_id, 
SUM((SELECT SUM(prod_price*prod_qty) FROM `TRANSACTION` WHERE TRANSACTION.prop_id=PRODUCT_NOMENCLATURE.product_id AND product_type = "MEUBLE" AND TRANSACTION.client_id = t.client_id )) AS ventes_meuble, 
SUM((SELECT SUM(prod_price*prod_qty) FROM `TRANSACTION` WHERE TRANSACTION.prop_id=PRODUCT_NOMENCLATURE.product_id AND product_type = "DECO" AND TRANSACTION.client_id = t.client_id)) AS ventes_deco 
FROM `TRANSACTION` t INNER JOIN PRODUCT_NOMENCLATURE ON t.prop_id=PRODUCT_NOMENCLATURE.product_id 
WHERE date >= '2020-01-01' AND date <= '2020-12-31' 
GROUP BY client_id