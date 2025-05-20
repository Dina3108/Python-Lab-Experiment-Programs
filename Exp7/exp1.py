n=int(input('Enter No of Elements in the Set:'))
set1=set({})
for x in range(n):
    set1.add(input(f"Enter Element {x+1}: "))
print('\n---Operations in Set---\nEnter 1 to Add an Element\nEnter 2 to remove an Element\nEnter 3 to check for membership\nEnter 4 to clear the set\nEnter 5 to Exit')
is_running=True
while is_running:
    x=int(input("Enter your Choice : "))
    if x==1:
        set1.add(input("Enter Element to Add:"))
        print('Element Added',set1)
    elif x==2:
        set1.remove(input("Enter Element to remove :"))
        print('Element removed',set1)
    elif x==3:
        if input("Enter Element to Check :") in set1:
            print('Element Found..!',set1)
    elif x==4:
        set1.clear()
        print('---Set Cleared---')
    elif x==5:
        is_running=False
        print('\n---EXIT---\n')