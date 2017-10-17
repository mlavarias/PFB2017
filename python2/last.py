count = 20
if count > 0:
	if count < 50:
		message = "is positive, but less than 50"
		print(count,message)
	elif count >=50:
		message = "is positive, but greater than or equal to 50"
		print(count, message)
else:
	message = "is negative"
	print(count, message)
