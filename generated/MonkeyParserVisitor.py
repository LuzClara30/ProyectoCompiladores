# Generated from C:/Users/Usuario7/Documents/GitHub/ProyectoCompiladores/ProyectoCompi\MonkeyParser.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MonkeyParser import MonkeyParser
else:
    from MonkeyParser import MonkeyParser

# This class defines a complete generic visitor for a parse tree produced by MonkeyParser.

class MonkeyParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MonkeyParser#programAST.
    def visitProgramAST(self, ctx:MonkeyParser.ProgramASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyParser#letStatAST.
    def visitLetStatAST(self, ctx:MonkeyParser.LetStatASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyParser#rtrnStatAST.
    def visitRtrnStatAST(self, ctx:MonkeyParser.RtrnStatASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyParser#exprsStatStatAST.
    def visitExprsStatStatAST(self, ctx:MonkeyParser.ExprsStatStatASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyParser#idEqLetStatAST.
    def visitIdEqLetStatAST(self, ctx:MonkeyParser.IdEqLetStatASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyParser#exprsRtrnStatAST.
    def visitExprsRtrnStatAST(self, ctx:MonkeyParser.ExprsRtrnStatASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyParser#exprsExprsStatAST.
    def visitExprsExprsStatAST(self, ctx:MonkeyParser.ExprsExprsStatASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyParser#addExprsExprsAST.
    def visitAddExprsExprsAST(self, ctx:MonkeyParser.AddExprsExprsASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyParser#eqlsComparsAST.
    def visitEqlsComparsAST(self, ctx:MonkeyParser.EqlsComparsASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyParser#multAddExprsAST.
    def visitMultAddExprsAST(self, ctx:MonkeyParser.MultAddExprsASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyParser#multAddFctrAST.
    def visitMultAddFctrAST(self, ctx:MonkeyParser.MultAddFctrASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyParser#elmtMultExprsAST.
    def visitElmtMultExprsAST(self, ctx:MonkeyParser.ElmtMultExprsASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyParser#multDivElmtMultFctrAST.
    def visitMultDivElmtMultFctrAST(self, ctx:MonkeyParser.MultDivElmtMultFctrASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyParser#prmtElmtExprsAST.
    def visitPrmtElmtExprsAST(self, ctx:MonkeyParser.PrmtElmtExprsASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyParser#brckExprsElmtAccsAST.
    def visitBrckExprsElmtAccsAST(self, ctx:MonkeyParser.BrckExprsElmtAccsASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyParser#prthsCllExprsAST.
    def visitPrthsCllExprsAST(self, ctx:MonkeyParser.PrthsCllExprsASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyParser#intPrmtvExprsAST.
    def visitIntPrmtvExprsAST(self, ctx:MonkeyParser.IntPrmtvExprsASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyParser#strnPrmtvExprgAST.
    def visitStrnPrmtvExprgAST(self, ctx:MonkeyParser.StrnPrmtvExprgASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyParser#idPrmtvAST.
    def visitIdPrmtvAST(self, ctx:MonkeyParser.IdPrmtvASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyParser#trPrmtAST.
    def visitTrPrmtAST(self, ctx:MonkeyParser.TrPrmtASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyParser#falsPrmtvExprsAST.
    def visitFalsPrmtvExprsAST(self, ctx:MonkeyParser.FalsPrmtvExprsASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyParser#prthsPrmtvExprsAST.
    def visitPrthsPrmtvExprsAST(self, ctx:MonkeyParser.PrthsPrmtvExprsASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyParser#arryLitPrmtvExprsAST.
    def visitArryLitPrmtvExprsAST(self, ctx:MonkeyParser.ArryLitPrmtvExprsASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyParser#arryFnctnPrmtvExprsAST.
    def visitArryFnctnPrmtvExprsAST(self, ctx:MonkeyParser.ArryFnctnPrmtvExprsASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyParser#fnctnLitPrmtvExprsAST.
    def visitFnctnLitPrmtvExprsAST(self, ctx:MonkeyParser.FnctnLitPrmtvExprsASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyParser#hshLitPrmtvExprsAST.
    def visitHshLitPrmtvExprsAST(self, ctx:MonkeyParser.HshLitPrmtvExprsASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyParser#prntExprsPrmtvExprsAST.
    def visitPrntExprsPrmtvExprsAST(self, ctx:MonkeyParser.PrntExprsPrmtvExprsASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyParser#ifExprsPrmtvExprsAST.
    def visitIfExprsPrmtvExprsAST(self, ctx:MonkeyParser.IfExprsPrmtvExprsASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyParser#arrayFunctions.
    def visitArrayFunctions(self, ctx:MonkeyParser.ArrayFunctionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyParser#brckExprsLstarryLitAST.
    def visitBrckExprsLstarryLitAST(self, ctx:MonkeyParser.BrckExprsLstarryLitASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyParser#fnctnPrmtsBlckStatFnctnLitAST.
    def visitFnctnPrmtsBlckStatFnctnLitAST(self, ctx:MonkeyParser.FnctnPrmtsBlckStatFnctnLitASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyParser#mrIdsFnctnPrmtsAST.
    def visitMrIdsFnctnPrmtsAST(self, ctx:MonkeyParser.MrIdsFnctnPrmtsASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyParser#cmmaIdMrIdsAST.
    def visitCmmaIdMrIdsAST(self, ctx:MonkeyParser.CmmaIdMrIdsASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyParser#hshCtntMrHshCtntHshLitAST.
    def visitHshCtntMrHshCtntHshLitAST(self, ctx:MonkeyParser.HshCtntMrHshCtntHshLitASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyParser#exprsClnExprsHshCtntAST.
    def visitExprsClnExprsHshCtntAST(self, ctx:MonkeyParser.ExprsClnExprsHshCtntASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyParser#cmmaHshCtntMrHshCtntAST.
    def visitCmmaHshCtntMrHshCtntAST(self, ctx:MonkeyParser.CmmaHshCtntMrHshCtntASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyParser#exprsMrExprsExprsLstAST.
    def visitExprsMrExprsExprsLstAST(self, ctx:MonkeyParser.ExprsMrExprsExprsLstASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyParser#emptExprsLstASTAST.
    def visitEmptExprsLstASTAST(self, ctx:MonkeyParser.EmptExprsLstASTASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyParser#cmmaExprsMrExprsAST.
    def visitCmmaExprsMrExprsAST(self, ctx:MonkeyParser.CmmaExprsMrExprsASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyParser#ptsExprsPrntExprsAST.
    def visitPtsExprsPrntExprsAST(self, ctx:MonkeyParser.PtsExprsPrntExprsASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyParser#ifExprsBlckStatElsBlckStatIdExprsAST.
    def visitIfExprsBlckStatElsBlckStatIdExprsAST(self, ctx:MonkeyParser.IfExprsBlckStatElsBlckStatIdExprsASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyParser#stntBlckStatAST.
    def visitStntBlckStatAST(self, ctx:MonkeyParser.StntBlckStatASTContext):
        return self.visitChildren(ctx)



del MonkeyParser