# List Comprahention,Tuple,Set,Dictionary,Function(Lamda function,Types of arguments,Local and global variable)
# 1.List Comprahention
# Comprehention is a Consise and effient way of creating a sequenses like list ,tuple,set etc
# Syntax=>[Expression for item in iterable if condition]

# list=[1,2,3,4,5,6]
# for i in list:
#     if i%2==0:
#         print(i);
        
        
        
# list=[1,2,3,4,5,6,7];
# print([x for x in list if x%2==0])       




# num=[1,2,3,4,5,6,7];
# for i in  num:
#     if i%2==0:
#         print("Even numbers are :",i)
#     else:
#         print("The dd numbers are:",i)
    
    
# list=[1,2,3,4,5,6,7]
# even=[]
# odd=[]
# for i in list:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print("Even numbers are:",even)
# print("Odd numbers are:",odd)



# list=[1,2,3,4,5,6,7];
# print("Even numbers are:",[x for x in list if x%2==0])
# print("Odd numbers are:",[x for x in list if x%2!=0])


# num=[1,2,3,4,5,6,7]
# even=[]
# odd=[]
# for i in num:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(even)
# print(odd)




# list=[1,2,3,4,5,6,7]
# print("Even numbers are:",[x for x in list if x%2==0])
# print("Odd numbers are:",[x for x in list if x%2!=0])

# ----------------------------------------------------------------------------


# Tuple
# Tuple is immutable collection of diffrent data datatype stored in a single variable
# 1.Creation of tuple
# 2.Accessibility
# 3.Immutability
# 4.Operations
# 5.Methods


# 1.Creation of empty tuple
# tuple=()
# print(type(tuple))


# t=tuple()
# print(type(t))


# Creating a tuple
# t=(1,2,3,4,5)
# print(t)


# t=1,2,3,4,5
# print(t)


# t=(3)
# print(t)
# print(type(t))


# t=(2,)
# print(t)
# print(type(t))


# Accessing tuple
# We can acces the tuple using iundexing,slicing 
# Indexing 
# t=(1,2,3,4,5,6)
# print(t[-3])

# Slicing
# [start ,stop,step]



# t=('apple','mango','banana','graps','papaya')
# print(t[0:3])
# print(t[::-1])
# print(t[:4]);
# print(t[2:])



# Tuple immutability
# t=(1,2,3,4,5);
# b=t[2]=9
# print(b)


# Tuple operators
# concatination,repetation,Membership check
# concatination(+)
# t1=(1,2,3)
# t2=(4,5,6)
# print(t1+t2)

# Repetation
# t1=(1,2,3)
# print(t1*10)


# t1=(1,2,3,4,5,6,7)
# print( 7 in t1);
# print( 9 in t1)


# Methos in tuple 
# 1.count(),2.index()


# 1.count=> tuplename.count(elemet)
# t1=(1,2,3,4,4,2,23,2,2,2,2,2,2,5,5,5,5)
# print(t1.count(2))

# 2.index=>tupename.index(elemet)
# t1=(1,2,3,4,5,6)
# print(t1.index(4))


# t1=(1,2,3,4,5,2,4,3,2,3,2,5);
# # print(t1.index(2))


# # tuplename.index(element,start,end)
# print(t1.index(2,2,10))


# Covertion in tuple
# t=(1,2,3,4,5,6)
# l=list(t)
# l[1]=7;
# l.append(9)
# l.insert(2,40)
# t=tuple(l)
# print(t)




# t=(1,2,3,4,5,6);
# l=list(t)
# l[4]=20
# t=tuple(l)
# print(t)


# t=(1,2,3,4,5);
# l=list(t)
# l.append(6)
# t=tuple(l)
# print(t)


# t=(1,2,3,5,6,7)
# l=list(t)
# l.extend([30,40])
# t=tuple(l)
# print(t)


# t=(1,2,3,5,6,7,2)
# l=list(t)
# l.remove(2)
# t=tuple(l)
# print(t)



# t=(1,2,3,5,6,7,2)
# l=list(t)
# l.pop(2)
# t=tuple(l)
# print(t)

# t=(1,2,3,5,6,7,2)
# l=list(t)
# l.pop()
# t=tuple(l)
# print(t)


# t=(1,2,3,5,6,7,2)
# l=list(t)
# del l[3]
# t=tuple(l)
# print(t)


# t=(1,2,3,5,6,7,2)
# l=list(t)
# del l[:]
# t=tuple(l)
# print(t)

# -------------------------------------------------------------

# SET
# Set is a unorderd collection of unique elemets
# Creating empty set 

# s={''}
# print(type(s))


# s=set()
# print(type(s))


# Creating set
# s={1,2,3,4,5}
# print(s)



# s=set([1,2,3,4,5])
# print(s)



# s=set((1,2,3,4,5))
# print(s)



# Set automatically remove the duplicates
# s={1,2,3,4,5,1,2,3,4,5}
# print(s)



# Adding elements to a set
# syntax=>SetName.add(element)
# s={1,2,3,4,5,6}
# s.add(9)
# print(s)

# Removing element in the set
# s={1,2,3,4,5,67}
# s.remove(67)
# print(s)


# If element not fount we get an error
# s={1,2,3,4,5}
# s.remove(8)
# print(s)


# discard()
# Syntax=>setname.discard(element)
# s={1,2,3,4,5}
# s.discard(4)
# print(s)


# It does not raise any error if element not found
# s={1,2,3,4,5}
# s.discard(8)
# print(s)


# pop()
# # pop remove the random element in the set
# s={1,2,3,4,5}
# o=s.pop()
# print(s)
# print("Removed elemet is:",o)



# Set operations
# union(),intersection(),diffrence(),symmetric_diffrence()


# union=>Combinig 2 sets
# s={1,2,3,4}
# s1={5,6,7}
# print(s|s1)
# print(s.union(s1))


# intersection=>Common element between 2 sets
# s1={1,2,3,4,5}
# s2={6,7,8,9}
# print(s1&s2)



# s1={1,2,3,4,5}
# s2={2,3,5}
# print(s1&s2)
# print(s1.intersection(s2))


# Diffrence=>Keeps the elements in A but not in B
# s1={1,2,3,4,5}
# s2={6,7,8,9}
# print(s1-s2)
# print(s2-s1)
# print(s1.difference(s2))


# Symmetric Diffrence=>Kepps the lemts either A or B but not in both
# s1={1,2,3,4,5}
# s2={6,7,8,9,1,2}
# print(s1^s2)
# print(s1.symmetric_difference(s2))



# l=[1,2,3,4,5,6,1,1,1,1,]
# s=set(l)
# print(s)



# -----------------------------------------------------------------------


# Dictionary
# Dictionary is a collection of key-value pairs stored in a single varible
# Dictionary is unordered before the version of 3.7 after the version of 3.7 dictionary is orderd
# Current version of Python is python 3.13.7 released on august 14 2025

# Creating an empty dictionary
# d={}
# print(type(d))


# d=dict()
# print(type(d))

# Creating dictionary with elemets
# d={'name':'preethi','age':21,'course':"data science"}
# print(d)


# d={'name':'preethi','age':21,'course':"data science"}
# print(d)



# Keys must be unique if we give same key name then 1st key name is replaced by last key name
# d={'name':'preethi','name':'raju','name':"kanya",'age':21}
# print(d)




# Values may be duplicate
# d={'name1':"preethi",'name2':"preethi",'age':21}
# print(d)


# creating dictionary using dict()
# d=dict(name='preethi',age=21)
# print(d)


# creating dictionary using list of tuple
# d=dict([('name','preethi'),('age',21)])
# print(d)


# d=dict([('name','preethi'),('age',21)])
# print(d['name'])
# print(d['age'])
# print(d.get('name'))
# print(d)


# d=dict([('name','preethi'),('age',21)])
# print(d.get('course','illa kane '))


# d=dict([('name','preethi'),('age',21)])
# d['gender']='Female'
# d['name']='varshini'
# print(d)



d=dict([('name','preethi'),('age',21)])
# c=d.pop('name')
# print(c)
# d.popitem()
# del d['name']
# print(d)
a=d.items()
print(a)