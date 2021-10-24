from Oops_Programming.VendingMachine.HospitalVendingMachine import HospitalVendingMachine
from Oops_Programming.VendingMachine.SchoolVendingMachine import SchoolVendingMachine
from Oops_Programming.VendingMachine.VendingMachine import VendingMachine

# Instances =============================================================================================


floor_machine = VendingMachine({"candy": 36, "soda": 15, "chips": 40, "cookies": 120}, "011423424", 24)
# floor_machine.sales_menu()

hospital_machine = HospitalVendingMachine({"candy": 32, "soda": 50, "chips": 45, "cookies": 80}, "03223424", 15)
hospital_machine.sales_menu()
chips_rate = hospital_machine.find_snack_price('chips')
print(f'chips price is : {chips_rate}')
hospital_machine.print_days_until_maintenance()

school_machine = SchoolVendingMachine({"candy": 36, "soda": 15, "chips": 40, "cookies": 120}, "0534424", 2)
# school_machine.sales_menu()
