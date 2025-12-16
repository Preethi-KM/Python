# # # # # # # # # # # # # # # # # # # # key not allow duplicate ,value allow duplicate
# # # # # # # # # # # # # # # # # # # a={};
# # # # # # # # # # # # # # # # # # # print(a);

# # # # # # # # # # # # # # # # # # # b=dict();
# # # # # # # # # # # # # # # # # # # print(b)

# # # # # # # # # # # # # # # # # # # # Syntax variable={key1:value,key2:value,key3:value} value only becase value allow duplicates ,key does not allow so key1,key2

# # # # # # # # # # # # # # # # # # # My_Info={
# # # # # # # # # # # # # # # # # # #     'name':"preethi",
# # # # # # # # # # # # # # # # # # #     'class':"7Th sem",
# # # # # # # # # # # # # # # # # # #     'section':"B",
# # # # # # # # # # # # # # # # # # #     'phoneNo':7676783274,
# # # # # # # # # # # # # # # # # # #     'BloodGrop':"A+"
# # # # # # # # # # # # # # # # # # # }
# # # # # # # # # # # # # # # # # # # print(My_Info);


# # # # # # # # # # # # # # # # # # dic={1:"hello",1:'hi',1:'bye',3:10}            It does not allow duplicates(key)
# # # # # # # # # # # # # # # # # # print(dic)



# # # # # # # # # # # # # # # # # dic={'name':'preethi','name':'paavana','name':'varshini'}
# # # # # # # # # # # # # # # # # print(dic)



# # # # # # # # # # # # # # # # # If we want to add multiple items inside the dictionary then we can use list inside dictionary
# # # # # # # # # # # # # # # # dic={'name':"preethi",'age':21,'marks':[99,88,77]}      
# # # # # # # # # # # # # # # # print(dic['marks'][0])




# # # # # # # # # # # # # # # d={'name':"preethi",'age':21}
# # # # # # # # # # # # # # # print(d.clear())



# # # # # # # # # # # # # # d={'name':"preethi",'age':21}
# # # # # # # # # # # # # # copy_v=d.copy()
# # # # # # # # # # # # # # print("copyed elements:",copy_v)
# # # # # # # # # # # # # # print("original ",d)


# # # # # # # # # # # # # # fromkeys(iterable,value)-creates a dictionry with specific keys and a common value
# # # # # # # # # # # # # # iterable means it going to check the every key and assignig same value to each  specifyed key
# # # # # # # # # # # # # # a=['a','b','c']
# # # # # # # # # # # # # # d=dict.fromkeys(a,2)
# # # # # # # # # # # # # # print(d)



# # # # # # # # # # # # # a=['a','b','c'];
# # # # # # # # # # # # # b=dict.fromkeys(a,3)
# # # # # # # # # # # # # print(b)



# # # # # # # # # # # # d={'name':"preethi",'age':25}
# # # # # # # # # # # # print(d.get('name'))
# # # # # # # # # # # # print(d.get('city','not found'))


# # # # # # # # # # # # by using the key accessing elements in dictionary


# # # # # # # # # # d={'name':"arun",'age':26,'Age':26}  caps and small are diffrent
# # # # # # # # # # print(d.items())



# # # # # # # # # d={'name':'preethi','age':25}
# # # # # # # # # print(d.keys())
# # # # # # # # # print(d.values())
# # # # # # # # # print(d.items())


# # # # # # # # d={'name':'preethi','age':25}
# # # # # # # # age=d.pop('age')
# # # # # # # # print(age)
# # # # # # # # print(d)





# # # # # # # # popitem() =>it remove the last item in the dictionary

# # # # # # # d={'name':'preethi','age':25,'grade':'A'}
# # # # # # # pop1=d.popitem()
# # # # # # # print(pop1)
# # # # # # # print(d)




# # # # # # # update(other_dict) -updates dictionary with key-values

# # # # # # d={'name':'preethi','age':25}
# # # # # # d.update({'city':'new york','age':26})
# # # # # # print(d)




# # # # # # Merging 2 dictionary
# # # # # dic1={'a':1,'b':2}
# # # # # dict2={'c':3,'d':4}
# # # # # merged_dic={**dic1,**dict2}
# # # # # print(merged_dic)



# # # # # comprahention
# # # # list=[1,2,3,4];
# # # # list2=[]
# # # # for i in list:
# # # #     list2.append(i*i)
# # # # print(list2)




 


# # # # list comprahetion
# # # # new_list=[expression for item in iterable if condition]
# # # # expression=>The operation or value to store in the new list
# # # # item=>The variable representin each elemnt in the iterable
# # # iterable=>The source data structure(like a list,range,or tuple)


# # square=[x**2 for x in range(5)]
# # print(square)



# list=[1,2,3,4,5];
# square=[x**2 for x in list]
# print(square)



