class ProductivitySystem:
    def __init__(self) -> None:
        self.roles = {
            "manager": ManagerRole(),
            "secretary": SecretaryRole(),
            "sales":SalesRole(),
            "factory":FactoryRole()
        }

    def get_role(self,role_id):
        role_type = self.roles.get(role_id)
        if not role_type:
            raise ValueError(role_type)
        return role_type

    def track(self,employees,hours):
        for employee in employees:
            result = employee.work(hours)
            

class ManagerRole:
    def work(self,hours):
        return f"works as a manager for {hours} hours a week."
    
class SecretaryRole:
    def work(self,hours):
        return f"works as a secretary for {hours} hours a week."
    
class SalesRole:
    def work(self,hours):
        return f"works as a salesperson for {hours} hours a week."
    
class FactoryRole:
    def work(self,hours):
        return f"works as a factory worker for {hours} hours a week."