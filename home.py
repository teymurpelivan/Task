#1
# user_height = float(input('Enter height in cm'))
# user_weight = float(input('Enter weight in kg'))
# recommended_weight = user_weight/(user_height**2)
# if recommended_weight < 18.5:
#     print('underweight')
# elif recommended_weight >=18.5 and recommended_weight <=25:
#     print('normal weight')
# elif recommended_weight >=25 and recommended_weight <=30:
#     print('overweight')
# else:
#     print('odesity')   
#2
# online_store = {}
# total = 0
# for x in range(0,2):
#     name = input('Name product')
#     price = float(input('Price product'))
#     tax=price*1.18
#     online_store[name]=tax
# for i in online_store.values():
#     total+=i
# if total > 50:
#     print('10 azn kupon qazandiniz')
# elif total >=100:
#     print('15 azn kupon qazandiniz')
# else:
#     print('bextinizi bir daha sinayin')
#3
# customer = int(input('1(car),2(plane),3(train)'))
# way = float(input('How many km'))
# if customer == 1:
#     print('Payment', way * 0.5)
# elif customer == 2:
#     print('Payment', way * 1)
# else:
#     print('Payment', way*2)    

#1      
# list_number = [1,2,3]
# a = 0
# while True:
#     try:
#         print(list_number[a])
#     except IndexError:
#         print('stop!')
#         break
#     a += 1
    
#2
# list_page = ['a','b','c']
# a = 0
# while a <= len(list_page):
#     if list_page[a]=="c":
#         continue
#     else:
#         print(list_page[a])
#     a+=1
         
#3
# a = 0
# while a < 9:
#     a += 1
#     print(a)        
    

#4
# keys = ('angel')
# for x in range(0,1):
#     password = input('Enter password')
#     if password == keys:
#         print('Password is correct')
#         break
#     if password != len(keys):
#         print('the password is incorrect, 3 attempts left')
#     password = input('Enter password')
#     if password != len(keys):
#         print('the password is incorrect, 2 attempts left') 
#     password = input('Enter password ')    
#     if password != len(keys):
#         print('the password is incorrect, 1 attempts left')       
# else:
#     print('The user is blocked')

#5
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

 
    
# a = ['Aslan','Fuad','Ali']

# choise = input(" (1) Ad Daxil edin (2) Ad Silin :")

# if choise == '1':
#     ad = input("Ad Daxil edin : ")
#     if ad == '':
#         print(" Zehmet olmasa Ad Daxil edin")
#     elif len(ad) > 15:
#         print("Maksimum 15 daxil edin  ")
#     else:
#         a.append(ad)
#         print(a)
# if choise == '2':
#     ad = input("Silmek istediyiniz adi daxil edin : ")
#     if ad == '':
#         print(" Zehmet olmasa Ad Daxil edin")
#     elif ad not in a:
#         print("Daxil etdiyiniz ad listde movcud deyil")
#     else :
#         a.remove(ad)
#         print("Ugurla Silindi ")

    
    

              