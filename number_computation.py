import math

num = int(input("Enter a number: "))

initial = 1
while initial < 8:
     
     print("choose 'a' for square root of number")
     print("choose 'b' for squaring number")
     print("choose 'c' for cube of number")
     print("choose 'd' for checking number is prime or not")
     print("choose 'e' for factoial of number")
     print("choose 'f' for prime factors of the number")
     print("choose 'q' for quiting the program")

     choice = input("Enter your choice: ")
     choice_list = ['a','b','c','d','e','f','q']

     #sqrt
     if (choice == choice_list[0]):
          print("Square root of the number is ",math.sqrt(num))

     #sqr
     if (choice == choice_list[1]):
          print("Square of the number is ",math.pow(num,2))

     #cube
     if (choice == choice_list[2]):
          print("Cube if the number is ",math.pow(num,3))

     #prime number
     if (choice == choice_list[3]):
          if (num == 1):
               print(num,"is not a prime number")
          elif (num > 1):
               for i in range(2, num):
                    if (num % i):
                         print(num,"is not a prime number")
                         break
               else:
                    print(num,"is a prime number")
          else:
               print(num,"is not a prime number")

     #factorial
     if (choice == choice_list[4]):
          n = num
          factorial = 1
          if (n == 0):
               print(1)
          elif (n == 1):
               print(1)
          else:
               for i in range(1,n+1):
                    factorial = factorial * i
               print("factorial of number is ",factorial)

     #prime factors
     if (choice == choice_list[5]):
          n = num
          for j in range(2,n+1):
               if n % j == 0:
                    count = 1
                    for k in range(2,(j//2 + 1)):
                         if (j % k == 0):
                              count = 0
                              break
                    if (count ==1):
                         print(j)

     if (choice == choice_list[6]):
          break
          
     print("\n")

     