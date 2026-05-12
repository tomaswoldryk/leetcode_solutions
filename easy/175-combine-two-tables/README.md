# 175. Combine Two Tables

## Problem Statement (Enunciado)

Table: Person
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| personId    | int     |
| lastName    | varchar |
| firstName   | varchar |
+-------------+---------+

Table: Address
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| addressId   | int     |
| personId    | int     |
| city        | varchar |
| state       | varchar |
+-------------+---------+

Write a solution to report the first name, last name, city, and state of each person in the Person table. If the address of a personId is not present in the Address table, report null instead.

## Example

Input:
Person table:
| personId | lastName | firstName |
| 1        | Wang     | Allen     |
| 2        | Alice    | Bob       |

Address table:
| addressId | personId | city          | state    |
| 1         | 2        | New York City | New York |

Output:
| firstName | lastName | city          | state    |
| Allen     | Wang     | null          | null     |
| Bob       | Alice    | New York City | New York |

## Solution Approach

Use LEFT JOIN to keep all persons even if they have no address.

## Complexity

- Time: O(n + m)
- Space: O(n)

## Related Problems

- 1378. Replace Employee ID With The Unique Identifier