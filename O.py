for i in range(8):
	for j in range(5):
		if (j==0 or j==4) and 1<i<6 or (i==1 or i==6) and 0<j<4:
			print("O",end=" ")
		else:
			print(" ",end=" ")
	print()