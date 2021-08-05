print("="*20)
customer_name = ['Jan', 'David', 'Jack', 'Eloit']
customer_pins = ['0123', '4561', '7891', '1011']
customer_balances = [1000, 2000, 3000, 4000]


while True:
	print("+"*20)
	print("+++++ welcome +++++")
	print("1- Open a new account.")
	print("2- Withdraw Money.")
	print("3- Deposit Money.")
	print("4- Check Customer & Balance.")
	print("5- Exit")
	print("+"*20)
	
	choice_number = input("Select your choice: ")
	
	
	if choice_number == "1":	
		print("++++++ Customer registration ++++++")
		name = input("Enter fullname: ")
		customer_name.append(name)
		pin = str(input("Enter pin: "))
		customer_pins.append(pin)
		balance = 0
		deposition = int(input("Enter a value to deposit to start an account: "))
		balance = balance + deposition
		customer_balances.append(balance)
		print("--- new account created successfully ! ---")
		
	
	elif choice_number == "2":
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
	
	
	elif choice_number == "3":
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
			
	elif choice_number == "4":
		print("Customer name list and balances mentioned below :")
		for item in range(len(customer_name)):
			print(customer_name[item],customer_balances[item])
			
	
	elif choice_number == "5":
		print("Thank you for using our banking system!")
		break
	else:
		print("Invalid option selected by the customer")
  		
        
					
	
	
	
