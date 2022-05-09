number_of_students = int(input("How many students are in the class?: "))
number_of_questions = int(input("How many questions are on the test?: "))

total = 0

for i in range(number_of_students):
    correct = int(input("How many questions did they get right?: "))
    testscore = correct/number_of_questions
    total = total + round(testscore*100, 0)

total = round(total/number_of_students, 0)
print(total)

#This is a demo I made for a friend to show how something like this would be accomplished. Nothing is really optimised!!!
