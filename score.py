try:
	inp = raw_input("Enter your score (0.0 to 1.0): ")
	score = float(inp)
except:
	print 'Error. Please enter numeric input'
	quit()

if score < 0.6:
	print 'F'
	
elif 0.7 > score >= 0.6:
	print 'D'
	
elif 0.8 > score >= 0.7:
	print 'C'
	
elif 0.9 > score >= 0.8:
	print 'B'
	
elif 1.0 >= score >= 0.9:
	print 'A'
	

else:
	print 'Error. Please enter score between 0.0 and 1.0'
