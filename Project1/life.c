/*******************************************************************
* Game of Life - Project 1
* 
* Aron Ockerse
* February 12, 2018
********************************************************************/

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <sys/stat.h>
#include <unistd.h>
#include <assert.h>
#include "helper.h"

/*****************************************************************
* Initializes board based on two parameters row and column. Returns
* an array of pointers called pBoard.
* @param row number of rows
* @param column number of columns
* @return pBoard
******************************************************************/
int** initialize_board(int row, int column){

	/** a pointer to a pointer holding board values */
	int **pBoard;
		
	/** hold the values for the for loops */
	int i, j;

	// creating memory on the heap references
	// from GeeksforGeeks 
	// https://www.geeksforgeeks.org/dynamically-allocate-2d-array-c/
	pBoard = (int**) (malloc(row * sizeof(int*)));
 
	// fills each row of memory with number of columns
	for (i=0; i<row; i++){
        	pBoard[i] = (int *)malloc(column * sizeof(int));
	
 	}
    
	// fills array with 0's
	for (i = 0; i <  row; i++){
      		for (j = 0; j < column; j++){
         		pBoard[i][j] = 0;
		}
	}

	// prints initialized array 
    	for (i = 0; i <  row; i++){
      		for (j = 0; j < column; j++){
         		printf("%d ", pBoard[i][j]);	
		}

	printf("\n");

	}
	printf("\n");	
	
	return pBoard;
}

/*************************************************************
* Game logic runs through each element of the array and checks 
* each direction for each rule of the game of life
* @param row number of rows
* @param column number of columns
* @param boardArray passes in an array
**************************************************************/
void check_neighbors(int row, int column, int** boardArray){

	/** holds values for the for loops  */
	int i, j;
	int inc = 0;
	int temp = 0;

	/** extra board arrays to make copies */
	int **pBoard;
	int **pBoard2;	

	/** mallocs memory based on row size */
	pBoard = (int**) (malloc(row * sizeof(int*)));
     	pBoard2 = (int**) (malloc(row * sizeof(int*)));

	//** fills each row of memory with number of columns */
	for (i=0; i<row; i++){
        	pBoard[i] = (int *)malloc(column * sizeof(int));
        	pBoard2[i] = (int *)malloc(column * sizeof(int));
 
 	}

	/** fills pBoard with 0's*/
	for (i = 0; i <  row; i++){
      		for (j = 0; j < column; j++){
         		pBoard[i][j] = 0;
		}
	}

	/** sets pBoard equal to boardArray parameter*/ 
	for (i = 0; i <  row; i++){
      		for (j = 0; j < column; j++){
         		pBoard[i][j] = boardArray[i][j];
			pBoard2[i][j] = boardArray[i][j];
		}
	}

	/** game logic checks if current position is either 1 or 0
	iterates through each part of array and checks for
	 1's and increments inc respectively*/
	for (i = 1; i < row - 1; i++){
		for (j = 1; j < column - 1; j++){
			
			inc = 0;

			if (boardArray[i][j] == 1){
				if (boardArray[i+1][j] == 1){
					inc++;
				}
				
				if (boardArray[i-1][j] == 1){
					inc++;
				}
				
				if (boardArray[i][j+1] == 1){
					inc++;
				}

				if (boardArray[i][j-1] == 1){
					inc++;
				}

				if (boardArray[i+1][j+1] == 1){
					inc++;
				}

				if (boardArray[i+1][j-1] == 1){
					inc++;
				}

				if (boardArray[i-1][j+1] == 1){
					inc++;
				}

				if (boardArray[i-1][j-1] == 1){
					inc++;
				}

				/** if current position has less 
				than 2 or more than 3 the cell dies*/
				if (inc < 2 || inc > 3){
					pBoard[i][j] = -1;
				}
				
				/** if current position has exactly 
				2 or 3 neighbors the cell lives*/
				if (inc == 2 || inc == 3){
					pBoard[i][j] = 1;
				}
                                inc = 0;

                        }else{

                                if (boardArray[i+1][j] == 1){
                                        inc++;
                                }

                                if (boardArray[i-1][j] == 1){
                                        inc++;
                                }

                                if (boardArray[i][j+1] == 1){
                                        inc++;
				}
 				if (boardArray[i][j-1] == 1){
                                        inc++;
                                }

                                if (boardArray[i+1][j-1] == 1){
                                        inc++;
                                }

                                if (boardArray[i-1][j-1] == 1){
                                        inc++;
                                }

                                if (boardArray[i-1][j+1] == 1){
                                        inc++;
                                }

                                if (boardArray[i+1][j+1] == 1){
                                        inc++;
                                }  

				/** if dead cell has exactly 3 neighbors
				it comes back to life*/
                                if (inc == 3){
                                        pBoard[i][j] = 1;
                                }

                                inc = 0;
                        
			}

		}
	}
	
	/** resets boards */
	for (i = 0; i <  row; i++){
      		for (j = 0; j < column; j++){
         		boardArray[i][j] = pBoard[i][j];
			
		}
	}

	/** prints board status*/ 
	for (i = 0; i <  row; i++){
      		for (j = 0; j < column; j++){
         		printf("%d ", boardArray[i][j]);
		}
		printf("\n");
	}

}

/**********************************************
* read_file method is supposed to read in a file
* and return file size but is not actually used
* @param filename name of file
* @param buffer board array
* @return size file size
**********************************************/
int read_file(char* filename, int **buffer) {
	FILE* file;
  	file = fopen(filename, "r");

  	struct stat st;
  	stat(filename, &st);
  	int size = st.st_size;

  	*buffer = malloc(size);
  	fread(*buffer, size, 1, file);
	fclose(file);

	return size;
}

/********************************************************
* write_file is supposed to take in a file and it's size
* and write it out to a text file but it does not work
* @param filename name of file
* @param buffer pointer to array
* @param size size of file
* @return size file size
********************************************************/
int write_file(char* filename, int *buffer, int size) {
  	FILE* file = fopen(filename, "w"); 
	int k;

  	for (k = size - 1; k >= 0; k--) {
    		fwrite(buffer + k, 1, 1, file);
  	}
	
  	fclose(file);

	return size;
}
