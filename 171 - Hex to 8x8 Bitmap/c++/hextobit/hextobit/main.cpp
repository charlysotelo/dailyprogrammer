#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int digitHexToInt(char c)
{
	switch(c)
	{
	case 'A':
		return 10;
	case 'B':
		return 11;
	case 'C':
		return 12;
	case 'D':
		return 13;
	case 'E':
		return 14;
	case 'F':
		return 15;
	default:
		return c - '0';
		break;
	}
}

int hexToInt(char hexString[])
{
	int returnValue = 0;
	for( int i = 0; hexString[i] != '\0'; i++)
		returnValue = 16*returnValue + digitHexToInt(hexString[i]);

	return returnValue;
}

void fillHexValues(int hexValues[],const char* hexString)
{
	int nextHexIndex = 0;
	for( int i = 0; ; i++)
	{
		if(hexString[i] == ' ' || hexString[i] == '\0')
		{
			char hexValueString[3];
			hexValueString[0] = hexString[i-2];
			hexValueString[1] = hexString[i-1];
			hexValueString[2] = '\0';
			hexValues[nextHexIndex] = hexToInt(hexValueString);
			nextHexIndex++;

			if(hexString[i] == '\0')
				return;
		}
	}
}

int main(int argc,char* argv [])
{
	if( argc != 2)
	{
		printf("Usage: hextobit.exe [filename]\n");
		return 0;
	}

	ifstream myInput;
	ofstream myOutput;
	int hexValues[8];
	bool bitmap[8][8];

	myInput.open(argv[1]);
	myOutput.open("output.txt");

	string line;
	getline(myInput,line);
	fillHexValues(hexValues,line.c_str());
	
	for(int i = 0; i < 8; i++)
		for (int j = 0; j < 8; j++)
			bitmap[i][j] = hexValues[i] & (1 << 7 - j) ;

	// Print out our bitmap:
	for(int i = 0; i < 8; i++)
	{
		if( i != 0 )
			myOutput << endl;
		for (int j = 0; j < 8; j++)
		{
			if(bitmap[i][j])
				myOutput << "x";
			else
				myOutput << " ";
		}
	}

	myInput.close();
	myOutput.close();
	return 0;
}