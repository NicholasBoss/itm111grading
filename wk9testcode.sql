-- ~
USE v_art;
-- ~
-- 1. When you visit art.ceiwebdev.com, and you search by artist first name 
--    and you choose Rembrandt, you get two resulting images 
--    ("Night watch" and "Storm Galilee"). 
--    Write the query that will display these images.
-- ~
SELECT lname, fname, title
FROM artist
INNER JOIN artwork 
	ON artist.artist_id = artwork.artist_id
WHERE artist.fname = 'Rembrandt';
-- ~
-- 2. When you visit art.ceiwebdev.com, and you search by Subject and type in the word bat, 
--    you get one image. Write the query to display that image.
--   (remember the keyword might have been 'battle' but they typed 'bat')
-- ~
SELECT artfile 
FROM artwork
INNER JOIN artwork_keyword
	ON artwork.artwork_id = artwork_keyword.artwork_id
INNER JOIN keyword
	ON artwork_keyword.keyword_id = keyword.keyword_id
WHERE keyword LIKE '%bat%';
-- ~
-- 3. List ALL the artists from the artist table from Italy, 
--    but only the related artwork from the artwork table.
--    We need the first and last name and artwork title. 
-- ~
SELECT fname, lname, title
FROM artist
LEFT JOIN artwork 
	ON artist.artist_id = artwork.artist_id
WHERE country = 'Italy' ;
-- ~
-- ~
USE magazine;
-- ~
-- 4. List all subscribers who don't subscribe to any magazine. 
--    List magazine name, and the subscriber's first and last name.
-- ~
SELECT magazineName, subscriberLastName, subscriberFirstName
FROM subscriber
LEFT JOIN subscription
	ON subscriber.subscriberKey = subscription.subscriberkey
LEFT JOIN magazine
	ON subscription.magazineKey = magazine.magazineKey
WHERE subscriptionStartDate IS NULL;
-- ~
-- 5.  List all the magazines that Lucy Lamont subscribes to.
-- ~ 
SELECT magazineName
FROM magazine
INNER JOIN subscription
	ON magazine.magazineKey = subscription.magazineKey
INNER JOIN subscriber 
	ON subscription.subscriberKey = subscriber.subscriberKey
WHERE subscriberLastName = 'Lamont' AND subscriberFirstName = 'Lucy';
-- ~
-- ~
USE employees;
-- ~
-- 6. List the managers from the Finance Department. 
--    Put them in alphabetical order by last name.
-- ~
SELECT first_name, last_name
FROM employees
RIGHT JOIN dept_manager
	ON employees.emp_no = dept_manager.emp_no
INNER JOIN departments
	ON dept_manager.dept_no = departments.dept_no
WHERE dept_name = 'Finance'
ORDER BY last_name;
-- ~
-- 7. Find out the current salary and department of Hisao Lipner. 
--    You can use the ORDER BY and LIMIT to get just the most recent salary. 
--    Format the salary to be readable (Use FORMAT())
-- ~
SELECT first_name, last_name, dept_name, salary
FROM employees
LEFT JOIN salaries 
	ON employees.emp_no = salaries.emp_no
LEFT JOIN dept_manager
	ON employees.emp_no = dept_manager.emp_no
LEFT JOIN departments
	ON dept_manager.dept_no = departments.dept_no
WHERE employees.first_name = "Hisao" AND employees.last_name = "Lipner"
ORDER BY salary DESC
LIMIT 1;
-- ~





