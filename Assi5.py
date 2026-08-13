students = []

for i in range(3):

    print("\nStudent", i + 1)

    Roll = input("Enter Rollno. = ")

    name = input("Enter Name: ")

    sub1 = int(input("Enter subject 1 marks= "))
    sub2 = int(input("Enter subject 2 marks= "))
    # sub3 = int(input("Enter subject 3 marks= "))
    # sub4 = int(input("Enter subject 4 marks= "))
    # sub5 = int(input("Enter subject 5 marks= "))

    total = sub1+sub2

    
    percentage = total / 2

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    students.append([Roll, name, total, percentage, grade])



for i in range(3):
    for j in range(i + 1, 3):

        if students[i][1] < students[j][1]:

            temp = students[i]
            students[i] = students[j]
            students[j] = temp



for i in range(3):

    if i > 0 and students[i][1] == students[i - 1][1]:
        rank = students[i - 1][4]
    else:
        rank = i + 1

    students[i].append(rank)



print(f"{'Roll':<7}{'Name':<15}{'Total':<10}{'Percentage':<15}{'Grade':<8}{'Rank'}")
print("-" * 63)

for student in students:
    print(f"{student[0]:<7}{student[1]:<15}{student[2]:<10}{student[3]:<15.2f}{student[4]:<8}{student[5]}")