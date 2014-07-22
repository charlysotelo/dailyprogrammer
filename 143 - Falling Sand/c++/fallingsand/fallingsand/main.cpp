#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

int getFallRate(char c)
{
	if(c == '.')
		return 1;
	else
		return 0;
}

// Simulates one tick. Returns true if there was a change
bool simulate(char** pSandGrid,int height, int width)
{
	bool ChangeDetected = false;
	for (int i = height -1; i >= 0; i--)
	{
		for (int j = 0; j < width; j++)
		{
			int fallRate = getFallRate(pSandGrid[i][j]);
			if(fallRate > 0 && i + fallRate < height && pSandGrid[i + fallRate][j] == ' ')
			{
				pSandGrid[i + fallRate][j] = pSandGrid[i][j];
				pSandGrid[i][j] = ' ';
				ChangeDetected = true;
			}
		}
	}

	return ChangeDetected;
}

int main(int argc, char* argv[])
{
	if (argc != 2)
	{
		printf("Usage: fallingsand.exe <file>\n");
		return 0;
	}

	ifstream myInput;
	ofstream myOutput;

	myInput.open(argv[1]);
	myOutput.open("ouput.txt");

	int width = 0, height = 0;
	vector<string> lines;


	if(myInput.is_open())
	{
		string line;
		while(getline(myInput,line))
			lines.push_back(line);
	}

	if(!lines.empty())
	{
		width = lines[0].length();
		height = lines.size();
		char** pSandGrid = new char*[height];
		for (int i = 0; i < height; i++)
			pSandGrid[i] = new char[width];


		// Fill our grid in
		for (int i = 0 ; i < height; i++)
			for (int j = 0 ; j < width; j++)
				pSandGrid[i][j] = lines[i][j];

		while(simulate(pSandGrid,height,width)) {}


		// Output our results to our file
		for (int i = 0 ; i < height; i++)
		{
			if(i != 0 )
				myOutput << endl;

			for (int j = 0 ; j < width; j++)
				myOutput << pSandGrid[i][j];
		}

		// Cleanup our grid!
		for (int i = 0; i < height; i++)
			delete [] pSandGrid[i];
		delete [] pSandGrid;
	}

	myInput.close();
	myOutput.close();

	return 0;
}