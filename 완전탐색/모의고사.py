def solution(answers):
    student_1 = [1,2,3,4,5]
    student_2 = [2,1,2,3,2,4,2,5]
    student_3 = [3,3,1,1,2,2,4,4,5,5]

    students = [0,0,0]
    for i in range(len(answers)):
        if answers[i] == student_1[i%5] : students[0]+=1
        if answers[i] == student_2[i%8] : students[1]+=1
        if answers[i] == student_3[i%10] : students[2]+=1
    return [i+1 for i in range(len(students)) if students[i] == max(students)]
