# # # Butterfly patteron
# # n=5;
# # for i in range(1,n+1):
# #     print("*"*i ,end=" ")
# #     print(" "*(2*(n-i)),end="")
# #     print("*"*i);
# # for i in range(n,0,-1):
# #     print("*"*i ,end=" ");
# #     print(" "*(2*(n-i)),end="")
# #     print("*"*i)
    
    
    

# # # # Pascal's Triangle in Python

# n = 5 

# for i in range(n):
#     print(" " * (n - i), end="")
#     val = 1
#     for j in range(i + 1):
#         print(val, end=" ")
#         val = val * (i - j) // (j + 1)
#     print()
    
    
    
    
#     a=input("Enter your day: ");
# if a=="sunday":
#     print("This is first day");
# elif a=="Monday":
#     print("This is second day");
# elif a=="Tuesday":
#     print("This is third day");
# elif a=="Wednesday":
#     print("This is fourth day");
# elif a=="thursday":
#     print("This is fifth day ");
# elif a=="friday":
#     print("This is sixth day");
# elif a=="saturday":
#     print("This is seventh day");
# else:
#     print("This is not a day")