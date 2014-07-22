import sys
import ast
import numpy
import cmath
import heapq


def findAveragePoint(pointList):
	return (numpy.mean(zip(*pointList)[0]),numpy.mean(zip(*pointList)[1]))
		
def circularSort(coordinates):
	heap = []
	sortedCoordinates = []
	coordinatesPolar = [cmath.polar(complex(x,y)) for (x,y) in coordinates]
	for i in range(0,len(coordinates)):
		heapq.heappush(heap,(coordinatesPolar[i][1],coordinates[i]))
	while(len(heap) > 0):
		sortedCoordinates.append(heapq.heappop(heap)[1])
	return sortedCoordinates
		
if len(sys.argv) != 2:
	print 'Usage: hextobit.py [filename]'
	sys.exit;

coordinates = []
term1 = 0
term2 = 0
with open(sys.argv[1], 'r') as f:
	lines = f.read().splitlines()
	for line in lines:
		coordinates.append(ast.literal_eval(line))
	newCenter = findAveragePoint(coordinates)
	coordinates = [(x-newCenter[0],y-newCenter[1]) for (x,y) in coordinates]
	coordinates = circularSort(coordinates)
	for i in range(0,len(coordinates)-1):
		term1 = term1 + coordinates[i][0]*coordinates[i+1][1]
	term1 = term1 + coordinates[len(coordinates)-1][0]*coordinates[0][1]
	for i in range(0,len(coordinates)-1):
		term2 = term2 + coordinates[i+1][0]*coordinates[i][1]
	term2 = term2 + coordinates[len(coordinates)-1][1]*coordinates[0][0]
	print 0.5*(float(term1) - float(term2))