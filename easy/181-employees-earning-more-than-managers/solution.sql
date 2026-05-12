# Write your MySQL query statement below
SELECT
    e.name AS Employee
FROM 
    Employee e
INNER JOIN 
    Employee m on e.managerID = m.id
where 
    e.salary > m.salary