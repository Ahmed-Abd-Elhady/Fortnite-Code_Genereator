import random, string
import webbrowser
import time
import requests
import os
import base64


os.system("cls")
os.system(
    "FORTNITE CODES GENREATOR BY KONAFA")
print("======================================")
print("==Fortnite FREE CODES GENREATOR==")
print("======================================\n")
print("Code By Konafa\n")

num = input('How Many Codes to Generate: ')

f=open("Fortnite Codes.txt","w", encoding='utf-8')

print("Wait, Generating!")
      
for n in range(int(num)):
   y = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(20))
   f.write("https://www.epicgames.com/fortnite/ajax/redemption/validate-redemption-code?redeem-code=")
   f.write(y)
   f.write("\n")

f.close()

#=============Checker=========================


with open("Fortnite Codes.txt") as f:
    for line in f:
        fortnite = line.strip("\n")
        url = fortnite
        r = requests.get(url)

        if r.status_code == 304:
            print(" Valid | {} ".format(line.strip("\n")))
            break
        else:
        	print(" Invalid | {} ".format(line.strip("\n")))
a = input("Done....")

if a == "":
    exit()