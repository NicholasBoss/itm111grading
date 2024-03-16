-- ~
USE magazine;
-- ~
-- 1
-- ~
SELECT magazineName,ROUND(magazinePrice * 0.63, 2) AS "37% off"
from magazine;
-- ~
-- 2
-- ~
SELECT subscriberKey,ROUND(DATEDIFF('2021-04-23', subscriptionStartDate)/ 365) AS 'Years since subscription'
FROM subscription;
-- ~
-- 3
-- ~
SELECT subscriptionStartDate AS 'subscriptionStartDate', subscriptionLength, DATE_FORMAT(DATE_ADD(subscriptionStartDate, INTERVAL subscriptionLength MONTH),'%m %d, %y') AS 'SubscriptionEnd'
FROM subscription;
-- ~
-- ~
USE bike;
-- ~
-- 4
-- ~
SELECT SUBSTRING(product_name, LOCATE(' -', product_name)) AS 'product name w/o product name'
FROM product
ORDER BY product_id
LIMIT 14;
-- ~
-- 5
-- ~
SELECT product_name,CONCAT('$', FORMAT(list_price, 2)) AS Price,CONCAT('$', FORMAT(list_price * 0.2, 2)) AS '20% Down',CONCAT('$', FORMAT((list_price - (list_price * 0.2)) / 7, 2)) AS 'Seven Equal Payments'
FROM product
WHERE model_year = 2019;
-- ~