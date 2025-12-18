# # ---------------------------------------------------------pop()----------------------------------------------------------------------------

# # pop() – remove random element from a set
# my_set = {11, 22, 33, "rahul", "ravi", 8.8}
# print("before pop:", my_set)

# my_set.pop()
# print("after pop:", my_set)

# # ---------------------------------------------------------discard() ----------------------------------------------------------------------------

# # discard() – remove specific element (NO error if not found)
# my_set = {11, 22, 33, "rahul", "ravi", 8.8}
# print("before discard:", my_set)

# my_set.discard(224565432)
# my_set.discard(22)
# print("after discard:", my_set)

# # ---------------------------------------------------------clear() ----------------------------------------------------------------------------

# # clear() – remove all elements from set
# my_set = {11, 22, 33, "rahul", "ravi", 8.8}
# print("before clear:", my_set)

# my_set.clear()
# print("after clear:", my_set)

# # ---------------------------------------------------------1️⃣ Explicit Typecasting ----------------------------------------------------------------------------


# # <<<<<<<<<<<<<<<<<<<<<<<<<<<-----------------1️⃣ Explicit Typecasting----------------->>>>>>>>>>>>>>>>>>.>>>>>>>>>>>>>>>>>>>>>>
# # (Developer converts manually)
# # String → Integer
# my_variable = "23"
# print(type(my_variable))

# my_new_variable = int(my_variable)
# print(my_new_variable)
# print(type(my_new_variable))


# # Integer → String
# my_variable = 23
# print(type(my_variable))

# my_new_variable = str(my_variable)
# print(my_new_variable)
# print(type(my_new_variable))


# # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<----------Boolean → Integer----------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# my_variable = True
# print(type(my_variable))

# my_new_variable = int(my_variable)
# print(my_new_variable)
# print(type(my_new_variable))

# # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<----------Integer → Boolean----------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# my_variable = 1
# print(type(my_variable))

# my_new_variable = bool(my_variable)
# print(my_new_variable)
# print(type(my_new_variable))


# # ---------------------------------------------------------2️⃣ Implicit Typecasting----------------------------------------------------------------------------

# (Python automatically converts)
# my_variable = 6.7
# my_second_variable = 4

# print(type(my_variable))          
# print(type(my_second_variable))   

# print("after implicit typecasting:", my_variable + my_second_variable)

# # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<----------🧾 DICTIONARY INTRODUCTION----------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# my_dict = {
#     "name": "Ujwal",
#     "age": 24,
#     "city": "Bangalore",
#     "roll_no": 101
# }

# print(my_dict)