# my_name="aditya"
# class name:
#          my_fullname="aditya kumar"
         
# print(name.my_fullname)         

class Student:
                   std_name = "Ujwal"
                   branch = "CSE"

                   def student_info(self):
                                     print("here is the all student information")
                    

my_obj = Student()
my_obj.student_info()
# Student.student_info()  => it give error because in class don't dorect call function
print(Student.std_name)  
print(Student.branch) 
print(my_obj.std_name) 



