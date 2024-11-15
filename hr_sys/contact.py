from representations import ShowAsDictMixin

class AddressBook:
    def __init__(self) -> None:
        self._employee_adresses = {
            1: Address("121 Admin Rd.", "Concord", "NH", "03301"),
            2: Address("67 Paperwork Ave", "Manchester", "NH", "03101"),
            3: Address("15 Rose St", "Concord", "NH", "03301"),
            4: Address("39 Sole St.", "Concord", "NH", "03301"),
            5: Address("99 Mountain Rd.", "Concord", "NH", "03301")
        }

    def get_employee_address(self,employee_id):
        address = self._employee_adresses.get(employee_id)
        if not address:
            ValueError(employee_id)            
        return address

class Address(ShowAsDictMixin):
    def __init__(self,house,city,state,zipcode):
        self.house = house
        self.city = city
        self.state = state
        self.zipcode = zipcode

    def __str__(self) -> str:
        lines = [f"{self.house} (H),",f"{self.city}",f"{self.zipcode} , {self.state}"]
        return "\n".join(lines)