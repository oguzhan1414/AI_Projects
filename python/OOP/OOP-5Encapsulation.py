

class User():
    def __init__(self,username,password):
        self.username = username
        self.__password = password

    def get_password(self):
        return "****"

    def set_password(self,new_Password):
        if len(new_Password) >= 8:
            self.__password = new_Password
            print("Password updated succesfully")
        else:
            print("Password must be all leat 8 characters")
user = User("Oguzhan","1234567")
print(user.username)
print(user.get_password())
user.set_password("oguzhanSS")
print(user.get_password())


class Account:
    def __init__(self,balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self,newBalance):
        if newBalance >= 0:
            self.__balance = newBalance
            print("Balance updated succesfully")
        else:
            print("Invalid balance value")

account = Account(1000)
print(account.get_balance())
account.set_balance(1500)
print(account.get_balance())


class Kullanici:
    def __init__(self,username):
        self.__username = username
        self.__password = None

    def set_password(self,password):
        if len(password)<6:
            print("Password must be at least 6 characters long")
        else:
            self.__password = password
            print("Password set successfully")

    def get_password(self):
        return self.__password

user = Kullanici("Alice")
user.set_password("password123")
print(user.get_password())
