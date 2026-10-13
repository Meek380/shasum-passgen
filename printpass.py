import os
import pyperclip

x = 0
password = ""

with open("sha.txt", "r") as file:
    data = file.read()
    list(data) == data.strip()
    for i in range(41):
    # while list(data)[x] == " ":
        password = password + list(data)[x]
        x = x + 1
    print(password)
    pyperclip.copy(password)
