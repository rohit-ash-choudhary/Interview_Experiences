/* SQL ROUND :

1. Ask the order of excaution of SQL
2. Union all vs Union which is past
3. # 1-- write a sql query to find the task start date and task end date.

#select * from taskTable

select start_date, end_date OVER


















# 2-- find the count of new customer added in each month


#select * from sales where

















#3 write a query to fill the subsequent null with their previosly mentioned products

#select * from Products_Table



CREATE TABLE taskTable
(
    task_id INT,
start_date VARCHAR(512),
end_date VARCHAR(512)
);

INSERT INTO taskTable (task_id, start_date, end_date) VALUES ('1', '2023-10-01', '2023-10-02');
INSERT INTO taskTable (task_id, start_date, end_date) VALUES ('2', '2023-10-02', '2023-10-03');
INSERT INTO taskTable (task_id, start_date, end_date) VALUES ('3', '2023-10-03', '2023-10-04');
INSERT INTO taskTable (task_id, start_date, end_date) VALUES ('4', '2023-10-15', '2023-10-16');
INSERT INTO taskTable (task_id, start_date, end_date) VALUES ('5', '2023-10-16', '2023-10-17');
INSERT INTO taskTable (task_id, start_date, end_date) VALUES ('6', '2023-10-21', '2023-10-22');
INSERT INTO taskTable (task_id, start_date, end_date) VALUES ('7', '2023-10-29', '2023-10-30');



CREATE TABLE sales
(
    order_date date,
customer VARCHAR(512),
qty INT
);

INSERT INTO sales (order_date, customer, qty) VALUES ('2021-01-01', 'C1', '20');
INSERT INTO sales (order_date, customer, qty) VALUES ('2021-01-01', 'C2', '30');
INSERT INTO sales (order_date, customer, qty) VALUES ('2021-02-01', 'C1', '10');
INSERT INTO sales (order_date, customer, qty) VALUES ('2021-02-01', 'C3', '15');
INSERT INTO sales (order_date, customer, qty) VALUES ('2021-03-01', 'C5', '19');
INSERT INTO sales (order_date, customer, qty) VALUES ('2021-03-01', 'C4', '10');
INSERT INTO sales (order_date, customer, qty) VALUES ('2021-04-01', 'C3', '13');
INSERT INTO sales (order_date, customer, qty) VALUES ('2021-04-01', 'C5', '15');
INSERT INTO sales (order_date, customer, qty) VALUES ('2021-04-01', 'C6', '10');


CREATE TABLE Products_Table (
    Products VARCHAR(50)
);

INSERT INTO Products_Table (Products)
VALUES
('bat'),
(NULL),
('stumps'),
(NULL),
(NULL),
('football'),
(NULL),
(NULL),
('ball'),
('Hat');
