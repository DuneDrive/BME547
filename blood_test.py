def interface():
	print("Blood Test Analysis")
	while True:
		print("\nOptions")
		print("1 - HDL")
		print("2 - LDL")
		print("9 - Quit")
		choice = input("Enter an option: ");
		if choice == "9":
			return
		elif choice == "1":
			HDL_driver()
		elif choice == "2":
			LDL_driver()

def analyze_HDL(HDL):
    if HDL >= 60:
        return "Normal"
    elif 40 <= HDL < 60:
        return "Borderline Low"
    else:
        return "Low"

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

def LDL_driver():
        # Get Data
    LDL_str = input("Enter LDL level: ")
    LDL = int(LDL_str)
    if (LDL < 130):
    	analysis = "Normal"
    elif (LDL >= 130 and LDL <159):
    	analysis = "Borderline High"
    elif (LDL >= 160 and LDL <189):
    	analysis = "High"
    else:
    	analysis = "Very High"
    print("LDL Level is {}".format(analysis))

          
if __name__ == "__main__":
    interface()
