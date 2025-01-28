# Write your MySQL query statement below
SELECT w.id
FROM Weather w, Weather w1
WHERE DATEDIFF(w.recordDate, w1.recordDate) = 1 and w.temperature > w1.temperature
