from Student import *

grades = [9, 13, 14, 8, 5, 8]

average_grades = calavg(grades)
max_grades = calmax(grades)
min_grades = calmin(grades)
status = calstatus(average_grades)

print(average_grades, max_grades, min_grades, status)