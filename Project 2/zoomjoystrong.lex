%{
	#include "zoomjoystrong.tab.h"
	#include <stdio.h>
	int fileno(FILE *stream);
%}

%option noyywrap

%%

-?[0-9]+		{ yylval.i = atoi(yytext); return INT; }
-?[0-9]*\.?[0-9]+ 	{ yylval.f = atof(yytext); return FLOAT; }
;			{ return END_STATEMENT; }
point			{ return POINT; }
line			{ return LINE; }
circle			{ return CIRCLE; }
rectangle		{ return RECTANGLE; }
set_color		{ return SET_COLOR; }
end 			{ return END; }

[\t| |\n]		; 
%%
