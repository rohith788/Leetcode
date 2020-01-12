select ( select distinct Salary from Employee Order by Salary Desc 
              Limit 1 Offset 1) as SecondHighestSalary; 