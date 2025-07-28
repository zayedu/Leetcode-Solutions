CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
SET N = N-1;
  RETURN (
      # Write your MySQL query statement below.
      SELECT DISTINCT(salary) FROM employee ORDER BY Salary desc
      LIMIT 1 OFFSET N
  );
END