str1=input('Enter String:').lower()
cd={}
count=0
for x in str1:
 for i in range(len(str1)):
  if x==str1[i]:
    count+=1
 cd[x]=count
 count=0  
print('\n---Frequency of Characters---\n')
for x,y in cd.items():
 print(f'{x} : {y}')
 