#OTP GENERATOR PROGRAM
#MADE BY ATHARVA BHIDE

import random

print("WELCOME TO THE OTP GENERATOR")
print("")

print("THIS GENERATOR GENERATES A 4 DIGIT OTP")
print("")
while True:
	print("Type START/EXIT below to start/exit the generator!")

	startexit = input()

	if startexit=="START":

		otp = random.randint(1000, 9999)

		print("The generated otp is ", otp)
		

	elif startexit=="EXIT":
		break

	else:
		print("Please enter a valid input!")

	continue



		
	
	



