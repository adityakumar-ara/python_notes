class Employee:
                    emp_name = "Ujwal"

                    emp_id = 111

                    emp_address = "xyzzz"

                    __emp_salary = 10000

                    def emp_info(self):
                                        print("all about Employee")

                    def __emp_confidential_data(self):
                                        print("here is the employee confidential data")


emp_obj = Employee()
print(emp_obj.emp_name)
print(emp_obj._emp_address)
emp_obj.emp_info()