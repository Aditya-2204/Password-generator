import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
symbols = "~!@#$%^&*()_+=-`\][|}{';?></.,"

letters = lower+upper+numbers+symbols

passwordSet = random.sample(letters, 8)
passwordset = passwordSet[0]+passwordSet[1]+passwordSet[2]+passwordSet[3]+passwordSet[4]+passwordSet[5]+passwordSet[6]+passwordSet[7]

print("The password created is:", passwordset)