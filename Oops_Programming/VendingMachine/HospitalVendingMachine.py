from Oops_Programming.VendingMachine.VendingMachine import VendingMachine


class HospitalVendingMachine(VendingMachine):
    snack_prices = {"candy": 3.00, "soda": 2.50, "chips": 4.00, "cookies": 4.50}

    def __init__(self, inventory, serial, days_until_maintenance):
        VendingMachine.__init__(self, inventory, serial, days_until_maintenance)

    # Complete the class
    def sales_menu(self):
        print(
            "\n============ Welcome to our Hospital Vending Machine ============ \nWe hope you are feeling better today!\n")
        VendingMachine.sales_menu(self)

    def find_snack_price(self, snack):
        return HospitalVendingMachine.snack_prices[snack]

    def print_days_until_maintenance(self):
        print(f'{self.days_until_maintenance} days are remaining until the machine needs maintenance')
