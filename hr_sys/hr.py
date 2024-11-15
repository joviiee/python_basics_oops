class PayrollSystem:
    def __init__(self) -> None:
        self._employee_policies = {
            1: WeeklyPolicy(3000),
            2: WeeklyPolicy(1500),
            3: CommissionPolicy(1000, 100),
            4: HourlyPolicy(15),
            5: HourlyPolicy(9)
        }

    def get_policy(self,employee_id):
        policy = self._employee_policies.get(employee_id)
        if not policy:
            return ValueError
        return policy
    
    def calculate_payroll(self,employees):
        for employee in employees:
            print(f'Payroll for : {employee.id} - {employee.name}')
            print(f'Check Amount : {employee.calculate_payroll()}\n')
            if employee.address != None:
                print(f"Sent to : \n{employee.address}\n")

class PayrollPolicy:
    def __init__(self) -> None:
        self.hours_worked = 0

    def track_work(self,hours):
        self.hours_worked += hours

class WeeklyPolicy(PayrollPolicy) :
    def __init__(self,weekly_salary):
        super().__init__()
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary

class HourlyPolicy(PayrollPolicy):
    def __init__(self,hourly_salary):
        super().__init__()
        self.hourly_salary = hourly_salary

    def calculate_payroll(self):
        return self.hourly_salary * self.hours_worked
    

class CommissionPolicy(WeeklyPolicy) :
    def __init__(self,weekly_salary,commission_per_sale):
        super().__init__(weekly_salary)
        self.commission_per_sale = commission_per_sale

    @property
    def commission(self):
        sales = self.hours_worked/5
        return sales * self.commission_per_sale

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission
