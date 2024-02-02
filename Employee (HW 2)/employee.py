#  File: EmployeeSalaries.py
#  Student Name:
#  Student UT EID:

class Employee:
    def __init__(self, **kwargs):
        pass
        '''##### ADD CODE HERE #####'''

    def __str__(self):
        pass
        '''##### ADD CODE HERE #####'''


############################################################
############################################################
############################################################
class Permanent_Employee(Employee):
    def __init__(self, **kwargs):
        pass
        '''##### ADD CODE HERE #####'''

    def __str__(self):
        pass
        '''##### ADD CODE HERE #####'''


############################################################
############################################################
############################################################
class Manager(Employee):
    def __init__(self, **kwargs):
        pass
        '''##### ADD CODE HERE #####'''

    def __str__(self):
        pass
        '''##### ADD CODE HERE #####'''


############################################################
############################################################
############################################################
class Temporary_Employee(Employee):
    def __init__(self, **kwargs):
        pass
        '''##### ADD CODE HERE #####'''

    def __str__(self):
        pass
        '''##### ADD CODE HERE #####'''


############################################################
############################################################
############################################################
class Consultant(Temporary_Employee):
    def __init__(self, **kwargs):
        pass
        '''##### ADD CODE HERE #####'''

    def __str__(self):
        pass
        '''##### ADD CODE HERE #####'''


############################################################
############################################################
############################################################
class Consultant_Manager(Consultant, Manager):
    def __init__(self,  **kwargs):
        pass
        '''##### ADD CODE HERE #####'''

    def __str__(self):
        pass
        '''##### ADD CODE HERE #####'''

############################################################
############################################################
############################################################

def calculate_total_salaries(employee_list):
    pass
    '''##### ADD CODE HERE #####'''

def calculate_manager_salaries(employee_list):
    pass
    '''##### ADD CODE HERE #####'''


''' ##### DRIVER CODE #####
    ##### Do not change. '''

# create employees
chris = Employee(name="Chris", id="UT1")
emma = Permanent_Employee(name="Emma", id="UT2", salary=100000, benefits=["health_insurance"])
sam = Temporary_Employee(name="Sam", id="UT3", salary=100,  hours=40)
john = Consultant(name="John", id="UT4", salary=100, hours=40, travel=10)
charlotte = Manager(name="Charlotte", id="UT5", salary=1000000, bonus=100000)
matt = Consultant_Manager(name="Matt", id="UT6", salary=1000, hours=40, travel=4, bonus=10000)

# print employees
print(chris, "\n")
print(emma, "\n")
print(sam, "\n")
print(john, "\n")
print(charlotte, "\n")
print(matt, "\n")

# calculate and print salaries
print("Check Salaries")
print("Emma's Salary is:", emma.cal_salary())
emma.benefits = ["health_insurance"]
print("Emma's Salary is:", emma.cal_salary())
emma.benefits = ["retirement", "health_insurance"]
print("Emma's Salary is:", emma.cal_salary())
print("Sam's Salary is:", sam.cal_salary())
print("John's Salary is:", john.cal_salary())
print("Charlotte's Salary is:", charlotte.cal_salary())
print("Matt's Salary is:",  matt.cal_salary())

