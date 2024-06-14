from colorama import Fore
print(Fore.CYAN)
class Account(): #Class
    def __init__(self,owner,balance=0): #Class Constructor/ Special Method
        self.owner=owner #Attributes
        self.balance=balance 
    def deposit(self,dep_amt):  #Methods                                        
        self.balance+=dep_amt
        print(f"Added Rs.{dep_amt} to the balance.")
    def withdrawal(self,wd_amt):
        if self.balance>=wd_amt:
            self.balance-=wd_amt 
            print("Withdrawal accepted!")
        else:
            print("Sorry non enough funds!")
    def __str__(self):
        return f"Owner    : {self.owner} \nBalance : {self.balance}"
import fontstyle
print("------------------------------------------------------------------------------------------------------------------------")
print("                                                                   "+fontstyle.apply('PSU Banks in India 2023','bold/Verdana/green'))
print(Fore.CYAN+"------------------------------------------------------------------------------------------------------------------------")
print("\n")
name=str(input("Enter your name   :   "))
print("\n")
bank_name=str(input("Enter the name of your bank   :   "))
if bank_name=="State Bank of India" or bank_name=="Punjab National Bank" or bank_name=="Bank of Baroda" or bank_name=="Canara Bank" or bank_name=="Union Bank of India" or bank_name=="Bank of India" or bank_name=="Indian Bank" or bank_name=="Central Bank" or bank_name=="Indian Overseas Bank" or bank_name=="UCO Bank" or bank_name=="Bank of Maharashtra" or bank_name=="Punjab & Sindh Bank":
    print("Ok")
else:
    print(False)
    print("Sorry! No information available about this bank in the database.")
    bank_name=str(input("Again enter the name of your bank   :   "))
bank_balance=int(input("\nEnter your bank balance   :   "))
bank_deposit=int(input("\nEnter the amount of to be deposited   :   "))
print("\n")
bank_data=Account(name,bank_balance)     #Instance or Object
bank_data.deposit(bank_deposit)
print(bank_data)
print("\n")
withdraw=int(input("Enter the amount of money you want to withdraw   :   "))
print("\n")
bank_data.withdrawal(withdraw)
print(f"Bank   :   {bank_name}")
print(bank_data)
print("\n")
print("------------------------------------------------------------------------------------------------------------------------")
print("                                                                   "+fontstyle.apply('PSU Banks in India 2023','bold/green'))
print(Fore.CYAN+"------------------------------------------------------------------------------------------------------------------------")
s=input(fontstyle.apply("ENTER TO EXIT","bold/Broadway/violet/YELLOW_BG"))
exit()

