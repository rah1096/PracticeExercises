import locale

universities = [
    ['California Institute of Technology', 2175, 37704], ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732], ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551], ['Stanford', 19535, 40569], ['Yale', 11701, 40500]
]

def enrollment_stats(list_of_lists):
    enrolled = []
    tuition = []
    total_enrolled = 0
    total_tuition = 0
    for i in list_of_lists:
        enrolled.append(i[1])
        tuition.append(i[2])
        total_enrolled += i[1]
        total_tuition += i[2]
    return sorted(enrolled), sorted(tuition), total_enrolled, total_tuition

students_list = enrollment_stats(universities)[0]
tuition_list = enrollment_stats(universities)[1]

total_students = enrollment_stats(universities)[2]
total_tuition = enrollment_stats(universities)[3]


def mean(students_list):
    total = 0
    count = 0
    for i in students_list:
        total += i
        count += 1
    return total/count

def median(students_list):
    list_len = len(students_list)
    list_even = students_list[(list_len - 1) / 2] + students_list[((list_len - 1) / 2) + 1]
    list_odd = students_list[((list_len + 1) / 2) -1]
    if list_len % 2 == 0:
        return list_even/2
    else:
        return list_odd



print students_list
print mean(students_list)
print median([1, 2, 3, 4, 5, 6, 7, 8])


print '*************************'
print 'Total students: ', total_students
print 'Total tuition: ', '$', total_tuition
print ''
print 'Student mean: ', mean(students_list)
print 'Student median: ', median(students_list)
print ''
print 'Tuition mean: ', '$', mean(tuition_list)
print 'Tuition mean: ', '$', median(tuition_list)
print '*************************'
