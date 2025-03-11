# ATM MINIPROJECT.........
#I John4:4(HE who is in me is greater than,he who is in the world)
# i am the way the truth and the life
#the joy the lord is my strength and shield

a='''
1.credit
2.debit
3.bankbalance
4.exit
'''

name="Harsha"
password="123"
print("WELCOME TO THE ATM PROGRAM")
balance=1000
user_name=input("Enter the user name:")
pass_word=input("Enter the password:")

if name==user_name  and  password==pass_word:
    while True:
        print(a)
        option=int(input("Choose the option :"))
        
        if option == 1:
            credit=float(input("Enter the amount to credit: "))
            balance+=credit
            
            if credit>0:
                print("The total balance is :",balance)
            else:
                print("Your credit should be more than '0'.Invalid...!")
        
        elif option == 2:
            debit=float(input("Enter the amount to debit: "))
            balance-=debit
            
            if debit<=0:
                print("Enter the positve money to draw. Invalid")
            else:
                print("The total balance is:",balance)
        
        elif option == 3:
           
            print("The total bankbalance is:",balance)
        elif option == 4:
            print("Exit the ATM")
            break
        
        elif option>4:
            print("Invalid option,please select the correct option")
        
else :
    print("invalid details")

