# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # num=5;
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # while num>0:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     print(num);
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     num=num-1;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # num=0;
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # while num<=10:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     print(num);
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     num=num+2;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # num=0;
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # while num<=10:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     if num%2==0:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         print("even",num)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     num=num+1;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # ans="";
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # while ans!="python":
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     ans=input("What is the best programming language");
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print("Correct")


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # amma="";
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # while amma!="you":
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     amma=input("Who is the best in this world");
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print("I like you mom")



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # secrete=7;
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # guess=0;
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # while guess!=secrete:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #     guess=int(input("Guess the number between 1 to 10"));
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # print("You guessed it");



# # # # # # # # # # # # # # # # # # # # # # # # # # # # ****
# # # # # # # # # # # # # # # # # # # # # # # # # # # # *33*                    <=output
# # # # # # # # # # # # # # # # # # # # # # # # # # # # *33*
# # # # # # # # # # # # # # # # # # # # # # # # # # # # ****


# # # # # # # # # # # # # # # # # # # # # # # # # # transfer statement using while continue and break
# # # # # # # # # # # # # # # # # # # # # # # # # # # while num<=10:
# # # # # # # # # # # # # # # # # # # # # # # # # # #     print("2",)


# # # # # # # # # # # # # # # # # # # # # # # # # i = 1
# # # # # # # # # # # # # # # # # # # # # # # # # while i<=4:   
# # # # # # # # # # # # # # # # # # # # # # # # #     if i==1 or i==4:
# # # # # # # # # # # # # # # # # # # # # # # # #         print("****")   
# # # # # # # # # # # # # # # # # # # # # # # # #     else:
# # # # # # # # # # # # # # # # # # # # # # # # #         print("3**3")   
# # # # # # # # # # # # # # # # # # # # # # # # #     i+=1



# # # # # # # # # # # # # # # # # # # # # # # # for i in range(10):
# # # # # # # # # # # # # # # # # # # # # # # #     print("*" * i)


# # # # # # # # # # # # # # # # # # # # # # # # for i in range(5):
# # # # # # # # # # # # # # # # # # # # # # # #     for i in range(5):
# # # # # # # # # # # # # # # # # # # # # # # #         print('*' ,end="")
# # # # # # # # # # # # # # # # # # # # # # # #     print()
    
    

# # # # # # # # # # # # # # # # # # # # # # # for i in range(5):
# # # # # # # # # # # # # # # # # # # # # # #     for j in range(5):
# # # # # # # # # # # # # # # # # # # # # # #         print('*'*j)
# # # # # # # # # # # # # # # # # # # # # # #         print()



# # # # # # # # # # # # # # # # # # # # # # n=5;
# # # # # # # # # # # # # # # # # # # # # # for i in range(n,0,-1):
# # # # # # # # # # # # # # # # # # # # # #     print("*" *1)



# # # # # # # # # # # # # # # # # # # # # assign =>butterfly pattern

# # # # # # # # # # # # # # # # # # # pyramid

# # # # # # # # # # # # # # # # # # a=int(input("Enter any number"));
# # # # # # # # # # # # # # # # # # fact=1;
# # # # # # # # # # # # # # # # # # for i in range(1,a+1):
# # # # # # # # # # # # # # # # # #     fact=fact*i;
# # # # # # # # # # # # # # # # # # print(fact);

# # # # # # # # # # # # # # # # # correct="1234";
# # # # # # # # # # # # # # # # # att=0;
# # # # # # # # # # # # # # # # # while att<3:
# # # # # # # # # # # # # # # # #     pin=input("Enter your pin:")
# # # # # # # # # # # # # # # # #     if pin==correct:
# # # # # # # # # # # # # # # # #         print("Acces granted");
# # # # # # # # # # # # # # # # #         break;
# # # # # # # # # # # # # # # # #     else:
# # # # # # # # # # # # # # # # #         print("Incorrect PIN");
# # # # # # # # # # # # # # # # # else:
# # # # # # # # # # # # # # # # #     print("Blocked");
    
# # # # # # # # # # # # # # # # # # We can use else with looping statement also



# # # # # # # # # # # # # # # correct="1234";
# # # # # # # # # # # # # # # attempt=0;
# # # # # # # # # # # # # # # while attempt<3:
# # # # # # # # # # # # # # #     pin=input("Enter your pin");
# # # # # # # # # # # # # # #     if pin==correct:
# # # # # # # # # # # # # # #         print("Access granted");
# # # # # # # # # # # # # # #         break;
# # # # # # # # # # # # # # #     else:
# # # # # # # # # # # # # # #         print("Incorrect pin");
# # # # # # # # # # # # # # #         attempt=attempt+1;
# # # # # # # # # # # # # # # else:
# # # # # # # # # # # # # # #     print("Card blocked")
    
    
    
    
# # # # # # # # # # # # # # # checking the month
# # # # # # # # # # # # # # # food menue
# # # # # # # # # # # # # # month=["jana","Apri","August","june","decem"]
# # # # # # # # # # # # # # for i in month:
# # # # # # # # # # # # # #     if i =="june":
# # # # # # # # # # # # # #         print("The month of february has 28/29 days");
# # # # # # # # # # # # # #     elif i in ('apri','june','sep','nov'):
# # # # # # # # # # # # # #         print("The month of",i,"has 30 days")
# # # # # # # # # # # # # #     elif i in ("jana","march","may","july","aguest"):
# # # # # # # # # # # # # #         print("The month of",i,"has 31 days")
# # # # # # # # # # # # # #     else:
# # # # # # # # # # # # # #         print(i,"is not a valid month name")
        
        
        
# # a=input("Enter your day: ");
# # if a=="sunday":
# #     print("This is first day");
# # elif a=="Monday":
# #     print("This is second day");
# # elif a=="Tuesday":
# #     print("This is third day");
# # elif a=="Wednesday":
# #     print("This is fourth day");
# # elif a=="thursday":
# #     print("This is fifth day ");
# # elif a=="friday":
# #     print("This is sixth day");
# # elif a=="saturday":
# #     print("This is seventh day");
# # else:
# #     print("This is not a day")
    
    
    
    
    
# # # # # # # # # # # # a=5;
# # # # # # # # # # # # for i in range(1,a+1) :
# # # # # # # # # # # #     print("*" * i) 
    
    
    
# # # # # # # # # # # n=5;
# # # # # # # # # # # for i in range(n,0,-1):
# # # # # # # # # # #     print('*'*i)

# # # # # # # # # # a=5;
# # # # # # # # # # for i  in range(1,a+1):
# # # # # # # # # #     print('*'*i)
    
# # # # # # # # # n=5;
# # # # # # # # # for i in range(n,0,-1):
# # # # # # # # #     print("*"*i)


# # # # # # # # a=5;
# # # # # # # # for i in range(1,a+1):
# # # # # # # #     print(" "*(a-i)+"*" *i)




# # # # # # # a=5;
# # # # # # # for i in range(1,a+1):
# # # # # # #      print(" "*(a-i)+"* " *i)



# # # # # # # a=5;
# # # # # # # for i in range(1,a+1):
# # # # # # #     print('*'*i);



# # # # # a=5;
# # # # # for i in range(1,a+1):
# # # # #     print(" "*(a-i)+"*"*i);



# # # # # a=5;
# # # # # for i in range(a+1):
# # # # #     print(" "*(a-i)+"* "*i);
    

# # # # a=5;
# # # # for i in range(a,0,-1):
# # # #     print(" "*(a-i)+"* "*i);
    
    
# # # # a=5;
# # # # for i in range(1,a+1):
# # # #     print(" "*(a-i)+"* "*i)
# # # # for i in range(a-1,0,-1):
# # # #     print(" "*(a-i)+"* "*i);
    
    
# # answer="";
# # while answer!="python":
# #     answer=input("Which is the best language:");
# # print("coorect");





# # # ans="";
# # # while ans!="python":
# # #     ans=input("What is the best programming language:");
# # # print("Correct")



# # ans="";
# # while ans!="python":
# #        ans=input("Enter your best languege");
# # print("correct");



# # i=1;
# # while i<=4:
# #     if i==1 or i==4:
# #         print("****");
# #     else:
# #         print("*33*");
# #     i=i+1;
    
    
    
    
    

# # i = 1
# # while i<=4:   
# #     if i==1 or i==4:
# #         print("****")   
# #     else:
# #         print("3**3")   
# #     i+=1




# for i in range(5):
#     for j in range(i):
#         print("*", end="");
#     print();
    
    
    
    
    
# a=5;
# for i in range(1,a+1):
#     print(" "*(a-i)+"*"*i);




a=5;
for i in range(1,a+1):
    print(" "*(a-i)+"* "*i)