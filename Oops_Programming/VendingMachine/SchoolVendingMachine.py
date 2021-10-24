from Oops_Programming.VendingMachine.VendingMachine import VendingMachine


class SchoolVendingMachine(VendingMachine):
    snack_prices = {"candy": 1.00, "soda": 0.50, "chips": 2.00, "cookies": 2.50}
    student_debt = {"John": 13.00, "Lisa": 10.50, "Lilly": 9.00, "Jack": 6.50}

    # Complete the class
    def __init__(self, inventory, serial, days_until_maintenance):
        VendingMachine.__init__(self, inventory, serial, days_until_maintenance)

    def sales_menu(self):
        print(
            "\n============ Welcome to our School Vending Machine ============ \nWe hope you have a great day full of learning!")
        VendingMachine.sales_menu(self)

    def find_snack_price(self, snack):
        return SchoolVendingMachine.snack_prices[snack]

    def print_student_debt(self, name):
        print(f'{name} has a debt of {self.student_debt[name]}')
