/*********************************************************** 
* Game of Life - Project 1
*
* Aron Ockerse
* February 12, 2018
************************************************************/

#include <stdlib.h>
#include <stdio.h>
#include "helper.h"
#include <stdio.h>
#include <ctype.h>

int main(int argc, char* argv[]){
	
	/** sets row and column based on argv parameter*/
	int row = atoi(argv[1]);
	int column = atoi(argv[2]);	

	/** for loop parameters*/
	int i = 0;
	int j = 0;

	/** used for playing game*/
	char ch;

	/** for read and write file functions not used*/
	char* file1;
	char* file2;
	int filesize;

	/** creating a new board*/
	int** pBoard = initialize_board(row,column);		

	/** */
	FILE *fC;
	FILE *fP;	
	fC = fopen("readLife.txt","r");
	fP = fopen("writeLife.txt","w");	

	/** option message*/
	printf("press 'c' to continue next generation\n");
	printf("press 'q' to quit\n");
	printf("press 'l' to load\n");
	printf("pres 's' to save file\n");
	scanf("%s", &ch);		
	
	/** continues looping until uses presses q*/
	while (ch != 'q'){
		
		if(ch != 'c' || ch != 'q'){
			printf("press 'c' to continue next generation\n");
			printf("press 'q' to quit\n");
			printf("press 'l' to load file\n");
			printf("press 's' to save file\n");
			printf("\n");
		}		

		if(ch == 'c'){
			check_neighbors(row, column, pBoard);
		}

		if(ch == 'l'){
			for (i = 0; i < row; i++){
				for (j = 0; j < column; j++){
					fscanf(fC, "%1d", &pBoard[i][j]);
				}
			}

			for (i = 0; i < row; i++){
				for (j = 0; j < column; j++){
					printf("%d ", pBoard[i][j]);
				}
				printf("\n");
			}	
		}		
		
		if(ch == 's'){
			fprintf(fP, "\n");
			for (i = 0; i < row; i++){
				for (j = 0; j < column; j++){
					fprintf(fP, "%d ", pBoard[i][j]);
				}
				fprintf(fP, "\n");
			}
		
			fclose(fP);
		}
		
		scanf("%s", &ch);
	}

	printf("\n");
	
	/** frees memory*/	
	for (i = 0; i < row; i++){
		free(pBoard[i]);
	}

	free(pBoard);

	return 0;


}
