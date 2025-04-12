-- Ctrl + Shift + Q to open a connection to the bank and to run


-- SELECT 
--     seller_id , 
--     count(*) AS frequency 
-- FROM tb_order_items
-- GROUP BY 1


SELECT 
    seller_id , 
    count(*) AS frequency ,
    sum(price) AS amount
FROM tb_order_items
GROUP BY 1
