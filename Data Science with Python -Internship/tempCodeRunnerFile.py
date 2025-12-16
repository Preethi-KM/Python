
try:
    f=open("preethi.txt","r")
    f.read()
except FileNotFoundError:
    print("This file is not found")