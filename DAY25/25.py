# my_set = {11, 22, 33, 44, 55, 11, 22, 33,22,55}  #remove same element when same element present in set
# print("this is actual elements of this set :", my_set)

# # add() – Add a Single Element    ---> e kahi bhi add kar di elemnt ke
# my_set = {11, 22, 33, 55, 44, 2}
# print("before adding element :", my_set)

# my_set.add(77)
# my_set.add(88)
# my_set.add(99)
# print("after adding element  :", my_set)



# #  update() – Add Multiple Elements
# my_set = {11, 22, 33, 55, 44, 2}
# print("before adding element :", my_set)

# my_set.update({77, 999, 102})
# print("after adding element  :", my_set)

# # 3. remove() – Remove a Specific Element
# my_set = {11, 22, 33, 55, 44, 2}
# print("before removing element :", my_set)

# my_set.remove(22)
# print("after removing element  :", my_set)


# #set Does NOT Support Indexing
# my_set = {11, 22, 33, "rahul", "ravi", 8.8}
# print("before operation :", my_set)

# print(my_set[4])   # ERROR → sets do not support indexing

# Loop Through a Set
# my_set = {11, 22, 33, "rahul", "ravi", 8.8}
# print("before iteration :", my_set)

# for i in my_set:
#     print(i)
