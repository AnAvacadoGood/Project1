#Programmed by Miko Tonthat
#Date: 07/16/19
#Description: This program takes a file that contains the student's answers to a test and decides which questions are wrong/correct and if you passed/failed the exam.

#gets rid of the brackets on questions wrong
def display_list(items):
    result = ""
    for item in items:
        result = result + str(item) + ", "
    result = result[: len(result) - 2]
    return result

#main program
def main():
    #answers
    correct_answers = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B', 'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']
    filename = input('Name of the student answers file: ') 
    student_answers = open(filename, 'r')
    student_test = []
    correct = 0
    wrong = 0
    wrong_list = []
    #takes the student's answers and strips \n
    for line in student_answers:
        line = line.strip()
        student_test.append(line)
    #closes file
    student_answers.close()
    #changes the amount of answers wrong/correct
    for i in range(len(correct_answers)):
        if student_test[i] == correct_answers[i]:
            correct += 1
        else:
            wrong_list.append(i + 1)
            wrong +=1
    #outputs amount of questions correct/wrong
    print("You got", correct, "questions correct.")
    print("You got", wrong, "question wrong.")
    #decides if you failed the exam
    if correct >= 15:
        print("You passed the exam.")
    else:
        print("You failed the exam.")
    #prints the question number you got wrong
    print("Questions you got wrong: ", display_list(wrong_list)) 
main()

