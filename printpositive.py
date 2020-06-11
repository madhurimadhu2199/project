List = []
n = int(input("Enter the list size : "))
for i in range(0, n):
    item = int(input())
    List.append(item)
print(List)
while n!=0:
  if List[n-1]<0:
   del List[n-1]
  n=n-1
print(List)
  


