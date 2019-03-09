def compare_subjects_within_student(subj1_all_students,
                                    subj2_all_students):
    """
    Compare the two subjects with their students and print out the "preferred"
    subject for each student. Single-subject students shouldn't be printed.

    Choice for the data structure of the function's arguments is up to you.
    """
    relevant_students = set(subj1_all_students.keys()).intersection(set(subj2_all_students.keys())) 
    for student in relevant_students:
        max1 = max(subj1_all_students[student])
        max2 = max(subj2_all_students[student])
        if max1 > max2:
            print(student + ' subj_1')
        elif max2 > max1:
            print(student + ' subj_2')
        else:
            print(student + ' equal')


subj1_all_students = {'J.T.Kirk': [75, 80], 
                      'Spock': [37,20], 
                      'A.Chakov': [100,90],
                      'Scoty': [70,80],
                      'C.Pyke': [10,40]}
subj2_all_students = {'J.T.Kirk': [39, 50], 
                      'Spock': [90,10], 
                      'A.Chakov': [80,99],
                      'Scoty': [77,57],
                      'N.Uhura': [10,10]}
compare_subjects_within_student(subj1_all_students,subj2_all_students)