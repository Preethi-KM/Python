# Reversea string

# a=input("Enter any string")
# rev=""
# for i in a:
#     rev=i+rev
# print(rev)


# a=input("Enter any string")
# print(a[::-1])



# a=int(input("Enter any number"))
# if a>=2:
#     for i in range(2,a):
#         if a%i==0:
#             print("not prime")
#             break
#     else:
#             print("prime")
# else:
#      print("Not prime")
        
    
    
    
    
    
    
    
# a=[1,2,3,4,5,69.8]
# b=list(set(a))
# b.sort()
# print(b[-2])



a=[1,2,3,7,9,11]
large=a[0]
for i in a:
    if i>large:
        large=i
print(large)
