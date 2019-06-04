li = [-9, 1, -8, 2, -7, 3, -6, 4, 5]

sorted_list1 = sorted(li)
sorted_list2 = sorted(li, reverse = True)
sorted_list3 = sorted(li, key = abs)
li.sort(reverse = True)
li.sort(reverse = False)

# print("Sorted Variable:\t", sorted_list1 )
# print("Sorted Variable:\t", sorted_list2 )
# print("Sorted Variable:\t", sorted_list3 )
# # print("Original Variable:\t", li )

tup = (9, 1, 8, 2, 7, 3, 6, 4, 5)
# There is no method of tup.sort()
sored_tup = sorted(tup)

# print("Sorted Tup:\t",sored_tup)

class employee():
	def __init__(self, name, age, salary):
		self.name = name
		self.age = age
		self.salary = salary

	def __repr__(self):
		return "({},{},${})".format(self.name, self.age, self.salary)

e1 = employee("Carl", 37, 7000000)
e2 = employee("Sarah", 29, 8000000)
e3 = employee("John", 43, 9000000)	

employees = [e1, e2, e3]

sorted_employees = sorted(employees, key = lambda e: e.age)	

print(employees)
print(sorted_employees)