import random

letter=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numbers=["0","1","2","3","4","5","6","7","8","9"]
symbol = ["!","@","#","$","%","^","&","*"]

# print('''__________                                               .___   ________                                   __
# \______   \_____    ______ ________  _  _____________  __| _/  /  _____/  ____   ____   ________________ _/  |_  ___________
#  |     ___/\__  \  /  ___//  ___/\ \/ \/ /  _ \_  __ \/ __ |  /   \  ____/ __ \ /    \_/ __ \_  __ \__  \\   __\/  _ \_  __ \
#  |    |     / __ \_\___ \ \___ \  \     (  <_> )  | \/ /_/ |  \    \_\  \  ___/|   |  \  ___/|  | \// __ \|  | (  <_> )  | \/
#  |____|    (____  /____  >____  >  \/\_/ \____/|__|  \____ |   \______  /\___  >___|  /\___  >__|  (____  /__|  \____/|__|
#                 \/     \/     \/                          \/          \/     \/     \/     \/           \/                   ''')

#Get Input
letters_need=int(input("\nHow many letters do you want to generate? "))
numbers_need=int(input("How many numbers do you want to generate? "))
symbols_need=int(input("How many symbols do you want to generate? "))

password =""
Select_character=random.randint(0,3)
all_characters=letters_need+numbers_need+symbols_need

letter_cal=0
number_cal=0
symbols_cal=0


while letter_cal!=letters_need or number_cal!=numbers_need or symbols_cal!=symbols_need:

    Select_character = random.randint(0, 3)

    if letters_need>letter_cal and Select_character==0:
        x=random.choice(letter)
        password+=x
        letter_cal+=1

    elif numbers_need>number_cal and Select_character==1:
        x=random.choice(numbers)
        password+=x
        number_cal+=1

    elif symbols_need>symbols_cal and Select_character==2:
        x=random.choice(symbol)
        password+=x
        symbols_cal+=1

print(password)
    
