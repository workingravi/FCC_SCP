class Category:
  
  def __init__(self, cat_name):
    self.categ = cat_name
    self.ledger = []
    self.cumsum = 0

  def __str__(self):
    l = len(self.categ)
    rem = (30-l)//2
    s = ('*' * rem) + self.categ + ('*' * rem) + '\n'
    for d in self.ledger:
      amnt =  d['amount']
      des =  d['description']
      if len(des)>23:
        des = des[:23]
      s += f'{des:<23}{amnt:7.2f}'+'\n'
    s += f'Total: {self.cumsum}'
    return s

  def deposit(self, amount, desc=""):
    self.ledger.append({"amount":amount, "description":desc})
    self.cumsum += amount

  def withdraw(self, amount, desc=""):
    if amount <= self.cumsum:
      self.ledger.append({"amount":-1*amount, "description":desc})
      self.cumsum -= amount
      return True
    else:
      return False

  def get_balance(self):
    return self.cumsum
  
  def transfer(self, amount, target):
    dstr = f'Transfer to {target.categ}'
    if self.withdraw(amount, dstr):
      sstr = f'Transfer from {self.categ}'
      target.deposit(amount, sstr)
      return True
    else:
      return False
  
  def check_funds(self, amount):
    return False if amount > self.cumsum else True
    

def create_spend_chart(categories):
  spend = []
  for category in categories:
    temp = 0
    for item in category.ledger:
      if item['amount'] < 0:
        temp += abs(item['amount'])
    spend.append(temp)
  
  total = sum(spend)
  percentage = [i/total * 100 for i in spend]

  s = "Percentage spent by category"
  for i in range(100, -1, -10):
    s += "\n" + str(i).rjust(3) + "|"
    for j in percentage:
      if j > i:
        s += " o "
      else:
        s += "   "
    # Spaces
    s += " "
  s += "\n    ----------"

  cat_length = []
  for category in categories:
    cat_length.append(len(category.categ))
  max_length = max(cat_length)

  for i in range(max_length):
    s += "\n    "
    for j in range(len(categories)):
      if i < cat_length[j]:
        s += " " + categories[j].categ[i] + " "
      else:
        s += "   "
    # Spaces
    s += " "

  return s
