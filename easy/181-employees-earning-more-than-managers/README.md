# 181. Employees Earning More Than Their Managers

**Difficulty:** Easy

**LeetCode Link:** [181. Employees Earning More Than Their Managers](https://leetcode.com/problems/employees-earning-more-than-their-managers/)

---

## Problem Statement (Enunciado)

Table: **Employee**

| Column Name | Type    |
|-------------|---------|
| id          | int     |
| name        | varchar |
| salary      | int     |
| managerId   | int     |

- `id` is the primary key (column with unique values).
- Each row indicates the ID of an employee, their name, salary, and the ID of their manager.
- If an employee has no manager, `managerId` is `NULL`.

Write a solution to find the employees who earn **more than their managers**.

Return the result table in **any order**.

---

## Example (Ejemplo)

### Input:

**Employee table:**

| id | name  | salary | managerId |
|----|-------|--------|-----------|
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | Null      |
| 4  | Max   | 90000  | Null      |

### Output:

| Employee |
|----------|
| Joe      |

### Explanation:

- Joe's manager is Sam (id = 3), and Joe earns $70000 while Sam earns $60000.
- Joe earns more than his manager → included in output.
- Henry's manager is Max, but Henry earns $80000 vs Max's $90000 → NOT included.
- Sam and Max have no managers → NOT included.

---

## Solution Approach (Enfoque de solución)

### Key Insight (Clave del problema)

We need to compare each employee's salary with **their manager's salary**. Since both are in the same table, we use a **SELF JOIN**.

### SQL Solution

```sql
SELECT 
    e.name AS Employee
FROM Employee e
INNER JOIN Employee m ON e.managerId = m.id
WHERE e.salary > m.salary;