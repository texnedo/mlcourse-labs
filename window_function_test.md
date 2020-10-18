```SQL
select customer_id, 
    count(*) as cnt
from purchases
group by customer_id
having count(*) > 1
order by cnt desc limit 10;

 customer_id | cnt 
-------------+-----
       21699 |   5
       41141 |   5
       25966 |   5
       44233 |   5
       54328 |   5
       51905 |   5
       35324 |   5
       49604 |   5
       58117 |   5
       46082 |   4
```

```SQL
select * from purchases 
where customer_id = 21699 
order by purchase_date;
 purchase_date | customer_id | product_category | payment_method | value_usd | time_on_site_mins | clicks_in_site 
---------------+-------------+------------------+----------------+-----------+-------------------+----------------
 2018-11-21    |       21699 |              513 | credit         |     38.26 |              10.9 |              9
 2018-11-22    |       21699 |              512 | paypal         |     73.83 |              12.3 |              6
 2018-11-23    |       21699 |              505 | credit         |     37.35 |               8.2 |              9
 2018-11-23    |       21699 |              505 | credit         |      26.2 |              15.3 |              8
 2018-11-27    |       21699 |              503 | credit         |    116.99 |                23 |             13
```

```SQL
select purchase_date, 
    value_usd, 
    sum(value_usd) over (partition by purchase_date order by purchase_date asc) as total_value_usd 
from purchases 
where customer_id = 21699 
order by purchase_date asc;
 purchase_date | value_usd | total_value_usd 
---------------+-----------+-----------------
 2018-11-21    |     38.26 |           38.26
 2018-11-22    |     73.83 |           73.83
 2018-11-23    |     37.35 |           63.55
 2018-11-23    |      26.2 |           63.55
 2018-11-27    |    116.99 |          116.99
```

```SQL
select purchase_date, 
    value_usd, 
    sum(value_usd) over (partition by customer_id order by purchase_date asc) as total_value_usd, 
    sum(time_on_site_mins) over (partition by customer_id order by purchase_date asc) as total_time_on_site_mins, 
    sum(clicks_in_site) over (partition by customer_id order by purchase_date asc) as total_clicks_in_site 
    from purchases 
where customer_id = 21699 
order by purchase_date asc;
 purchase_date | value_usd | total_value_usd | total_time_on_site_mins | total_clicks_in_site 
---------------+-----------+-----------------+-------------------------+----------------------
 2018-11-21    |     38.26 |           38.26 |                    10.9 |                    9
 2018-11-22    |     73.83 |          112.09 |      23.200000000000003 |                   15
 2018-11-23    |     37.35 |          175.64 |                    46.7 |                   32
 2018-11-23    |      26.2 |          175.64 |                    46.7 |                   32
 2018-11-27    |    116.99 |          292.63 |                    69.7 |                   45
```