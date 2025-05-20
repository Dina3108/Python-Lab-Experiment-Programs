dict1={'Name':'Dinakar','Marks':99,'College':'KPRIET','Place':'Coimbatore'}
k=input('Enter key to search:').capitalize()
for x,y in dict1.items():
    if k==x:
        print(f'Key found its value : {y}')