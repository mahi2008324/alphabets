for i in range(6):
	for j in range(7):
		if j == 0 or j==6 :
			print("M",end=" ")
		elif i+j==6 and j>2:
			print("M",end=" ")
		elif i==j and j<4:
			print("M",end=" ")
		else:		
			print(" ",end=" ")
	print()