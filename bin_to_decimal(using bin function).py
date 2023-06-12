num = int(input("Enter number: ")) #user input 
l = [] #initial empty list
print('''decimal | binary | decimal''')

#appending a list here l[]
for i in range(1,num+1):
     l.append(i)

#for converting list into individual integers  
for j in l:  
     print(j,end="     ")

#decimal to binary
     decimal = j
     binary = bin(decimal)  # bin function converts decimal to binary with "0b" as prefix
     binary_without_prefix = binary.replace("0b","")#replace function replaces old string
     print(binary_without_prefix,end="     ")  

#binary to decimal
     decimal = int(binary, 2)
     print(decimal)

print("\n")    #just for neatness in the output



