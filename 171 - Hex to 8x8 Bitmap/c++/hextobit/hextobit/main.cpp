#include <stdio.h>

// Credit to the idea of implementing this function this way goes to reddit
// user "skeeto":
// http://www.reddit.com/r/dailyprogrammer/comments/2ao99p/7142014_challenge_171_easy_hex_to_8x8_bitmap/cixadsp
int main(int argc,char* argv [])
{
	if( argc != 2)
	{
		printf("Usage: hextobit.exe [filename]\n");
		return 0;
	}
	int value;
	FILE* pInputFile = fopen(argv[1],"r");
	FILE* pOutputFile = fopen("output.txt","w");

	while(!feof(pInputFile))
	{
		fscanf(pInputFile,"%2x",&value);
		for(int i = 0 ; i < 8; i++)
			fputc(value & 0x80 >> i ? 'x' : ' ',pOutputFile);
		fputc('\n',pOutputFile);
	}

	fclose(pInputFile);
	fclose(pOutputFile);
}