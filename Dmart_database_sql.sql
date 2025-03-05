create database DMart;
use dmart

# create a table
create table products(
name varchar(255),
brand varchar(255),
price float,
discountedprice float,
category varchar(255),
quantity varchar(50),
sold_in varchar(50)
);

#updating the table
alter table products
modify quantity int,
add unit varchar(10);



use dmart;
select * from products;
 
 #find all the null values
select * from products
where qty is null;

select * from products
where name is null;

select * from products
where price is null;
