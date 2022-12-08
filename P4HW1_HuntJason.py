# CTI-110
# P4HW1 -  Score List
# Jason Hunt
# 11/13/2022
# Get how many test scores they want and scores from user
# if score is less than 0 or greater than 100 display Invalid message
# Calculate the lowest grade, and score avg
# Remove the lowest grade from list
# Display lowest score, modified list, score average, and grade letter 

count = int(input('How many scores do you want to enter? '))

i=1
score_list=[]

while(True):
    if (len(score_list)==count):
        break
    print("Enter score #" + str(i) + ": ", end=" ")
    score = int(input())
    if (score < 0 or score > 100):
        print("INVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        print("Enter score #" + str(i) + " again:", end=" ")
        score = int(input())
        score_list.append(float(score))
        i += 1
    else:
        score_list.append(float(score))
        i += 1

lowest_grade = min(score_list)
score_list.remove(lowest_grade)
score_avg = sum(score_list) / len(score_list)

if (score_avg >= 90):
    grade_letter = "A"
elif (score_avg >= 80):
    grade_letter = "B"
elif (score_avg >= 70):
    grade_letter = "C"
elif (score_avg >= 60):
    grade_letter = "D"
else:
    grade_letter = "F"

print("\n----------------Results----------------")
print("Lowest Score :", lowest_grade)
print("Modified List:", score_list)
print("Score Average:", f'{score_avg: .2f}')
print("Grade        :", grade_letter)
print("---------------------------------------")

    
