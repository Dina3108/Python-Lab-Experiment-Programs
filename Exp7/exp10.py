n=int(input('Enter No of Students:'))
sd={}
for i in range(n):
    name=input('Enter Name of the Student :')
    sd[name]=int(input('Enter Mark of the Student :'))
print('\n---Students who scored above 80---\n')
for x,y in sd.items():
    if y>80:
        print(x)