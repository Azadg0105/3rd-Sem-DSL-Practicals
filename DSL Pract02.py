# To compute net amount of your Bank Account

Amount = 0
while True:
  str = input("Enter transaction: ")
  trans = str.split(" ")

  type = trans[0]
  amt = int(trans[1])

  if type == "D" or type == "d":
    Amount += amt
  elif type == "W" or type == "w":
    Amount -= amt
  else:
    pass

  str = input("Press Y to continue else press any key to End Transaction: ")
  if not (str[0] =="Y" or str[0] =="y"):
    break

print("Net amount: ", Amount)
