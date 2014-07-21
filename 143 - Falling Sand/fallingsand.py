import sys

#returns fallrate
def fallRate(char):
	if char == '.':
		return 1;
	else:
		return 0;
		
if len(sys.argv) != 2:
	print 'Usage: fallingsand.py [filename]'
	sys.exit;
	
f = open(sys.argv[1])
fw = open('output.txt','w')
sandGrid = []

for line in f:
	if line[-1] == '\n':
		line = line[0:len(line)-1]
	sandGrid.append(list(line))
dimensions = [len(sandGrid),len(sandGrid[0])] #height,width

for row in range(dimensions[0]-1,-1,-1):
	for col in range(0,dimensions[1]):
		rate = fallRate(sandGrid[row][col])
		if( rate > 0 and row + rate < dimensions[0] and sandGrid[row+rate][col] == ' '): #physics object
			sandGrid[row+rate][col] = sandGrid[row][col]
			sandGrid[row][col] = ' '

firstLine = True
for row in sandGrid:
	if not firstLine:
		fw.write('\n')
	firstLine = False
	for element in row:
		fw.write(str(element))
		
f.close()
fw.close()