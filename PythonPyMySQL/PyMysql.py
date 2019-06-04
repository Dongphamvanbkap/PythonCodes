# Task: 
# 1- Connect to the database.
# 2- Create a table named user.
# 3- Insert fake information to the table.
# 4- Select rows and print the table.
# 5- Insert, Update, Delete database by Id.

# Solution:

import datetime
import pymysql
import random


# 1 Connect to the database.
connection = pymysql.connect(
	host = "localhost",
	user = "admin",
	password = "123456a@",
	database = "PT1812LM",
	charset = "utf8mb4",
	cursorclass = pymysql.cursors.DictCursor
	)
cursor = connection.cursor()
print("Successfully Connected\n")


# 2 Create table named user.
del_existing_table = "DROP TABLE IF EXISTS user"
cre_table_query = """CREATE TABLE user(
	id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(45) NOT NULL,
	gender INT,
	age INT,
	phone VARCHAR(45),
	email VARCHAR(100),
	address VARCHAR(100),
	date_create DATE)"""

try:
	cursor.execute(del_existing_table)
	print("Existing  tables has been deleted\n")
	cursor.execute(cre_table_query)
	print("User table has been created\n")

except Exception as e:
	print("Exception: ", e)


# 3 Insert fake information to user table
first_names = ['John', 'Jane', 'Corey', 'Travis', 'Dave', 'Kurt', 'Neil', 'Sam', 'Steve', 'Tom', 'James', 'Robert', 'Michael', 'Charles', 'Joe', 'Mary', 'Maggie', 'Nicole', 'Patricia', 'Linda', 'Barbara', 'Elizabeth', 'Laura', 'Jennifer', 'Maria']

last_names = ['Smith', 'Doe', 'Jenkins', 'Robinson', 'Davis', 'Stuart', 'Jefferson', 'Jacobs', 'Wright', 'Patterson', 'Wilks', 'Arnold', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin']

street_names = ['Main', 'High', 'Pearl', 'Maple', 'Park', 'Oak', 'Pine', 'Cedar', 'Elm', 'Washington', 'Lake', 'Hill']

fake_cities = ['Metropolis', 'Eerie', "King's Landing", 'Sunnydale', 'Bedrock', 'South Park', 'Atlantis', 'Mordor', 'Olympus', 'Dawnstar', 'Balmora', 'Gotham', 'Springfield', 'Quahog', 'Smalltown', 'Epicburg', 'Pythonville', 'Faketown', 'Westworld', 'Thundera', 'Vice City', 'Blackwater', 'Oldtown', 'Valyria', 'Winterfell', 'Braavos‎', 'Lakeview']

states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']

first_phone_num = [86, 96, 97, 98, 32, 33, 34, 35, 36, 37, 38, 39, 89, 90, 93, 70, 79, 77, 76, 78, 88, 91, 94, 83, 84, 85, 81, 82]

for num in range(11):
	first = random.choice(first_names)
	last = random.choice(last_names)
	name = f"{first} {last}"

	gender = random.randint(0, 1)

	age = random.randint(15, 80)

	phone = f'{random.choice(first_phone_num):03} {random.randint(100, 999)} {random.randint(1000,9999)}'

	email = first.lower() + last.lower() + '@gmail.com'

	street_num = random.randint(100, 999)
	street = random.choice(street_names)
	city = random.choice(fake_cities)
	state = random.choice(states)
	zip_code = random.randint(10000, 99999)
	address = f'{street_num} {street} St., {city} {state} {zip_code}'

	date_create = datetime.datetime.now().strftime("%Y-%m-%d")


	insert_query = "INSERT INTO user(name, gender, age, phone, email, address, date_create) VALUES(%s,%s,%s,%s,%s,%s,%s)"
	
	try:
		cursor.execute(insert_query, (name, gender, age, phone, email, address, date_create))
		connection.commit()

	except Exception as e:
		print("Exception: ",e)

# for costummer in  costumers:
# 	name = costummer["name"]
# 	gender = costummer["gender"]
# 	age = costummer["age"]
# 	address = costummer["address"]
# 	email = costummer["email"]
# 	date_create = datetime.datetime.now().strftime("%Y-%m-%d")
# 	# print("{}\t{}\t{}\t{}\t{}\t{}".format(name, gender, age, address, email, date_create))

# 	insert_query = "INSERT INTO user(name, gender, age, address, email, date_create) VALUES(%s,%s,%s,%s,%s,%s)"

	# try:
	# 	cursor.execute(insert_query,(name, gender, age, address, email, date_create))
	# 	connection.commit()
	
	# except Exception as e:
	# 	print("Exception: ",e)

print("Insert Sucessfully!\n")


# 4- Select rows and print the table.
sql_query ="SELECT * FROM user"

try:
	cursor.execute(sql_query)
	results = cursor.fetchall()
	print("User table:")
	print("ID\tName\t\t\tGender\tAge\tPhone\t\t\tEmail\t\t\tAddress\t\t\tDate_create")

	for row in results:
		print("{}\t{}\t\t{}\t{}\t{}\t\t{}\t\t{}\t\t\t{}".format(row["id"], row["name"], row["gender"], row["age"], row["phone"], row["email"], row["address"], row["date_create"]))

except Exception as e:
	print("Exception occured", e)


# 5 Update and Delete data:
while True:
	opt = input("\nChoise options you want to use.\nInsert[i] | Update[u] | Delete[d] | ListData[l] | Exit[e]:")
	print()

	if opt == "u" or opt == "U":
		update_query = "UPDATE user SET name=%s, gender=%s, age=%s, phone=%s, email=%s, address=%s WHERE id=%s"
		Id = input("Update data.\nWhich Id do you want to update: ")
		name = input("Input user name: ")
		gender = input("Input user gender: ")
		age = input("Input user age: ")
		phone = input("Input user phone: ")
		email = input("Input user email: ")
		address = input("Input user address: ")

		try:
			cursor.execute(update_query,(name, gender, age, phone, email, address, Id))
			connection.commit()
			print("Update Sucessfully!\n")
	
		except Exception as e:
			print("Exception: ",e)

	elif opt == "d" or opt == "D":
		del_query = "DELETE FROM user WHERE id=%s"
		Id = input("Delete data.\nWhich Id do you want to delete: ")

		try:
			cursor.execute(del_query,(Id))
			connection.commit()
			print("Delete Sucessfully!\n")
	
		except Exception as e:
			print("Exception: ",e)

	elif opt == "l" or opt == "L":
		sql_query ="SELECT * FROM user"

		try:
			cursor.execute(sql_query)
			results = cursor.fetchall()
			print("User table:")
			print("ID\tName\t\t\tGender\tAge\tPhone\t\t\tEmail\t\t\tAddress\t\t\tDate_create")

			for row in results:
				print("{}\t{}\t\t{}\t{}\t{}\t\t{}\t\t{}\t\t{}".format(row["id"], row["name"], row["gender"], row["age"], row["phone"], row["email"], row["address"], row["date_create"]))

		except Exception as e:
			print("Exception occured", e)

	elif opt == "i" or opt == "I":
		insert_query = "INSERT INTO user(name, gender, age, phone, email, address, date_create) VALUES(%s,%s,%s,%s,%s,%s,%s)"
		name = input("Input data.\nInput user name: ")
		gender = input("Input user gender: ")
		age = input("Input user age: ")
		phone = input("Input user phone: ")
		email = input("Input user email: ")
		address = input("Input user address: ")
		date_create = datetime.datetime.now().strftime("%Y-%m-%d")

		try:
			cursor.execute(insert_query,(name, gender, age, phone, email, address, date_create))
			connection.commit()
			print("Insert Sucessfully!\n")
		
		except Exception as e:
			print("Exception: ",e)

	elif opt == "e" or opt == "E":
		print("Exit program, Goodbye!")
		break

	else:
		print("Please, Choose the right option!")

connection.close()