# Write your MySQL query statement below
SELECT s.student_id, s.student_name, a.subject_name, COUNT(e.student_id) AS attended_exams
FROM Students s
CROSS JOIN Subjects a
LEFT JOIN Examinations e ON (s.student_id = e.student_id and a.subject_name = e.subject_name)
GROUP BY 1,2,3
ORDER BY s.student_id , a.subject_name 
