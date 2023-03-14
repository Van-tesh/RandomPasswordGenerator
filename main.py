import random 
letters= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers= ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
Symbols= ['!', '@' ,'#', '$', '%', '&', '*', '+']

print ("Welcome to RandomPasswordGenerator")
nr_letters= int(input("How many letters would you like in your paswword? \n"))
nr_symbols= int(input(f"How many symbols would you like in your paswword? \n"))
nr_numbers= int(input(f"How many numbers would you like in your paswword? \n"))

pasword=[]
for char in range (1, nr_letters+1):
  pasword += random.choice(letters)

for char in range (1, nr_numbers+1):
  pasword += random.choice(numbers)
for char in range (1, nr_symbols+1):
  pasword += random.choice(Symbols)
  
random.shuffle(pasword)
print(''.join(pasword))