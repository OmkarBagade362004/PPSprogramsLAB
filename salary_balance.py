try:
     basic_pay = float(input("Enter your basic pay: "))
     hra = (10/100)*basic_pay
     ta = (5/100)*basic_pay
     
     if (basic_pay == 0):
          print("You are broke!")

     elif (basic_pay > 0):
          gross = basic_pay + hra + ta
          print("Your Gross salary is ",gross)

          pf_tax = (2/100)*gross
          print("Your professional tax is ",pf_tax)

          net_salary = gross - pf_tax
          print("Your net salary is ",net_salary)

     elif (basic_pay < 0):
          print("You are in debt!")
        
except :
     print("Invalid Input in the Basic Pay!")
