n=int(input("enter the number of employee ID"))
emp_id=[]

#ACCEPTING EMPLOYEE ID 

for i in range(n):
    emp_id.append(int(input("enter employee ID:")))

emp_id.sort()
print("sorted list",emp_id)

x=int(input("enter the employee ID to be searched"))
low=0
high=n-1
found=False

while low<=high:
    mid=(low+high)//2

    if emp_id==x:
        print("employeee ID found at",mid+1)
        found=True
        break

    elif x>=emp_id[mid]:
        low=mid +1

    else:
        high = mid-1

if found==False:
    print("employee ID not found")

   

