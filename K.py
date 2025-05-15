for i in range(7):
	for j in range(6):
		if j==0 or i+j==3 or i-j==3:
			print("K",end=" ")
		else:
			print(" ",end=" ")
	print()