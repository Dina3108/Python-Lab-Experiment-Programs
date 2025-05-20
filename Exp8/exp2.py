try:
    list1=[['Dina',100],['Hari__',200]]
    x=int(input('Enter Index Number to get Student Mark :'))
    print(f'{list1[x][0]}:{list1[x][1]}')
except IndexError:
    print("Invalid Index entered.Please try again.")