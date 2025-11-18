systemNumber = 10
guessNumber = input("tebak angka lo (1-10)...")
if(systemNumber) == int(guessNumber):
    print("You are win bro!")
else:
    print("ulangi lagi deh, salah nih")

import random
systemNumber = random.randint(1,11)
print(f"contekan nih bos: {systemNumber}")
guessNumber = input("tebak angka lo (1-10)...")
if(systemNumber) == int(guessNumber):
    print("You are win bro!")
else:
    print("ulangi lagi deh, salah nih")

# while True:
#     systemNumber = random.randint(1,11)
# print(f"contekan nih bos: {systemNumber}")
# guessNumber = input("tebak angka lo (1-10)...")
# if(systemNumber) == int(guessNumber):
#     print("You are win bro!")
# else:
#     print("ulangi lagi deh, salah nih")

keepRestart = True
while keepRestart:
    systemNumber = random.randint(1,10)
    print(f"contekan nih bos: {systemNumber}")
    guessNumber = input("tebak angka lo (1-10)...")
    if(systemNumber) == int(guessNumber):
        print("You are win bro!")
        keepRestart = False
    else:
        print("ulangi lagi deh, salah nih")