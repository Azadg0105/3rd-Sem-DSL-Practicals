# Write a Python program that computes the net amount of a bank account based a transaction
# log from console input. The transaction log format is shown as following: D 100 W 200
# (Withdrawal is not allowed if balance is going negative. Write functions for withdraw and deposit)
# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300, D 300 , W 200, D 100 Then, the output should be: 500

# To compute net amount of your Bank Account

Amount = 0
while True:
  str = input("\nEnter Transaction (d/w for deposit/withdrawal followed by Amount): ")
  trans = str.split(" ")

  type = trans[0]
  amt = int(trans[1])

  if type == "D" or type == "d":
    Amount += amt
  elif type == "W" or type == "w":
      if amt > Amount:
          print("\nYour Account Balance is Low, Rs.",Amount," only.")
      else:
          Amount -= amt
  else:
    pass

  str = input("\nPress Y to continue else press any key to End Transaction: ")
  if not (str[0] =="Y" or str[0] =="y"):
    break

print("\nYour available Balance is Rs.",Amount," only.")
