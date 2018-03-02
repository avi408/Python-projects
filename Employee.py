class Employee:
    def __init__(self,fn,ln,ssn,salary):

        self.fn=fn
        self.ln=ln
        self.ssn=ssn
        self.salary= salary

    def __str__(self):

        return "Name: %s \nLast Name: %s\nSocial Security: %s\nSalary: %s\n" % (
        self.firstName_, self.lastName_, self.ssn_, self.salary_)

    def giveRaise(self, percentRaise):

        salaryIncrease = percentRaise / 100 * self.salary_


        self.salary_ = salaryIncrease + self.salary_




