sd={}
for i in range(5):
 name=input(f'Enter Name {i+1} :')
 sd[name]=int(input('Enter Age :'))
print('\n---Name and Ages of 5 People---\n')
for x,y in sd.items():
        print(x,':',y)