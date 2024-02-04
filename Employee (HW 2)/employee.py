#  File: EmployeeSalaries.py
#  Student Name:
#  Student UT EID:

class Employee:
    def __init__(self, **kwargs):
            self.name = kwargs["name"]
            self.id = kwargs["id"]
            if "salary" in kwargs:
                self.salary = kwargs["salary"]
            else:
                self.salary = 80000


    def get_salary(self):
        return self.cal_salary()

    def cal_salary(self):
        return self.salary
    def __str__(self):
        return f"Employee \n {self.name},{self.id},{self.salary}"


############################################################
############################################################
############################################################
class Permanent_Employee(Employee):
    def __init__(self, **kwargs):
        super().__init__(name=kwargs["name"], id=kwargs["id"], salary=kwargs["salary"])
        if "salary" in kwargs:
            self.benefits = kwargs["benefits"]
        else:
            self.benefits = []


    def cal_salary(self):
        # checking if the benefits array is empty
        if len(self.benefits) == 0:
            return self.salary
        if "health_insurance" and "retirement" in self.benefits:
            return self.salary * 0.7
        if "retirement" in self.benefits:
            return self.salary * 0.8
        if "health_insurance" in self.benefits:
            return self.salary * 0.9


    def __str__(self):
        return f"Permanent_Employee \n {self.name},{self.id},{self.salary},{self.benefits}"


############################################################
############################################################
############################################################
class Manager(Employee):
    def __init__(self, **kwargs):
        super().__init__(name=kwargs["name"], id=kwargs["id"], salary=kwargs["salary"])
        self.bonus = kwargs.get("bonus")

    def cal_salary(self):
        return self.salary + self.bonus


    def __str__(self):
        return f"Manager \n {self.name},{self.id},{self.salary},{self.bonus}"




############################################################
############################################################
############################################################
class Temporary_Employee(Employee):
    def __init__(self, **kwargs):
        super().__init__(name=kwargs["name"], id=kwargs["id"], salary=kwargs["salary"])
        self.hours = kwargs.get("hours")

    def cal_salary(self):
        return self.salary * self.hours


    def __str__(self):
        return f"Temporary_Employee \n {self.name},{self.id},{self.salary},{self.hours}"


############################################################
############################################################
############################################################
class Consultant(Temporary_Employee):
    def __init__(self, **kwargs):
        super().__init__(name=kwargs["name"], id=kwargs["id"], salary=kwargs["salary"])
        self.hours = kwargs.get("hours")
        self.travel = kwargs.get("travel")

    def cal_salary(self):
        return self.salary * self.hours + (self.travel * 1000)


    def __str__(self):
        return f"Consultant \n {self.name},{self.id},{self.salary},{self.hours},{self.travel}"


############################################################
############################################################
############################################################ NEEEEED TO FIX############################################################ NEEEEED TO FIX
############################################################ NEEEEED TO FIX
############################################################ NEEEEED TO FIX
############################################################ NEEEEED TO FIX
############################################################ NEEEEED TO FIX
class Consultant_Manager(Consultant, Manager):
    def __init__(self, **kwargs):
        Consultant.__init__(self, name=kwargs["name"], id=kwargs["id"], salary=kwargs["salary"], hours=kwargs["hours"], travel=kwargs["travel"])
        Manager.__init__(self, name=kwargs["name"], id=kwargs["id"], salary=kwargs["salary"], bonus=kwargs["bonus"])

    def cal_salary(self):
        return self.salary * self.hours + (self.travel * 1000) + self.bonus

    ############################################################ NEEEEED TO FIX
    def __str__(self):
        return f"Consultant_Manager \n {self.name},{self.id},{self.salary},{self.hours},{self.travel},{self.bonus}"

############################################################
############################################################
############################################################

def calculate_total_salaries(employee_list):
    returnSum = 0

    #looping though all employess and summing them
    for employee in employee_list:
        returnSum += employee.get_salary()


def calculate_manager_salaries(employee_list):
    returnSum = 0

    # looping though all employess and summing them
    for employee in employee_list:
        if isinstance(employee, Consultant_Manager) or isinstance(employee, Manager):
            returnSum += employee.get_salary()


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

