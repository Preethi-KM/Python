# DSA stands for data structures and algorithms .
# Datastructurs:It is a way of storing and organizing the data so that we can acces the data efficiently
# ALGORITHM:It is a stp by step procedure for solving a problem
        #    Why we need to learn data structure
# Efficient searching of data
# Efficient inseartion/deletion
# Efficient organization of data
# Better memory management
        #  Types of data structure
# Thre are 2 types of data structures are there
# 1 Premitive data structure
# 2 Non pre,itive data structure

# 1.Premitive data structure
# int,float,double,char,boolean
# 2.Non premitive data structure(Again 2 types)
#  1.Linear data structure
#  2.Non linear data structure

# 1.Linear dat structure
# ->Arrays,stacks,queues,Linked list

# 2.Non linear data structures
# ->Trees and graphs 

# Operations in data struictures 
# Traversing=>Accesing each element
# Insertion=>Adding an element
# Deletion=>Removing an element
# Searching=>Finding an element
# Sorting=>Arranging an element in some order
# Updating=>Modifying the existing dat

# LINEAR SEARCH
# def LINEAR(arr,target,i=0):
#     for i in range(len(arr)):
#         if arr[i]==target:
#             return i
        
#     return -1
# arr=[1,2,3,7]
# target=7
# result=LINEAR(arr,target)
# if result!=-1:
#     print("Element found at index ",result)
# else:
#     print("Element Not found") 



# def linear(arr,target):
#     for i in range(len(arr)):
#         if arr[i]==target:
#             return i
#     return -1
# arr=[1,2,3,4,5,6,9,8]
# target=10
# result=linear(arr,target)
# if result!=-1:
#     print("The element is found at the index",result)
# else:
#     print("Element not found")




# arr=[1,2,3,4,5]
# if 3 in arr:
#     print("Element found ")
# else:
#     print("Not found")




# def Finding(arr,target):
#     if target in arr:
#         print("Element found")
#     else:
#         print("Not found")
# arr=[1,3,34,4,5,5]
# target=4
# Finding(arr,target)



# Count how many times a target occurs

# arr=[1,2,3,4,5,4,5,4,4,4,4]
# target=4;
# count=0;
# for i in range(len(arr)):
#     if arr[i]==target:
#         count+=1
# print("Count of target values are:",count)



# Return all indices where target occurs
# arr=[1,2,3,4,5,4,4,4,4];
# target=4
# index=[x for x in range(len(arr)) if arr[x]==target]
# print(index)


