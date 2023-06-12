num_list = []       #creating an empty list 
n = int(input("Enter list size: "))     #inpput the size of the list 
for i in range(0,n):
     print("Enter number at index ",i," ")
     item = int(input())
     num_list.append(item) # ye toh pata hi hoga add karta hai items/elements ko list main
     
print("\n")         #to make output neat 
print("User list is ",num_list)
print("\n")          #to make output neat 

count = 0      #initial value iss zero to increment further in the code below
for j in num_list :
     count += j     #incrementing the count variable by the j variable which takes the elements 
                    #and separate them

avg = count/len(num_list)
maximum = max(num_list)       #max function is used to extract maximum value in the list
minimum = min(num_list)       #same min function bhi karta hai 

print("Sum of the elements in the list: ",count)
print("Average of the elements in the list: ",avg)
print("Maximum of the elements in the list: ",maximum)
print("Minimum of the elements in the list: ",minimum)

'''
time thoda jyada lag gaya approx 20 min. 

ab check karle output run ho rah ki nahi 
waise mere laptop pe toh ho rha hai 
'''



