class Budget:
    category_record = [] 
    def __init__(self,category = '', balance = 0):
        self.category = category
        self.balance = balance
        #self.entertainment = entertainment

        Budget.category_record.append(self)

    def deposit(self, amount):
            #amount = input('How much do you wanna deposit ? ')
            self.balance += amount
            print(f'You have deposited {amount} into your {self.category} budget, your balance is {self.balance} ')
            return
        
    def withdraw(self, amount):
            if amount > self.balance:
                print("Insufficient funds")
            else:
                self.balance -= amount
                print(f'You have withdrawn {amount} from your {self.category} budget, your balance is {self.balance}')
                return
    def category_balance(self):
            print(f'Your balance is {self.balance} for your {self.category} budget')
        
    @staticmethod
    def transfer(amount, source, destination):
            source.withdraw(amount)
            destination.deposit(amount)
            

            
            
            
            #input('what budget account do you wanna add this to?' +
            #food, clothing, entertainment)

            
food = Budget('food')
clothing = Budget('clothing')
entertainment = Budget('entertainment')
rent = Budget('rent')

food.deposit(200)
rent.deposit(100)
Budget.transfer(100, food, rent)
print(food.balance)
print(rent.balance)
