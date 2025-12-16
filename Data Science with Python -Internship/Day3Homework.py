# # # # # Palindrome
# # # # # a="mam";
# # # # # if a==a[::-1]:
# # # # #     print("This is palindrome");
# # # # # else:
# # # # #     print("This is not a palindrome");
    
    
    
    
    
# # # # # a="mam";
# # # # # rev="";
# # # # # for i in a:
# # # # #     rev=i+rev;
# # # # # if rev==a:
# # # # #     print("This is palindrome");
# # # # # else:
# # # # #     print("This is not palindrome");





# # # # # # count the vowels
# # # # # a=input("Enter any string:");
# # # # # vowels="a,e,i,o,u";
# # # # # count=0;
# # # # # for i in a:
# # # # #     if i in vowels:
# # # # #         count=count+1;
# # # # # print(count);





# # # # # # print a maximum  and minimum list without using buitin function
 
# # # # # # list=[1,2,3,4,5,6,7,8];
# # # # # maximun=list[0];
# # # # # for i in list:
# # # # #     if i>max:
# # # # #         maximum=i;
# # # # # print(max);



 
# # # # # list=[1,2,3,4,5,6,7,8];
# # # # # mini=list[0];
# # # # # for i in list:
# # # # #     if i<mini:
# # # # #         mini=i;
# # # # # print(mini);
        
        


# # # # # All buit in strings
# # # # # case changing methods(6)

# # # # a="preethi";
# # # # print(a.capitalize())


# # # # a="PREETHI";
# # # # print(a.casefold());


# # # a="preethi";
# # # print(a.upper());


# # # a="PREETHI";
# # # print(a.lower());


# # # a="preethi welcome to our home";
# # # print(a.title());


# # # a="hELLO pREETHI";
# # # print(a.swapcase());

# # # a="sanjana"
# # # print(a.find("jan"));
# # # print(a.find("java"));




# # # a="sanjana"
# # # print(a.rfind("jan"));
# # # print(a.rfind("java"));





# # a="sanjana"
# # print(a.rfind("an"));
# # print(a.rfind("java"));


# a='preethi';
# print(a.index("ree"));



list=[1,2,3,4,5]
min=list[0];
for i in list:
    if i<min:
        min=i;
    print(min)
    
    
    
list=[1,2,3,4,5];
min=list[0];
for i in list:
    if i<min:
      min=i;
print(min);