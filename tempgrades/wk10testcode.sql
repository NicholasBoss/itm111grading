-- Q1
-- ~
USE bike;
-- ~
-- ~
SELECT DISTINCT COUNT(quantity) as 'Unique Stock'
FROM stock;
-- ~
-- Q2
-- ~
SELECT store_name, COUNT(quantity) as 'Number to be reordered'
FROM store
LEFT JOIN stock
ON store.store_id = stock.store_id
WHERE stock.quantity = 0
GROUP BY store_name;
-- ~
-- Q3
-- ~
SELECT category_name, SUM(quantity) as 'instock'
FROM category
LEFT JOIN product
ON category.category_id = product.category_id
LEFT JOIN stock
ON product.product_id = stock.product_id
WHERE stock.store_id = 1
GROUP BY category.category_name
ORDER BY SUM(quantity);
-- ~
-- ~
USE employees;
-- ~
-- Q4
-- ~
SELECT departments.dept_name, COUNT(dept_manager.emp_no) AS 'Number of Managers'
FROM departments
LEFT JOIN dept_manager
ON departments.dept_no = dept_manager.dept_no
GROUP BY departments.dept_name
UNION ALL
SELECT NULL, COUNT(emp_no)
FROM dept_manager;
-- ~
-- Q5
-- ~
SELECT dept_name, CONCAT('$',FORMAT(AVG(salary), 2)) AS 'Average Salary'
FROM departments
LEFT JOIN dept_manager 
ON departments.dept_no = dept_manager.dept_no
LEFT JOIN salaries
ON dept_manager.emp_no = salaries.emp_no
GROUP BY dept_name
HAVING AVG(salary) >= 70000;
-- ~
-- Q6
-- ~
SELECT dept_name, first_name, last_name
FROM departments
LEFT JOIN dept_manager
ON departments.dept_no = dept_manager.dept_no
LEFT JOIN employees
ON dept_manager.emp_no = employees.emp_no
WHERE departments.dept_name = 'Research';
-- ~

