print("hey you just entered my computer quiz game! \nlet's see how much you know me \nall the best")

play=input("do you want to play?  ") # user input to cherck if the user wants to play the game or not 
score=0 # score is set to 0 at the start of the game.
if play != "yes": # if the condition is true then the code below will run and the program will end 
    quit()

print("okay! let's play :)")  # the user has entered yes so the game will continue 

answer1=input("what is my favorite color? brown/blue? ")# user input to check the answer of first question.

if answer1 == "brown":
    print("correct answer! you have earned 1 loyalty point!")
    score+=1 # if the answer is correct score will increase by 1 point 
else:
    print("wrong answer! the correct answer is brown") # if the answer is wrong it will print the correct answer and the score will not increase

answer2=input("what is my favorite food? rice/pasta? ")# user input to check the answer of second question.

if answer2 == "rice":
    print("correct answer! you have earned 1 loyalty point!")
    score+=1 # if the answer is correct score will increase by 1 point 
else:
    print("wrong answer! the correct answer is rice") # if the answer is wrong it will print the correct answer and the score will not increase

answer3=input("what is my favorite movie? saiyaara/3 idiots? ")# user input to check the answer of third question.

if answer3 == "saiyaara":
    print("correct answer! you have earned 1 loyalty point!")
    score+=1 # if the answer is correct score will increase by 1 point 
else:
    print("wrong answer! the correct answer is saiyaara") # if the answer is wrong it will print the correct answer and the score will not increase

answer4=input("what is my favorite song? tu jaane na/tum hi ho? ")# user input to check the answer of fourth question.

if answer4 == "tum hi ho":
    print("correct answer! you have earned 1 loyalty point!")
    score+=1 # if the answer is correct score will increase by 1 point 
else:
    print("wrong answer! the correct answer is tum hi ho") # if the answer is wrong it will print the correct answer and the score will not increase

answer5=input("what is my favorite car? range rover/bmw? ")# user input to check the answer of fifth question.

if answer5 == "range rover":
    print("correct answer! you have earned 1 loyalty point!")
    score+=1 # if the answer is correct score will increase by 1 point 
else:
    print("wrong answer! the correct answer is range rover") # if the answer is wrong it will print the correct answer and the score will not increase

answer6=input("what is my favorite phone? iphone/samsung? ")# user input to check the answer of sixth question.

if answer6 == "iphone":
    print("correct answer! you have earned 1 loyalty point!")
    score+=1 # if the answer is correct score will increase by 1 point 
else:
    print("wrong answer! the correct answer is iphone") # if the answer is wrong it will print the correct answer and the score will not increase

answer7=input("what is my age? 21/22?")# user input to check the answer of seventh question.

if answer7 == "22":
    print("correct answer! you have earned 1 loyalty point!")
    score+=1 # if the answer is correct score will increase by 1 point 
else:
    print("wrong answer! the correct answer is 22") # if the answer is wrong it will print the correct answer and the score will not increase

answer8=input("what is my birthdate? 20 may/21 june? ")# user input to check the answer of eighth question.

if answer8 == "20 may":
    print("correct answer! you have earned 1 loyalty point!")
    score+=1 # if the answer is correct score will increase by 1 point 
else:
    print("wrong answer! the correct answer is 20 may") # if the answer is wrong it will print the correct answer and the score will not increase

answer9=input("what is my dream city? melbourne/paris? ")# user input to check the answer of ninth question.

if answer9 == "melbourne":
    print("correct answer! you have earned 1 loyalty point!")
    score+=1 # if the answer is correct score will increase by 1 point 
else:
    print("wrong answer! the correct answer is melbourne") # if the answer is wrong it will print the correct answer and the score will not increase

answer10=input("what is my car's color? pearl white/black? ")# user input to check the answer of tenth question.

if answer10 == "pearl white":
    print("correct answer! you have earned 1 loyalty point!")
    score+=1 # if the answer is correct score will increase by 1 point 
else:
    print("wrong answer! the correct answer is pearl white") # if the answer is wrong it will print the correct answer and the score will not increase

print("you have completed the quiz your total score is ",score,"out of 10")# at the end of game the total score will be printed out of 10