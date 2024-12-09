
# learn to save rojects or open new projrcts
# now i want to create students result file

#this was a continution from line 36 of reults.py file
# print("Exam Result")
# marks =34
# if marks >=35: #by putting red mark we are using break point
#     print("You passed the Exam!")
# if marks < 35:
#     print("you failed")
# after debugging we click f8 for every line so it will check and it passes
# at line 12 the debuger will exit as it is a false statement and no need to check it
# so for that pursose we dont write the second if condition we change it to else inted of if for line 11
print("exam result")
# marks=34
# if marks >= 35:
#     print("you have passed")
#
# else:
#     print(" you have failed ")
# after clicking on debuging the program will exit if the first conditon is true so it will not check else
 #we will talk about nested if so before that we will learn elif
# ELIF
# print("Exam result")
# marks=36
# if marks == 35:
#     print("You Are Promoted")
# elif marks > 35: # a situation in where you get 35 stamp marks the result will be different
#     print("YOu have passed exam")
# geerally there i nschools pre primary primary and upper primer types of schools will be there so based on standards
#based on preprimary students client can say if he get 35 exact you have to say promoted only based on the requirment we have to write the code
# if you want to provide grades for passed studnets we have to write again if statment
# print("Exam result")
marks=35
if marks == 35:
    print("You Are Promoted: Marks",marks)
elif marks > 35: # a situation in where you get 35 stamp marks the result will be different
    print("YOu have passed exam")
    if marks >=75 and  marks <=85 :
     print("You Got Good Marks:",marks)
    elif marks >85 and marks <=95: #for this to execute we have to write double condition other wise it will only print you got good marks
        print("you got great marks:",marks)
    elif marks>95:
        print("you got best marks:",marks)
else :
    print("you have failed marks:",marks)
    # now lets discuss about nested if
#now lets lear how to write double condition
# you have to write this statementif marks >=75 and <=85:
# for activating the grads
# if lopala inkoka if raste we call it nested if
