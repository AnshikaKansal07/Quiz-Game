print("Welcome to trivia quiz!")
reply=input("Do you want to play? ").lower().strip()
if reply != "yes":
    quit()
print("Awesome! Let's start ")
count=0
ans=input("What is the capital of India? ").lower().strip()
if ans == "delhi":
    print("Correct answer")
    count=count+1
else:
    print("Wrong answer")
ans=int(input("How many continents are there on Earth? "))
if ans == 7 :
    print("Correct answer")
    count=count+1
else:
     print("Wrong answer")
ans=input("What is the closest planet to Sun? ").lower().strip()
if ans == "mercury":
    print("Correct answer")
    count=count+1
else:
    print("Wrong answer")
ans=int(input("What is the square root of 64? "))
if ans == 8 :
    print("Correct answer")
    count=count+1
else:
     print("Wrong answer")
ans=input("What does CPU stand for? ").lower().strip()
if ans  == "central processing unit":
    print("Correct answer")
    count=count+1
else:
    print("Wrong answer")    
print("You scored", count, "points")