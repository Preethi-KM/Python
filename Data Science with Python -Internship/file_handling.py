# file=open("notes.txt","r")
# context=file.read()
# print(context)
# file.close();


# file=open("notes.txt","r")
# context=file.read()
# print(context)
# file.close()



# file=open("notes.txt","w")
# file.write("ninna ashirvaada nanna mele sada irali thande")
# file.close();



# file=open("notes.txt","w")
# file.write("Ninnanne nambiruve thande kai bidabeda")
# file.write("\nivattu 11:11 ge bedikolluttene neraverisu thande")
# file.close()


# Read modes 
# read(size) ==>It reads the entire file as a string
# file=open("notes.txt","r")
# a=file.read()
# print(a)
# file.close()

# or
# no need to close

# with open("notes.txt","r") as file:
#     print(file.read())



# It reads the line by line
# with open("notes.txt","r") as file:
#     data=file.readline()
#     print(data)



# with open("notes.txt","r") as file:
#     print(file.readline())
#     print(file.readline())
#     file.read()


# with open("notes.txt","r") as file:
#     print(file.readlines())
#     print(file)





f=open("notes.txt","w")
print("Hello python")
f.close()