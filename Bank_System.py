#creat account
Accounts = []
balance = 0
print("--------Welcome to our Bank--------")

print("-------creat your account--------")
def creat_account():
 while True : 
     user_name = input ("Enter your user name : ")
     password = input ("Enter your pass word : ")
     
     Found = False
     for i in Accounts:
        if i["User_name"] == user_name :
            print("The user name is already exist try again")
            Found = True   
     if not Found :
        print("done")
        Account = {"User_name":user_name,
           "Password":password,
           "Balance":balance}
        Accounts.append(Account)
        break

def login():
    while True :
        username= input("Enter your user name : ")
        password_ = input("Enter your password : ")
        Found = False
        for i in Accounts :
            if i["User_name"] == username and i["Password"] == password_ :
                Found = True
                while True:
                    print("log in succseful")
                    print(f"HI {username} your balance = {i['Balance']}")
                    print("------Bank Operation-----")
                    print("Enter 1 to make deposite")
                    print("Enter 2 to wuthdraw")
                    print("Enter 3 to log in with differnt acccount")
                    print("Enter 4 to creat new account")
                    print("Enter 5 to exsist")
                    choice = int(input("Enter your choice : "))


                    if choice == 1 :
                            while True :
                                amount = int(input("Enter the amount that you want to deposite : "))
                                if amount > 1000 or amount < 0 :
                                    print("Try again")
                                else :
                                    i["Balance"] +=amount
                                    break

                    elif choice == 2 :
            
                            while True :
                                withdraw = int(input("Enter your amount : "))
                                if withdraw > i["Balance"] or withdraw < 0 :
                                    print("There somthing wrong")
                                else :
                                    i["Balance"] -= withdraw
                                    break
                  
                    elif choice == 3 :
                        return login()

                    
                    elif choice == 4 :
                        return creat_account ( ),login()

                    
                    elif choice == 5 : 
                        print("bye")
                        return

                        
                    else :
                      print("Try again ")
            else : 
                  print("The user name or password is wrong try again")

              
creat_account ()
login()
