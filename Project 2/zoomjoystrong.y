%{
	#include <stdio.h>
	#include "zoomjoystrong.h"
	void yyerror(const char* msg);
	int yylex();
%}

%error-verbose

%union {int i; float f;}

%start program

%token END
%token END_STATEMENT
%token POINT
%token LINE
%token CIRCLE
%token RECTANGLE
%token SET_COLOR
%token INT
%token FLOAT

%type<i> INT
%type<f> FLOAT

%%

program:	function_list
		|	function_list program
		;
	
function_list:		point
		|	line
		|	circle
		|	rectangle
		|	set_color
		|	end
	

point:		POINT INT INT END_STATEMENT {
			if($2 < 0 || $2 > WIDTH || $3 < 0 || $3 > HEIGHT){
				yyerror("Index out of bounds");
			}else{
				point($2, $3);
			}
		}
	
line:		LINE INT INT INT INT END_STATEMENT {
			if($2 < 0 || $2 > WIDTH || $3 < 0 || $3 > HEIGHT){
				yyerror("Index out of bounds");
			}else{
				line($2, $3, $4, $5);
			}
		}	
	
circle:		CIRCLE INT INT INT END_STATEMENT {
			if($2 < 0 || $2 > WIDTH || $3 < 0 && $3 > HEIGHT || $4 < 0){
				yyerror("Index out of bounds");
			}else{
				circle($2, $3, $4);
			}
		}
			
rectangle:	RECTANGLE INT INT INT INT END_STATEMENT	{
			if($2 < 0 || $2 > WIDTH || $3 < 0 || $3 > HEIGHT){
				yyerror("Index out of bounds");
			}
				rectangle($2, $3, $4, $5);
		}


set_color:	SET_COLOR INT INT INT END_STATEMENT {
			if($2 < 0 || $3 < 0 || $4 < 0 || $2 > 255 || $3 > 255 || $4 > 255){
				yyerror("Color index out of bound");	
			}else{
				set_color($2, $3, $4);
			}
		}

end:		END END_STATEMENT {
			finish();
		}
		;

%%

int main(int argc, char** argv){
	setup();
	yyparse();
	return (0);
}

void yyerror(const char* msg){
	fprintf(stderr, "ERROR! %s\n", msg);
}


