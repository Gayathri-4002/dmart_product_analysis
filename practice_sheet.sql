use dmart;
select * from products limit 10;

#count the unique product name for each brand
select brand ,count(distinct name) from products 
#where brand = "premia"
group by brand;

#find the duplicate product name for each brand
select brand,name, count(name) from products
#where brand = "premia"
group by brand,name
having count(name)>1;

#list brand,productname, the max price (windows func)
select brand, name, discountedprice,
max(discountedprice) over (partition by name, brand )
from products
where brand='premia'
order by name
#group by  brand, name,discountedprice
