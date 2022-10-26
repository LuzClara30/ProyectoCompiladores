parser grammar MonkeyParser;

options{
tokenVocab = MonkeyLexer;
}

program:    statement*                                                          #programAST;
statement: LET letStatement                                                     #letStatAST
           | RETURN returnStatement                                             #rtrnStatAST
           | expressionStatement                                                #exprsStatStatAST;
letStatement: ID EQUALS expression ( SEMICOLON|  )                              #idEqLetStatAST;
returnStatement: expression ( SEMICOLON|  )                                     #exprsRtrnStatAST;
expressionStatement: expression ( SEMICOLON| )                                  #exprsExprsStatAST;
expression:  additionExpression comparison                                      #addExprsExprsAST;
comparison: ((GREATERTHAN|LOWERTHAN|LTE|GTE|EQUALE)additionExpression)*         #eqlsComparsAST;
additionExpression: multiplicationExpression additionFactor                     #multAddExprsAST;
additionFactor: ((ADD|SUB) multiplicationExpression)*                           #multAddFctrAST;
multiplicationExpression: elementExpression multiplicationFactor                #elmtMultExprsAST;
multiplicationFactor: ((MULT|DIV) elementExpression)*                           #multDivElmtMultFctrAST;
elementExpression: primitiveExpression (elementAccess | callExpression |  )     #prmtElmtExprsAST;
elementAccess: BRACKETSOP expression BRACKETSCL                                 #brckExprsElmtAccsAST;
callExpression: POPEN expressionList PCLOSE                                     #prthsCllExprsAST;
primitiveExpression: INT                                                        #intPrmtvExprsAST
                     | STRING                                                   #strnPrmtvExprgAST
                     | ID                                                       #idPrmtvAST
                     | TRUE                                                     #trPrmtAST
                     | FALSE                                                    #falsPrmtvExprsAST
                     | POPEN expression PCLOSE                                  #prthsPrmtvExprsAST
                     | arrayLiteral                                             #arryLitPrmtvExprsAST
                     | arrayFunctions ( expressionList )                        #arryFnctnPrmtvExprsAST
                     | functionLiteral                                          #fnctnLitPrmtvExprsAST
                     | hashLiteral                                              #hshLitPrmtvExprsAST
                     | printExpression                                          #prntExprsPrmtvExprsAST
                     | ifExpression                                             #ifExprsPrmtvExprsAST;
arrayFunctions: LEN | FIRST | LAST | REST | PUSH                                #grouparryFnctnAST;
arrayLiteral:   BRACKETSOP expressionList BRACKETSCL                            #brckExprsLstarryLitAST;
functionLiteral: FN POPEN functionParameters PCLOSE blockStatement              #fnctnPrmtsBlckStatFnctnLitAST;
functionParameters: ID moreIdentifiers                                          #mrIdsFnctnPrmtsAST;
moreIdentifiers: (COMMA ID)*                                                    #cmmaIdMrIdsAST;
hashLiteral: CURLYOP hashContent moreHashContent CURLYCL                        #hshCtntMrHshCtntHshLitAST;
hashContent	: expression COLON expression                                       #exprsClnExprsHshCtntAST;
moreHashContent	: (COMMA hashContent)*                                          #cmmaHshCtntMrHshCtntAST;
expressionList: expression moreExpressions                                      #exprsMrExprsExprsLstAST
                    |                                                           #emptExprsLstASTAST;
moreExpressions: (COMMA expression)*                                            #cmmaExprsMrExprsAST;
printExpression: PUTS POPEN expression PCLOSE                                   #ptsExprsPrntExprsAST;
ifExpression: IF expression blockStatement (ELSE blockStatement |  )            #ifExprsBlckStatElsBlckStatIdExprsAST;
blockStatement	: CURLYOP statement* CURLYCL                                    #stntBlckStatAST;