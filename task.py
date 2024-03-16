#1      
list_number = [1,2,3]
a = 0
while True:
    try:
        print(list_number[a])
    except IndexError:
        print('stop!')
        break
    a += 1

#2
list_page = ['a','b','c']
a = 0
while a <= len(list_page):
    if list_page[a]=="c":
        continue
    else:
        print(list_page[a])
    a+=1
    
#3
a = 0
while a < 9:
    a += 1
    print(a)

#4
keys = ('angel')
for x in range(0,1):
    password = input('Enter password')
    if password == keys:
        print('Password is correct')
        break
    if password != len(keys):
        print('the password is incorrect, 3 attempts left')
    password = input('Enter password')
    if password != len(keys):
        print('the password is incorrect, 2 attempts left') 
    password = input('Enter password ')    
    if password != len(keys):
        print('the password is incorrect, 1 attempts left')       
else:
    print('The user is blocked')

print('Capital of Azerbaijan')
answer = int(input('1(a), 2(b), 3(c), 4(e)'))
choice = {
    'a':['Moskva'],
    'b':['Baki'],
    'c':['Vilnus'],
    'e':['Roma']
    }
if answer == 1:
    print(choice['a'], 'Wrong answer')
elif answer == 2:
    print(choice['b'],'Correct answer')
if answer == 3:
        print(choice['c'],'Wrong answer')
else:
    print(choice['e'],'Wrong answer')       