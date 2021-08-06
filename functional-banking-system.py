import time

def menu():
	print("+"*20)
	print("+++++ welcome +++++")
	print("1- Open a new account.")
	print("2- Withdraw Money.")
	print("3- Deposit Money.")
	print("4- Check Customer & Balance.")
	print("5- Exit")
	print("+"*20)
	
def get_user_choice(user_number):
	switcher = {
		1: lambda: open_account(),
		2: lambda: withdraw(),
		3: lambda: Deposit(),
		4: lambda: check_customer(),
		5: lambda: exit()
	}
	choice_func = switcher.get(user_number)
	choice_func()

def open_account():
	print("== == == Customer Registration == == == ")
	name = input("Enter fullname: ")
	customer_name.append(name)
	pin = str(input("Enter pin: "))
	customer_pins.append(pin)
	balance = 0
	deposition = int(input("Enter a value to deposit to start an account: "))
	balance = balance + deposition
	customer_balances.append(balance)
	print("--- new account created successfully ! ---") 

def withdraw():
	name = input("Enter name: ")
	pin = input("Enter pin: ")
	for x in range(len(customer_name)):
		balance = int(customer_balances[x])
		if name == customer_name[x]:
			if pin == customer_pins[x]:
				print("Your Current Balance : ", customer_balances[x])
				withdrawal = int(input("Enter Value to Withdraw: "))
				if withdrawal > balance:
					deposition = input("Please Deposit a higher Value because your Balance mentioned above is not enough: ")
				else:
					balance = balance - withdrawal
					print("--- Withdraw Duccessfull!---")
					customer_balances[x] = balance
					print("Your new Balance: ", balance )
					break
				print("Your name and pin does not match!")
				print(customer_name)
				print(customer_balances)

def Deposit():
	name = input("Enter name: ")
	pin = input("Enter pin: ")
	for x in range(len(customer_name)):
		balance = int(customer_balances[x])
		if name == customer_name[x]:
			if pin == customer_pins[x]:
				print("Your Current Balance : ", customer_balances[x])
				deposition = int(input("Enter Value to deposit: "))
				balance = balance + deposition
				customer_balances[x] = balance
				print("---Deposition successful!---")
				print("Your New Balance : ", balance)
				break
			print("Your name and pin does not match!")
			
def check_customer():
	print("Customer name list and balances mentioned below :")
	for item in range(len(customer_name)):
		print(customer_name[item],customer_balances[item])

if __name__ =="__main__":
	customer_name = ['Jan', 'David', 'Jack', 'Eloit']
	customer_pins = ['0123', '4561', '7891', '1011']
	customer_balances = [1000, 2000, 3000, 4000]
	Runـtheـmenu = True
	while Runـtheـmenu: 
		menu()
		user_number = int(input("Select your choice: "))
		if user_number in [1,2,3,4,5]:
			get_user_choice(user_number)
		else:
			print("\n ---> Enter number Between 1 to 5 !!! \n")
			time.sleep(2)
