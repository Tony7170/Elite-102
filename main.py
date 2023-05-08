import mysql.connector

conn = mysql.connector.connect(user='root', database='bank', password='antonio2008.')

cursor = conn.cursor()

import random

print("--Welcome to my bank!--")

global repeat
repeat = True

selectBal = ("SELECT Balance From info")
cursor.execute(selectBal)

savedBal = cursor.fetchone()[0]

acc_balance = []  

acc_balance.append(savedBal)

def deposit():
    print("**Depositing**")
    print("------------------")
    dep_amt = int(input("How much would you like to deposit? "))

    acc_balance.append(dep_amt)
    new_bal = sum(acc_balance)
  
    print(f'Your balance is now ${new_bal}!')
  
def withdraw():
    wit_amt = int(input("How much would you like to withdraw? "))
  
    balance = sum(acc_balance)
    if balance < wit_amt:
      print("Error... \nYour account balance is low.")
    elif balance >= wit_amt:
      new_bal = balance - wit_amt
      acc_balance.clear()
      acc_balance.append(new_bal)
      print(f'Your balance is now ${new_bal}.')
    
    
while repeat:
    
    prompt = input("What can I help you with today?(deposit, withdraw) ")
  
    if 'balance' in prompt:
      print_bal = (sum(acc_balance))
      print(f"Your balance is ${print_bal}")
  
    elif 'deposit' in prompt:
      deposit()
      
    elif 'withdraw' in prompt:
      withdraw()
  
    elif 'nothing' in prompt:
      print("Goodbye!")
      repeat = False
      break
    else:
      print("Choose 'balance', 'deposit', 'withdraw', or 'nothing'")

balance = acc_balance[0]
updateBal = ("UPDATE info SET Balance = (%s)")
cursor.execute(updateBal, (balance,))
conn.commit()

cursor.close()

conn.close()

 