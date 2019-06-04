# Task: 
# 1- Check the file if exists or not.
# 2- If the file exists, copy it. If not create a file, write to the file and make a copy of it.


# Sollution.
import os

if os.path.exists("text.txt"):
	print("Yes, the file exists. Python is going to copy the file.")
	with open("text.txt","r") as rf:
		with open("text_copy.txt","w") as wf:
			for line in rf:
				wf.write(line)
else:
	print("Sorry, The file does not exists.\nPython will create a file with that name and make a copy of it.")
	with open("text.txt","w") as wf1:
		wf1.write("This is a new file.\nThe file was created automaticlly.\nAfter creating this file. We're going to make a copy of it")
	with open("text.txt","r") as rf:
		with open("text_copy.txt","w") as wf2:
			for line in rf:
				wf2.write(line)	