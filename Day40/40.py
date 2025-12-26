# ------------------------------------Multgible Inharitage*-------------------------------
# class Grandfather:
#     grendfather_Assets = "Grand Complex"

# class Father(Grandfather):
#     father_Assets = "Father Complex"

# class Son(Father):
#     son_Assents = "Son Complex"

# class Grandson(Son):
#     Grandson_Assets = "Grandson Complex"

# grandson_obj = Grandson()
# print(grandson_obj.grendfather_Assets)
# print(grandson_obj.father_Assets)
# print(grandson_obj.son_Assents)
# print(grandson_obj.Grandson_Assets)


# ----------------------------------*hierarchican*--------------------------------------
# class father:
#     father_assets = "Bharat Petrolium"
# class child1(father):
#     child1_assets = "BMW"
# class child2(father):
#     child2_assets = "Fortuner"

# child1_obj = child1()
# print(child1_obj.father_assets)
# print(child1_obj.child1_assets)

# child2_obj = child2()
# print(child2_obj.father_assets)
# print(child2_obj.child2_assets)


# ----------------------------------------*Hybrid* -------------------------------------------
# class Grandfather:
#     grendfather_Assets = "Grand Complex"

# class Father(Grandfather):
#     father_Assets = "Father Complex"

# class Son(Father):
#     son_Assents = "Son Complex"

# class Grandson(Father):
#     Grandson_Assets = "Grandson Complex"

# grandson_obj = Grandson()
# print(grandson_obj.Grandson_Assets)
# print(grandson_obj.grendfather_Assets)


# class person_name :
#     Name = "Aditya"
# class Employee(person_name):
#     Employee_id = 23444 
# class manager(Employee):
#        Department = "computer science"       
# class student:
#      roll_no = 234123
# class intern( student,manager ) :
#      pass
                
# my_obj = intern()
# print(my_obj.Name)
# print(my_obj.Employee_id)
# print(my_obj.Department)
# print(my_obj.roll_no)