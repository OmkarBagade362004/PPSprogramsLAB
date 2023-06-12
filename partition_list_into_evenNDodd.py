'''
creating a partition list program to tell the nmber of 
even and odd values in the lists appended by the user
'''
print("\n")

num1 = int(input("Enter your first list size: "))

list1 = []
for i in range(0,num1):   
     print("Enter the values at index",i)
     item1 = int(input())
     list1.append(item1)
     #checking even and odd values in the list appended

# for k in list1:
#           # print(k,end=" ")
#           if (k % 2 == 0):
#                print("even value: ",k)
#           elif (k % 2 != 0):
#                print("odd value: ",k)     
#           else:
#                print("values may be wrong!")    
# print(list1)

print('\n')

num2 = int(input("Enter your second list size: "))

list2 = []
for j in range(0,num2):   
     print("Enter the values at index",j)
     item2 = int(input())
     list2.append(item2)     
     #checking even and odd values in the list appended
# for k in list1:
#           # print(k,end=" ")
#           if (k % 2 == 0):
#                print("even value: ",k)
#           elif (k % 2 != 0):
#                print("odd value: ",k)     
#           else:
#                print("values may be wrong!")  
# print(list2)

print('\n')

total = []
total = list1 + list2
print("total list created is ",total)

for t in total: 
     if (t % 2 == 0):
          print("even value: ",t)      
     elif (t % 2 != 0):
          print("odd value: ",t)  
     else:
          print("values may be wrong!") 
 
print('\n')



