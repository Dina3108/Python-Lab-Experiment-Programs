dict1={'Name':'Dinakar','Marks':99}
x=input('Enter U to Update/D to remove key-value pair:')
if x.lower()=='d':
 dict1.pop(input('Enter Key name to delete key-value pair:').capitalize())
elif x.lower()=='u':
 dict1.update({input('Enter key to Update:').capitalize():input('Enter Value to Update:')})
print('\n---Updated Dictionary---\n',dict1)