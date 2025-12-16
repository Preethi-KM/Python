# class Car:
#     def __init__(self,color,brand):
#         self.color=color
#         self.brand=brand
#         print("The color is",self.color)
#         print("The brand is ",self.brand)
# o=Car("red","BMW")
# o1=Car("green","Maruthi")



# Inheritance 
# polymorphim
# Abstarction
# Encapsulation




# Inheritance
# making public variabe to private




# class person:
#     def __init__(self,name):
#         self.name=name
#     def get_name(self):
#         return  self.name
# p=person("varshini")
# p.name="preethi"
# print(p.name)




class person:
    def __init__(self,name):
        self.__name=name
    def get_value(self):
        return self.__name
p=person("chaithanya")
print(p.get_value())
p.__name="preethi"
print(p.__name)