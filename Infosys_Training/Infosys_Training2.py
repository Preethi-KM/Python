#1.... Largest element in a list

# l=[1,2,8,9,11]
# b=sorted(a)
# print(l[-1])



#2... Largest element in a list without using slicing

# l=[1,3,2,4,7,6,8]
# max=l[0]
# for i in range(0,len(l)):
#     if l[i]>max:
#         max=l[i]
# print(max)



#3... Find the Smallest Element in a list with builtin

# a=[1,2,3,7,9,8]
# b=sorted(a)
# print(b[0])


#4... Find the smallest element  without builtin function

# l=[9,5,6,1,2,2,8]
# min=l[0]
# for i in range(0,len(l)):
#     if l[i]<min:
#         min=l[i]
# print(min)




#5.... Find the second largest element in a list with builtin

# l=[1,2,3,4,1,1,1,3,2,2,2]
# s=list(set(l))
# d=sorted(s)
# print(d[-2])



# 6....Find the  second largest without using buitin

# l=[10,10,40,70,80,60]
# max=l[0]

# for i in range(0,len(l)):
#     if l[i]>max:
#         max=l[i]
# second=float("-inf")
# for j in range(0,len(l)):
#     if l[j] !=max and l[j]>second:
#         second=l[j]
# print(second) 


# # 7.....Check if  list is sorted

# l=[1,4,3,2,6,7,8]
# is_sorted=True
# for i in range(0,len(l)):
#     if l[i]>l[i+1]:
#         is_sorted=False
#         break
# print("sorted" if is_sorted else "Not Sorted")  
    
    
    # or
# if is_sorted:
#     print("Sorted")
# else:
#     print("Not Sorted")



# Reverse the elements in a list without using builtin

# l=[1,2,3,4,5]
# n=len(l)
# for i in range(n//2):
#     l[i],l[n-i-1]=l[n-i-1],l[i]
# print(l)









