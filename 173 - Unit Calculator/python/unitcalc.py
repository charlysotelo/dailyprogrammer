#Nested Dictionary implementation:

dict = {'meters': {'meters': 1.0, 'inches': 39.3701, 'miles': 0.000621371, 'attoparsecs': 32.4077929 }, \
		'inches': {'meters': 0.0254, 'inches': 1.0, 'miles': 0.0000157828, 'attoparsecs': 0.82315794 }, \
		'miles': {'meters': 1609.34, 'inches': 63360, 'miles': 1.0, 'attoparsecs': 52155.287 }, \
		'attoparsecs': {'meters': 0.0308567758, 'inches': 1.21483369, 'miles': 0.0000191735116, 'attoparsecs': 1.0 }, \
		'kilograms': {'kilograms': 1.0, 'pounds': 2.20462, 'ounces': 35.274, 'hogsheads of Beryllium': 440.7}, \
		'pounds': {'kilograms': 0.4536, 'pounds': 1.0, 'ounces': 16.0, 'hogsheads of Beryllium': 971.6}, \
		'ounces': {'kilograms': 0.02835, 'pounds': 0.0625, 'ounces': 1.0, 'hogsheads of Beryllium': 0.00006432936635574}, \
		'hogsheads of Beryllium': {'kilograms': 0.002269117, 'pounds': 0.00102923, 'ounces': 15546.0, 'hogsheads of Beryllium': 1.0}}

while(True):
	inputString = raw_input('Usage : <quantity> <unit1> to <unit2>\n')
	inputString = inputString.split()
	toIndex = 0
	inValue = 0.0
	
	if(len(inputString) < 4 ):
		print 'Error: Incorrect ussage. not enough arguments'
		continue
	try:
		inValue = float(inputString[0])
		toIndex = inputString.index('to')
	except:
		print 'Error: Incorrect ussage. delimiter \'to\' not found or first input is not a number'
		continue 
	
	unit1 = ' '.join(inputString[1:toIndex])
	unit2 = ' '.join(inputString[toIndex+1:])
	
	if(len(inputString) > 4):
		inputString[3] = ' '.join(inputString[3:])
	
	try:
		print inputString[0] + ' ' + unit1 + ' is ' + str(inValue*dict[unit1][unit2]) + ' ' + unit2
	except:
		print 'Error: Incorrect ussage. Unit 1 quantity type does not match unit 2'
		continue 
	
	