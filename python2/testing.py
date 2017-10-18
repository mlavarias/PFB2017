count = 53 # defines number
if count > 0: #tells if positive
	if count < 50: #tells if greater than 50
		if count%2 == 0:
			message = "is even and smaller than 50"
			print(count, message)
		else:
			message = "is odd and smaller than 50"
			print(count,message)
	elif count >=50:
		if count%3 == 0:
			message = "is divisible by 3 and greater than 50"
			print(count, message)
		else:
			message = "is not divisible by 3 but is greater than 50"
			print(count,message)
else:
        message = "is negative"
        print(count, message)
