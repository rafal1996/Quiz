import sys
#Quiz game

def open_quiz(file_name, mode):  #open file
    try:
        file = open(file_name, mode)
    except IOError as e:
        print(f"Can't open file {file_name}. Game will be close.\n", e)
        input("Press the enter button to end the program")
        sys.exit()
    else:
        return file

def next_line(file):
    #return the next line of the file
    line = file.readline()
    line = line.replace('/', '\n')
    return line

def next_block(file):
    #return another block of data
    question = next_line(file)
    answer = []
    for i in range(4):
        answer.append(next_line(file))

    correct = next_line(file)
    if correct:
        correct = correct[0]
    return question, answer, correct

def welcome():
    print('\t\t Welcome in Quiz')


def main():
    text_file = open_quiz('question', 'r')
    welcome()
    score = 0
    question, answer, correct = next_block(text_file)
    while question:
        #ask question
        print(question)
        for i in range(4):
            print('\t', i+1, '-', answer[i])

        #get answer
        answer = input("Chose answer 1-4: ")

        #chceck answer
        if answer == correct:
            print("Good answer !!")
            score += 1
        else:
            print("Bad answer :( ")
            print("Score = ", score, '\n\n')

        #next question
        question, answer, correct = next_block(text_file)

    text_file.close()
    print('That was last question')
    print('Your score = ', score)

main()


