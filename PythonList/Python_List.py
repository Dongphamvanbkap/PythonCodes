# Task:
# 1- Create a list for user to input elements.
# 2- Ask the user to add more elements to the list or not.
# 3- If the element's already existed, ask the user still want to add or not.


# Solution.

# 1- Create a list for user to input elements.
_list = []
num_of_element = int(input("Create a list.\nInput the number of elements:"))
print()
for i in range(num_of_element):
	element_1 = input("Input the value of the element indexing at {}: ".format(i))
	try:
		element_1 = int(element_1)
		print("Add successfully an integer number.\n")
	except ValueError as e:
		try:
			element_1 = float(element_1)
			print("Add successfully a decimal number.\n")
		except:
			print("Add successfully a string.\n")
	finally:
		_list.append(element_1)
print("Your List: ",_list, "\n")

# 2- Ask the user to add more elements to the list or not.
# 3- If the element's already existed, ask the user still want to add or not.
while True:
	opt = input("Do you want to add more elements to the list [y/n]: ")
	print()
	if (opt == "y" or opt == "Y"):
		num_of_add_element = int(input("Input the number of additional elements: "))
		print()
		while True:
			element_2 = input("Input the value of additional elements: ")
			try:
				element_2 = int(element_2)
				print("You've inputed an integer number.")
			except ValueError as e:
				try:
					element_2 = float(element_2)
					print("You've inputed a decimal number.")
				except:
					print("You've inputed a string.")
			finally:
				if element_2 in _list:
					print("The value's already existed.")
					sub_opt = input("Do you still want to add this value [y/n]: ")
					if sub_opt =="y" or sub_opt == "Y":
						_list.append(element_2)
						print("Add successfully.\n")
					else:
						print("This value will not be added to the list.\n")
				else:
					_list.append(element_2)
					print("Add successfully.\n")
			if len(_list) == num_of_element +num_of_add_element:
				print("Your List after adding elements: ",_list, "\n")
				num_of_element = len(_list)
				break
		# break		
	elif (opt == "n" or opt == "N"):
		print("Your List: ",_list, "\nEnding program!")
		break
	else:
		print("Please, Input correct options.\n")
