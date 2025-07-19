print ("Welcome to Quiz Game")

playing = input ("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's Play :)")
score = 0

answer = input("1. What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print ("Incorrect!")

answer = input("2. What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print ("Incorrect!")

answer = input("3. Who is the GOAT? a. lionel messi b. pele c. maradona d. cristiano ronaldo " )
if answer.lower() == "d":
    print("Correct!")
    score += 1
else:
    print ("Incorrect!")

answer = input("4. What process is responsible for converting sunlight into energy in plants? ")
if answer.lower() =="photosynthesis":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("5. In what fictional town does SpongeBob SquarePants live? ")
if answer.lower() =="bikini bottom":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("6. Who painted the Mona Lisa? ")
if answer.lower() == "leonardo da vinci":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("7. What is the capital city of Japan? ")
if answer.lower() == "tokyo":
    score += 1
    print("Correct!")
else:
    print("Incorrect!")

answer = input("8. What is the largest ocean on Earth? ")
if answer.lower() == "pacific ocean":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("9. What is the name of the galaxy that contains our Solar System? ")
if answer.lower() == "milky way":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("10. Which country has won the most FIFA World Cup titles? ")
if answer.lower() == "brazil":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " out of 10 questions correct!")
print("You got " + str(score/10 * 100) + "%.")