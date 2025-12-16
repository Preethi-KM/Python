# # # # # # # # # # # String(Immutable)
# # # # # # # # # # a="preethi";
# # # # # # # # # # a[0]='P'
# # # # # # # # # # print(a);


# # # # # # # # # # string slicing
# # # # # # # # # # string[start,stop,step]=>step is mandotory

# # # # # # # # s="pythonprogramming";
# # # # # # # # # print(s[0:6])


# # # # # # # # # print(s[6:18])

# # # # # # # # # print(s[:]);

# # # # # # # # # print(s[:;]);


# # # # # # # # # print(s[::-1]);

# # # # # # # # # print(s[6:9])
# # # # # # # # # print([4:])
# # # # # # # # print(s[14:])

# # # # # # # # s="preethi";
# # # # # # # # print(s[::-1]);

# # # # # # # # print(s[-1:-5])
# # # # # # # # print(s[-1::-1])
# # # # # # # # print(s[:6]);
# # # # # # # # print(s[6:]);
# # # # # # # # print(s[:]);
# # # # # # # # print(s[0:12:2])
# # # # # # # # print(s[::-2])


# # # # # # # # date='2025-03-17';
# # # # # # # # print(date[:4])


# # # # # # # s="string";
# # # # # # # print(s.upper())
# # # # # # # print(s.lower())
# # # # # # # print(s.count("s"))
# # # # # # # print(len(s))



# # # # # a="HelloWorld";
# # # # # # print(a[2:9]);
# # # # # # print(a[8:1:-1]);

# # # # # print(a[2:8:2])


# # # there are 3 ways are there to empty list
# # # # # List
# # # # # list=[];
# # # # # print(type(list));



# # # # list=list()
# # # # print(type(list));



# # # list=[1,2,3];
# # # print(list.clear());

# # # Accessing list(we can have nested list also)

# # # list=[1,"hello",4.5,True]
# # # print(list[1]);
# # # print(list[-1]);
# # # print(list[::-1]);
# # # print(list[2]);

# # # Nested2 list


# # list=[1,"hello",[1,2,"hi"],4.5,True]
# # print(list[2][1])

# # list1=[1,"hello",[1,2,[4,6],"hi"],4.5,True,["Good",23,""]]
# # print()

# # Insert(index_value,value)
# # list=[1,2,3,"good","python"];
# # list.insert(1,"bad");
# # print(list)

# # list.insert(3,"preethi");
# # print(list)

# # list.insert(1,"varshini");
# # print(list)


original=[1,2,3];
copy=original.copy();
copy[0]=100
print("original",original);
print("copy:",copy)

# # append
# list=[1,2,3,4];
# list.append(3

