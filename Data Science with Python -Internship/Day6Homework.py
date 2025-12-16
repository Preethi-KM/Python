# # # Setter method used to set a value for a key
# # # In python dictionary don't have an afficial set() method ,but they provide multiple ways to set values

# # # 1.Using Assignment/update
# # my_dict = {"name": "Alice", "age": 25}
# # my_dict["city"] = "Bangalore"
# # my_dict["age"] = 26  
# # print(my_dict)

# if the key exist update the value if the key does not exit add a new key 



# # 2.Using update method=>We can add multiple  values at once
# my_dict = {"name": "Alice", "age": 25}
# my_dict.update({"age": 27})
# my_dict.update({"city": "Bangalore", "country": "India"})
# print(my_dict)




# 3.Using setdefault( method)
my_dict = {"name": "Alice", "age": 25}

# Key doesn't exist → sets new key
my_dict.setdefault("city", "Bangalore")

# Key exists → does not overwrite
my_dict.setdefault("age", 30)

print(my_dict)




# 4.using dictionary  comprohention
my_dict = {"a": 1, "b": 2, "c": 3}

# Increase all values by 10
my_dict = {k: v + 10 for k, v in my_dict.items()}

print(my_dict)
