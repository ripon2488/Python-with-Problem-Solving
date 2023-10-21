
''' Encapsulation Problem 1:
"Private attribute and public method"
Create a Python class BankAccount that represents a bank account. 
The class should have private attributes __account_number and __balance. 
Implement public methods get_account_number(), get_balance(), deposit(amount), 
and withdraw(amount) to access and modify these private attributes. 
Ensure that the withdraw method does not allow the account balance to go negative. 
Initialize the __balance attribute to 0 when a new account is created.

'''
class BankAccount():
    
    def __init__(self,__account_number,__balance=0):
        self.__account_number=__account_number
        self.__balance=__balance

    def get_account_number(self):
        print(f"Your Account Number is: {self.__account_number}")

    def get_balance(self):
        print(f"Balance of Account {self.__account_number} is: {self.__balance}")

    def deposit(self,amount):
        self.amount=amount
        self.__balance=self.__balance+self.amount
        return self.__balance
    
    def withdraw(self,amount):
        self.amount=amount
        if self.amount>self.__balance:
            print("Your Account Balance is lower then withdraw amount!")  
            return self.__balance        
        else:
            self.__balance=self.__balance-self.amount
            return self.__balance



bankaccount=BankAccount('123456')
bankaccount.get_account_number()
bankaccount.get_balance()

bankaccount.deposit(500)
bankaccount.get_balance()

bankaccount.withdraw(700)
bankaccount.get_balance()

bankaccount.withdraw(300)
bankaccount.get_balance()



''' Encapsulation Problem 2:
"Private attribute and public method"
Create a Python class Student that represents a student. 
The class should have private attributes __name, __age, and __roll_number. 
Implement public methods get_name(), get_age(), get_roll_number(), set_name(new_name), 
set_age(new_age), and set_roll_number(new_roll_number) to access and modify these private attributes. 
Ensure that the student's age is between 18 and 25, inclusive.
If an invalid age is provided, set the age to 18 by default. 
Implement a static method is_valid_age(age) that returns True if the provided age is valid (between 18 and 25) 
and False otherwise.
'''
print ('''
-------------------------------------
Encapsulation Problem 2:
"Private attribute and public method" 
-------------------------------------
''')
class Student:
    def __init__(self,__name, __roll_number, __age=18):
        self.__name = __name
        self.__age = __age
        self.__roll_number = __roll_number

    def get_name(self):
        print(f"Name of Student is : {self.__name}")

    def get_age(self):
        print(f"Age of Student is : {self.__age}")

    def get_roll_number(self):
        print(f"Roll Number of Student is : {self.__roll_number}")

    def set_name(self,new_name):
        self.new_name = new_name
        self.__name=new_name


    def set_age(self,new_age):
        self.new_age = new_age
        if is_valid_age(self.new_age):
            self.__age= self.new_age
        else:
            self.__age=18

    def set_roll_number(self,new_roll_number):
        self.new_roll_number = new_roll_number
        self.__roll_number=self.new_roll_number
@staticmethod
def is_valid_age(age):

    if 18 <=age<=25:
        return True
    else:
        return False
    
student=Student("Ripon",1)
student.get_name()
student.get_age()
student.get_roll_number()

student.set_name("Mr. Ripon")
student.get_name()

student.set_age(16)
student.get_age()

student.set_age(20)
student.get_age()

student.set_roll_number(2)
student.get_roll_number()