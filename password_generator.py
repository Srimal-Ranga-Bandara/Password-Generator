import random

letter=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numbers=["0","1","2","3","4","5","6","7","8","9"]
symbol = ["!","@","#","$","%","^","&","*"]

letters_need=int(input("How many letters do you want to generate? "))
numbers_need=int(input("How many numbers do you want to generate? "))
symbols_need=int(input("How many symbols do you want to generate? "))

password =""

#Get Letter
for a in range(0,letters_need):
    x=random.choice(letter)
    password+=x

for b in range(0,numbers_need):
    x=random.choice(numbers)
    password+=x

for c in range(0,symbols_need):
    x=random.choice(symbol)
    password+=x

print(password)
    
