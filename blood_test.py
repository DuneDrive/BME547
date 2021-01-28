def interface():
	print("Blood Test Analysis")
	while True:
		print("\nOptions")
		print("1 - HDL")
		print("9 - Quit")
		choice = input("Enter an option: ");
		if choice == "9":
			return
		elif choice == "1":
			HDL_driver()


def HDL_driver():
	# Get Data
	HDL_str = input("Enter HDL level: ")
	HDL = int(HDL_str)
	if (HDL >= 60):
		print("HDL Level is Normal")
	elif (HDL >= 40 and HDL <60):
		print("HDL Level is Borderline Low")
	else:
		 print("HDL Level is Low")

	# Analyze Data
	# Output Data



interface()
