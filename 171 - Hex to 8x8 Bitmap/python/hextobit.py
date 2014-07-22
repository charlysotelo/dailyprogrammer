import sys

if len(sys.argv) != 2:
	print 'Usage: hextobit.py [filename]'
	sys.exit;

hexlist = []
bitmap = []
with open(sys.argv[1], 'r') as f:
	with open('output.txt','w') as fw:
		hexlist = f.readline().split()
		hexlist = [int(x,16) for x in hexlist]
		for hexValue in hexlist:
			row = []
			for i in range(0,8):
				if hexValue & 1 << 7 - i :
					row.append(1)
				else:
					row.append(0)
			bitmap.append(row)
		
		firstRow = True
		for row in bitmap:
			if not firstRow:
				fw.write('\n')
			firstRow = False
			for element in row:
				if element == 1:
					fw.write('x')
				else:
					fw.write(' ')