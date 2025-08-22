/*Q1. Get the second highest salary.*/ 

Select MAX(salary) 
 from Employees
 where salary < (Select MAX(salary) from Employees)


/*Q2.Find employees who earn more than the average salary.*/

Select name, salary from Employees
where salary > (Select AVG(salary) FROM Employees)

/* Q3. Department-wise maximum salary.*/

SELECT d.dept_name, MAX(e.salary) AS max_salary
FROM Employees e
JOIN Departments d ON e.dept_id = d.dept_id
GROUP BY d.dept_name;

/*Q4. Employees without managers.*/

Select name from Employees
Where manager_id is NULL


/* Top 3 salaries per department. Method 1*/

SELECT *
FROM (
  SELECT e.name, e.salary, e.dept_id,
         RANK() OVER (PARTITION BY e.dept_id ORDER BY e.salary DESC) as rnk
  FROM Employees e
) t
WHERE rnk <= 3;

/* Top 3 salaries per department. Method 2*/

SELECT e1.dept_id, e1.name, e1.salary
FROM Employees e1
WHERE 3 > (
    SELECT COUNT(DISTINCT e2.salary)
    FROM Employees e2
    WHERE e2.dept_id = e1.dept_id   -- same department
      AND e2.salary > e1.salary     -- salary higher than current
)
ORDER BY e1.dept_id, e1.salary DESC;

/*
