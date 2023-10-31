CREATE TABLE products (
  product_name VARCHAR(255),
  price DECIMAL(10,2),
  quantity INT,
  color VARCHAR(255),
  area DECIMAL(10,2)
);

INSERT INTO products (product_name, price, quantity, color, area)
VALUES ('HP Pavilion 15', 599.99, 3, 'Blue', 12.5),
       ('Dell Inspiron 13 7000', 699.99, 2, 'Silver', 9.5),
       ('Lenovo Yoga C740', 799.99, 1, 'Grey', 11.5),
       ('Acer Aspire 5 A515-55-378V', 599.99, 4, 'Black', 10.5);

SELECT *
FROM products
WHERE price <= 600
AND price > 1;

SELECT *
FROM products
WHERE quantity > 2
AND color = 'Blue';

SELECT product_name, price * quantity AS total_price
FROM products;

SELECT *
FROM products
WHERE area > 10;
