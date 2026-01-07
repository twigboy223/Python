import time
import random 
print("this is my password generator")
time.sleep(1)
print("this will work but dont use it")
time.sleep(2)
start = input("do you want to generate a password? (yes, or no):       ")
if start == "yes":
    length = input("how long do you want you password to be? :     ")
    time.sleep(1)
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"
    password = random.sample(characters, int(length))
    print("the generated password is: ", password)
    restart = input("do you want to generate another password? (yes )")
if start == "no":
    print("fuck you why did you open it")
    quit()