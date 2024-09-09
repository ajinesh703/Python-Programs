class Account:
  def __init__(self, owner, balance=0):
    self.owner = owner
    self.balance = balance
    
  def __str__(self):
    return f'Account owner: {self.owner}\nAccount balance: ${self.balance}'

  def deposite(self, dep_amt):
    self.balance += dep_amt
    print('Deposite Accepted')

  def withdraw(self, wd_amt):
    if self.balance >= wd_amt:
      self.balance -= wd_amt
      print('Withdrawal Accepted')

    else:
      print('Funds Unavailable!')

acc1 = Account('Jose',100)
acc1.deposite(150)
acc1.withdraw(800)

print(acc1)