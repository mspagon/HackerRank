# Author: mspagon
# Date: 5/21/18 7:36 PM


class Employee:
    def __init__(self, name: str):
        self.name = name
        self.employees = []

    def get_name(self):
        return self.name

    def set_name(self, name: str):
        self.name = name

    def add_employee(self, names):
        for person in names:
            self.employees.append(person)

    def get_employees(self):
        return self.employees

    def count_employees_below(self):
        count = 0
        if len(self.employees) == 0:
            return 0
        else:
            count = len(self.employees)
            for person in self.employees:
                count = count + person.count_employees_below()



def main():
    # Which design pattern?? Builder?
    # learn to make something that constructs objects from a list of names and IDs.
    mike = Employee("mike")
    sam = Employee("sam")
    steve = Employee("steve")
    candice = Employee("candice")
    bob = Employee("bob")
    carson = Employee("carson")
    jake = Employee("jake")
    phillip = Employee("phillip")
    cindy = Employee("cindy")
    natasha = Employee("natasha")
    alice = Employee("alice")
    will = Employee("will")
    kate = Employee("kate")

    mike.add_employee([sam, steve])
    steve.add_employee([candice])
    candice.add_employee([carson, jake])
    jake.add_employee([phillip])
    phillip.add_employee([cindy, natasha])
    bob.add_employee([alice, will, kate])

    print(bob.count_employees_below())


if __name__ == "__main__":
    main()
