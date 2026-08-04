#linear search
emp_id=[]
n = int(input("Enter the number of employee ID:"))

#accepting employee ID

for i in range(n):
    emp_id.append(int(input("enter employee ID:")))    
    
#linear search 

a=int(input("enter the number of employee ID to be searched"))

flag= 0  #employee ID not found yet


#search employee ID
for i in range(a):
   if emp_id[i]==a:
    print("employee ID found at position",i+1)    #i+1 for position as index take value from 0
    flag=1  #found one employee ID
    break

if flag==0:
  print("employee ID not found")

   


