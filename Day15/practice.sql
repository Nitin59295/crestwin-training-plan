'1. Find the second-highest salary/marks from a table.'
ans. select salary from (
	select salary,
  DENSE_RANK() OVER(ORDER bY salary DESC) as rnk
  from employees
)	WHERE rnk=2;

'2. Find duplicate emails'
ans. select count(email) from employees
GROUP by email
having count(email)>1

'3. Employees earning more than average salary'
ans. select name,salary from employees
where salary > (SELECT AVG(salary) from employees)

'4.  Top 2 employees from each department'
ans. SELECT name, salary, department_id
FROM (
    SELECT name,
           salary,
           department_id,
           ROW_NUMBER() OVER (
               PARTITION BY department_id
               ORDER BY salary DESC
           ) AS rn
    FROM employees
)
WHERE rn <= 2;

'5. INNER JOIN employees with departments'
SELECT e.name,
       e.salary,
       d.department_name
FROM employees e
INNER JOIN departments d
ON e.department_id = d.department_id;

'6. Departments having more than 5 employees'
SELECT department_id,
       COUNT(*) AS employee_count
FROM employees
GROUP BY department_id
HAVING COUNT(*) > 5;