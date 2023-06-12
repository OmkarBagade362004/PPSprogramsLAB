# sub1 = float(input("Enter your marks in first Subject: "))
# sub2 = float(input("Enter your marks in second Subject: "))
# sub3 = float(input("Enter your marks in third Subject: "))
# sub4 = float(input("Enter your marks in forth Subject: "))
# sub5 = float(input("Enter your marks in fifth Subject: "))

# print("\n")
# total = sub1 + sub2 + sub3 + sub4 + sub5 
# print("You scored ",total," marks")

# avg = total/5
# print("Your average marks",avg)

# if (avg == 0 or avg < 40):
#      print("You Failed")
# elif(avg >=40 and avg < 50):
#      print("Third division")
# elif(avg >=60 and avg < 75):
#      print("Second division")
# elif(avg >=75 and avg <= 100):
#      print("First division")
# else :
#      print("Invalid Input! ")

                                    # using list
                              
marks_list = []
m = int(input("enter number of subjects: "))
for i in range(0,m):
     print("Enter your marks here:")
     item = int(input())
     marks_list.append(item)
print('\n')
print('the marks you scored in each subjects: ',marks_list)
print('\n')

total = 0
for j in marks_list:
     total += j
print("your total score is: ",total)

avg = total/m
print("Your average score is:",avg)

if (avg == 0 or avg < 40):
     print("You Failed")
elif(avg >=40 and avg < 50):
     print("Third division")
elif(avg >=60 and avg < 75):
     print("Second division")
elif(avg >=75 and avg <= 100):
     print("First division")