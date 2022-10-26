lexer grammar MonkeyLexer;

//Simbolos y operadores
MULT        : '*';
DIV         : '/' ;
ADD         : '+' ;
SUB         : '-' ;
EQUALS      : '=';
NOTEQUALS   : '!=';
GREATERTHAN : '>';
LOWERTHAN   : '<';
COLON   : ':';
SEMICOLON : ';';
POPEN   : '(';
PCLOSE  : ')';
GTE: '>=';
LTE : '<=';
EQUALE: '==';
BRACKETSOP: '[';
BRACKETSCL: ']';
COMMA:  ',';
CURLYOP: '{';
CURLYCL: '}';

//Palabras reservadas y constantes booleanas
LET         : 'let';
TRUE        : 'true';
FALSE       : 'false';
IF          : 'if';
ELSE        : 'else';
RETURN      : 'return';
LEN         : 'len';
FIRST       : 'first';
LAST        : 'last';
REST        : 'rest';
PUSH        : 'push';
FN          : 'fn';
PUTS        : 'puts';



//Expresiones complejas
ID          : LETTER (LETTER|DIGIT)*;

//Constantes numéricas
INT         : [0-9]+ ;

//Cadena
STRING : '"' .*? '"' ;

fragment LETTER : 'a'..'z' | 'A'..'Z'| '_';
fragment DIGIT  : '0'..'9' ;

WS              :   [ \t\n\r]+ -> skip ;
LINE_COMMENT    : '//' .*? '\n' -> skip ;
COMMENT         : '/*' .*? '*/' -> skip ;