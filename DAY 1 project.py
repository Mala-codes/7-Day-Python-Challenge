Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import random
... import string
... 
... print("--- Day 1: Password Generator ---")
... 
... # Ask the user for the length of the password
... length = int(input("How many characters should the password have? "))
... 
... # Create a pool of letters, numbers, and symbols
... all_characters = string.ascii_letters + string.digits + string.punctuation
... 
... # Randomly select characters from the pool
... password = "".join(random.choice(all_characters) for i in range(length))
... 
... print(f"Your generated password is: {password}")
SyntaxError: multiple statements found while compiling a single statement
>>> 
= RESTART: C:/Users/THINKPAD/AppData/Local/Programs/Python/Python314/DAY 1 PROJECT .py
--- Day 1: Password Generator ---
How many characters should the password have? 24
Your generated password is: b3AWjr4rienb`7H]UjSp43*V
>>> 
= RESTART: C:/Users/THINKPAD/AppData/Local/Programs/Python/Python314/DAY 1 PROJECT .py

    *****************************************
    * *
    * [  SAFE-GEN PASSWORD SHIELD  ]     *
    * _________________            *
    * |                |            *
    * |      [ESC]     |            *
    * |________________|            *
    * *
    *****************************************
    
Welcome, Agent. Let's secure your digital life.
-----------------------------------------
Enter desired password length (e.g., 16): 8

[!] Initializing Security Protocols...
.
..
...

=========================================
  YOUR ENCRYPTED KEY:
  > q_2vKxKS
-----------------------------------------
  STRENGTH: 🟡 MEDIUM (Decent security)
=========================================

Project Day 1: COMPLETE. ✅
