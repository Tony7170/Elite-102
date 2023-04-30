import mysql.connector

connection = mysql.connector.connect(user='root', database='bank', password='antonio2008.')

cursor = connection.cursor()

import random

print("--Welcome to my bank!--")

repeat = True

testQuery = ('SELECT Balance FROM info')
balance = cursor.execute(testQuery)
balance = int(balance)
acc_balance = [balance]
acc_balance = sum(acc_balance)
  
def deposit():
    print("**Depositing**")
    print("------------------")
    dep_amt = int(input("How much would you like to deposit? "))

    acc_balance.append(dep_amt)
    new_bal = sum(acc_balance)
  
    print(f'Your balance is now {new_bal}!')
    return
  
def withdraw():
    wit_amt = int(input("How much would you like to withdraw? "))
  
    balance = sum(acc_balance)
    if balance < wit_amt:
      print("Error... \nYour account balance is low.")
    elif balance >= wit_amt:
      new_bal = balance - wit_amt
      acc_balance.clear()
      acc_balance.append(new_bal)
      print(f'Your balance is now {new_bal}.')
    return
    
    
while repeat:
    
    prompt = input("What can I help you with today? ")
  
    if 'balance' in prompt:
      print (acc_balance)
  
    elif 'deposit' in prompt:
      deposit()
      
    elif 'withdraw' in prompt:
      withdraw()
  
    elif 'nothing' in prompt:
      print("Goodbye!")
    else:
      print("Choose 'balance', 'deposit', 'withdraw', or 'nothing'")
    

cursor.execute(testQuery)

for item in cursor:

    print(item)

cursor.close()

connection.close()

 