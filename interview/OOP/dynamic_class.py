# # using type()
# DynamicClass = type(
#     'DynamicClass',
#     (object,),
#     {
#         'greet': lambda self: 'Hello from DynamicClass!',
#         'attribute': 'I\'m dynamic!'
#     }
# )
#
# instance = DynamicClass()
# print(instance.greet())
# print(instance.attribute)

# -------------------------------------------------------
# # using exec()
# class_definition = """
# class DynamicClass:
#     def __init__(self, name):
#         self.name = name
#
#     def greet(self):
#         return f"Hello, {self.name} from DynamicClass!"
# """
#
# exec(class_definition)
#
# instance = DynamicClass("Dee")
# print(instance.greet())


# -------------------------------------------------------
# # using metaclass
# class Meta(type):
#     def __new__(cls, name, bases, dct):
#         dct['meta_attribute'] = 'Added by metaclass'
#         return super().__new__(cls, name, bases, dct)
#
#
# class DynamicClass(metaclass=Meta):
#     def greet(self):
#         return "Hello from a class with a metaclass!"
#
#
# instance = DynamicClass()
# print(instance.greet())
# print(instance.meta_attribute)
# -------------------------------------------------------
# # dynamic methods and attributes creation
# class DynamicClass:
#     pass
#
#
# instance = DynamicClass()
#
# setattr(instance, 'type_of_class', 'This is dynamic!')
#
#
# def dynamic_method(self):
#     return f"Dynamic method called, attribute value: {self.type_of_class}"
#
#
# setattr(DynamicClass, 'method', dynamic_method)
#
# print(instance.type_of_class)
# print(instance.method())
# -------------------------------------------------------
