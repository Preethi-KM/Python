# a=[1,2,3,4]
# for i in a:
#     print(i,end="")
    
# list=[1,2,3,4]
# if 5 in list:
#     print("found 5");
# else:
#     print("5 is not found")
    
    
    
# Find the largest element in an array

# r=[1,2,3,4,5,5];
# a=list(set(r))
# a.sort()
# b=a[-2]
# print("The largest elemet is ",b)


# a=[1,4,6,3,7,3,7,9]
# large=0
# for i in range(len(a)):
#     if i>large:
#         large=i
# print("The largest number is",large)
        
        
        
# a=[1,2,3,4,6,5];
# b=list(set(a))
# b.sort()
# c=b[-1]
# print(c)



# Reverse an string

# a=[1,2,3,4,5,6]
# reverse=a[::-1]
# print(reverse)



# a=[1,2,3,4,5,6]
# reverse=a[::-1]
# print(reverse)



# a=[1,2,3,4,5,6]
# rev=[]
# for i in range(len(a)-1,-1,-1):
#     rev.append(a[i])
# print(rev)


# Reverse a string
# a="preethi"
# b=a[::-1]
# print(b)


# without slicing

# a="preethi";
# rev=''
# for i in a:
#     rev=i+rev;
# print(rev)



# a=[3,4,5,65,1]
# b=list(set(a))
# b.sort()
# c=b[0]
# print(c)


# a=[1,23,4,5,6,6,0]
# small=a[0]
# for i in a:
#     if i<small:
#         small=i
# print(small)



# a=[1,2,3,4,5];
# sum=0
# for i in a:
#     sum=sum+i
# print(sum)



# count how many numbers ngreater than ngiven numbers

# target=3;
# list=[1,2,3,4,5,56,6,7];
# count=0
# for i in list:
#     if i>target:
#         count=count+1
# print(count)



# a=[1,2,3,4,5,4]
# if 4 in a:
#     print("found")



# a=[1,2,3,4,1,3,4,5];
# b=list(set(a))
# print(b)



a=[1,2,34,4,5,5,6,1,1,1,1,];
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)