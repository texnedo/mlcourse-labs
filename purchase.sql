CREATE DATABASE purchase;

--date,customer_id,product_category,payment_method,value [USD],time_on_site [Minutes],clicks_in_site

--20/11/2018,37077,505,credit,49.53,12.0,8,
--20/11/2018,59173,509,paypal,50.61,25.9,8,
--20/11/2018,41066,507,credit,85.99,34.9,11,
--20/11/2018,50741,506,credit,34.60,16.5,9,
--20/11/2018,53639,515,paypal,266.27,43.1,30,
--20/11/2018,39783,501,credit,193.78,14.0,10,
--20/11/2018,26767,514,paypal,61.22,11.6,8,
--20/11/2018,20719,505,paypal,11.18,3.1,7,
--20/11/2018,46947,515,paypal,144.01,38.3,6,

CREATE TABLE IF NOT EXISTS purchases (
   purchase_date DATE NOT NULL,
   customer_id INT NOT NULL,
   product_category INT NOT NULL,
   payment_method VARCHAR(50) NOT NULL,
   value_USD FLOAT NOT NULL,
   time_on_site_MINS FLOAT NOT NULL,
   clicks_in_site INT NOT NULL
);

CREATE INDEX idx_customer_id ON "purchases" USING btree (customer_id);

SELECT * FROM "purchases";

DELETE FROM "purchases" WHERE customer_id = '37077';