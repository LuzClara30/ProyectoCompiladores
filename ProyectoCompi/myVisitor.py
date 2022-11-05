from antlr4.tree.Tree import TerminalNodeImpl
from REPL import REPL
from generated.MonkeyParser import MonkeyParser
from generated.MonkeyParserVisitor import MonkeyParserVisitor


class myVisitor(MonkeyParserVisitor):
    mainRepl: REPL = REPL()
    def lista(self, ctx):
        ListReturn = []
        el = self.visit(ctx.expressionList())
        self.visit(el.expression())
        ListReturn.append(self.mainRepl.stackPop())
        l2 = self.visit(el.moreExpressions())
        ListRet = []
        for element in l2.expression():
            self.visit(element)
            ListRet.append(self.mainRepl.stackPop())
        self.mainRepl.stackPush(ListReturn + ListRet)
    def myVisitor(self):
        self.mainRepl = REPL.getInstance()
    # Visit a parse tree produced by MonkeyParser#programAST.
    def visitProgramAST(self, ctx: MonkeyParser.ProgramASTContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MonkeyParser#letStatAST.
    def visitLetStatAST(self, ctx: MonkeyParser.LetStatASTContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MonkeyParser#rtrnStatAST.
    def visitRtrnStatAST(self, ctx: MonkeyParser.RtrnStatASTContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MonkeyParser#exprsStatStatAST.
    def visitExprsStatStatAST(self, ctx: MonkeyParser.ExprsStatStatASTContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MonkeyParser#idEqLetStatAST.
    def visitIdEqLetStatAST(self, ctx: MonkeyParser.IdEqLetStatASTContext):
        try:
            self.visit(ctx.expression())
            self.mainRepl.setData(ctx.ID().getText(), self.mainRepl.stackPop())
        except:
            print("An exception occurred")

        return None

    # Visit a parse tree produced by MonkeyParser#exprsRtrnStatAST.
    def visitExprsRtrnStatAST(self, ctx: MonkeyParser.ExprsRtrnStatASTContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MonkeyParser#exprsExprsStatAST.
    def visitExprsExprsStatAST(self, ctx: MonkeyParser.ExprsExprsStatASTContext):
        try:
            self.visit(ctx.expression())
            val = self.mainRepl.stackPop()
            print(val)

        except:
            raise Exception("Error en la expresión escrita")
        return None
    # Visit a parse tree produced by MonkeyParser#addExprsExprsAST.
    def visitAddExprsExprsAST(self, ctx: MonkeyParser.AddExprsExprsASTContext):
        self.visit(ctx.additionExpression())
        self.visit(ctx.comparison())
        return None

    # Visit a parse tree produced by MonkeyParser#eqlsComparsAST.
    def visitEqlsComparsAST(self, ctx: MonkeyParser.EqlsComparsASTContext):
        if ctx.children is not None:
            i = 0
            y = len(ctx.children)
            while i < len(ctx.children):
                comp = ctx.children[0]
                self.visit(ctx.children[i + 1])
                op2 = self.mainRepl.stackPop()
                op1 = self.mainRepl.stackPop()
                if TerminalNodeImpl(comp).getSymbol().symbol.type == MonkeyParser.GREATERTHAN and (
                        (isinstance(op1, int) and isinstance(op2, int)) or
                        (isinstance(op1, str) and isinstance(op2, str)) or
                        (isinstance(op1, list) and isinstance(op2, list))):
                    if (op1 > op2):
                        self.mainRepl.stackPush("True")
                    else:
                        self.mainRepl.stackPush("False");
                elif TerminalNodeImpl(comp).getSymbol().symbol.type == MonkeyParser.LOWERTHAN and (
                        (isinstance(op1, int) and isinstance(op2, int)) or
                        (isinstance(op1, str) and isinstance(op2, str)) or
                        (isinstance(op1, list) and isinstance(op2, list))):
                    if (op1 < op2):
                        self.mainRepl.stackPush("True")
                    else:
                        self.mainRepl.stackPush("False");
                elif TerminalNodeImpl(comp).getSymbol().symbol.type == MonkeyParser.EQUALE and (
                        (isinstance(op1, int) and isinstance(op2, int)) or
                        (isinstance(op1, str) and isinstance(op2, str)) or
                        (isinstance(op1, list) and isinstance(op2, list))):
                    if (op1 == op2):
                        self.mainRepl.stackPush("True")
                    else:
                        self.mainRepl.stackPush("False");
                elif TerminalNodeImpl(comp).getSymbol().symbol.type == MonkeyParser.GTE and (
                        (isinstance(op1, int) and isinstance(op2, int)) or
                        (isinstance(op1, str) and isinstance(op2, str)) or
                        (isinstance(op1, list) and isinstance(op2, list))):
                    if (op1 >= op2):
                        self.mainRepl.stackPush("True")
                    else:
                        self.mainRepl.stackPush("False");
                elif TerminalNodeImpl(comp).getSymbol().symbol.type == MonkeyParser.LTE and (
                        (isinstance(op1, int) and isinstance(op2, int)) or
                        (isinstance(op1, str) and isinstance(op2, str)) or
                        (isinstance(op1, list) and isinstance(op2, list))):
                    if (op1 <= op2):
                        self.mainRepl.stackPush("True")
                    else:
                        self.mainRepl.stackPush("False");
                else:
                    raise Exception(
                        "Type error between " + op1.getClass().getSimpleName() + " and " + op2.getClass().getSimpleName() + " in expression")
                i = i + 2
        return None

    # Visit a parse tree produced by MonkeyParser#multAddExprsAST.
    def visitMultAddExprsAST(self, ctx: MonkeyParser.MultAddExprsASTContext):
        self.visit(ctx.multiplicationExpression())
        self.visit(ctx.additionFactor())
        return None

    # Visit a parse tree produced by MonkeyParser#multAddFctrAST.
    def visitMultAddFctrAST(self, ctx: MonkeyParser.MultAddFctrASTContext):
        if ctx.children is not None:
            i = 0
            y = len(ctx.children)
            while i < len(ctx.children):
                oper = ctx.children[0]
                self.visit(ctx.children[i + 1])
                op2 = self.mainRepl.stackPop()
                op1 = self.mainRepl.stackPop()
                if TerminalNodeImpl(oper).getSymbol().symbol.type == MonkeyParser.ADD and isinstance(op1,
                                                                                                     int) and isinstance(
                        op2, int):
                    self.mainRepl.stackPush(int(op1) + int(op2))
                elif TerminalNodeImpl(oper).getSymbol().symbol.type == MonkeyParser.ADD and isinstance(op1,
                                                                                                       str) and isinstance(
                        op2, str):
                    self.mainRepl.stackPush(str(op1)[1:-1] + str(op2)[1:-1])
                elif TerminalNodeImpl(oper).getSymbol().symbol.type == MonkeyParser.ADD and isinstance(op1,
                                                                                                       list) and isinstance(
                        op2, list):
                    self.mainRepl.stackPush(list(op1) + list(op2))
                elif TerminalNodeImpl(oper).getSymbol().symbol.type == MonkeyParser.SUB and isinstance(op1,
                                                                                                       int) and isinstance(
                        op2, int):
                    self.mainRepl.stackPush(int(op1) - int(op2))
                else:
                    raise Exception(
                        "Type error between " + op1.getClass().getSimpleName() + " and " + op2.getClass().getSimpleName() + " in expression")
                i = i + 2
        return None

    # Visit a parse tree produced by MonkeyParser#elmtMultExprsAST.
    def visitElmtMultExprsAST(self, ctx: MonkeyParser.ElmtMultExprsASTContext):
        self.visit(ctx.elementExpression())
        self.visit(ctx.multiplicationFactor())
        return None

    # Visit a parse tree produced by MonkeyParser#multDivElmtMultFctrAST.
    def visitMultDivElmtMultFctrAST(self, ctx: MonkeyParser.MultDivElmtMultFctrASTContext):
        if ctx.children is not None:
            i = 0
            y = len(ctx.children)
            while i < len(ctx.children):
                oper = ctx.children[0]
                self.visit(ctx.children[i + 1])
                op2 = self.mainRepl.stackPop()
                op1 = self.mainRepl.stackPop()
                if TerminalNodeImpl(oper).getSymbol().symbol.type == MonkeyParser.DIV and isinstance(op1,
                                                                                                     int) and isinstance(
                        op2, int):
                    self.mainRepl.stackPush(int(int(op1) / int(op2)))
                elif TerminalNodeImpl(oper).getSymbol().symbol.type == MonkeyParser.MULT and isinstance(op1,
                                                                                                        int) and isinstance(
                        op2, int):
                    self.mainRepl.stackPush(int(op1) * int(op2))
                else:
                    raise Exception(
                        "Type error between " + op1.getClass().getSimpleName() + " and " + op2.getClass().getSimpleName() + " in expression")
                i = i + 2
        return None
    # Visit a parse tree produced by MonkeyParser#prmtElmtExprsAST.
    def visitPrmtElmtExprsAST(self, ctx: MonkeyParser.PrmtElmtExprsASTContext):
        l = self.visit(ctx.primitiveExpression())
        if ctx.elementAccess():
            self.visit(ctx.elementAccess())
        elif ctx.callExpression():
            ctxname = ctx.getChild(0).__class__.__name__
            if ctxname == 'IdPrmtvASTContext':
                self.visit(ctx.getChild(1))
                self.lista(ctx.getChild(1))
                parametros = self.mainRepl.stackPop()
                print(parametros)

            if l.arrayFunctions() is not None:
                if self.visit(l.arrayFunctions()) == 1:
                    listLen = []
                    l1 = self.visit(ctx.callExpression())
                    l2 = self.visit(l1.expressionList())
                    self.visit(l2.expression())
                    listLen.append(len(self.mainRepl.stackPop()))
                    l3 = self.visit(l2.moreExpressions())
                    listLen2 = []
                    for element in l3.expression():
                        self.visit(element)
                        listLen2.append(len(self.mainRepl.stackPop()))
                    self.mainRepl.stackPush(listLen + listLen2)
                if self.visit(l.arrayFunctions()) == 5:
                    a = self.visit(ctx.callExpression())
                    b = self.visit(a.expressionList())
                    self.visit(b.expression())
                    listLen = self.mainRepl.stackPop()
                    c = self.visit(b.moreExpressions())
                    listLen2 = []
                    for element in c.expression():
                        self.visit(element)
                        listLen2.append(self.mainRepl.stackPop())
                    self.mainRepl.stackPush(listLen + listLen2)


        return None

    # Visit a parse tree produced by MonkeyParser#brckExprsElmtAccsAST.
    def visitBrckExprsElmtAccsAST(self, ctx: MonkeyParser.BrckExprsElmtAccsASTContext):
        x = self.mainRepl.stackPop()
        if type(x) is list:
            self.visit(ctx.expression())
            self.mainRepl.stackPush(x[self.mainRepl.stackPop()])
        elif type(x) is dict:
            self.visit(ctx.expression())
            self.mainRepl.stackPush(x[self.mainRepl.stackPop()])
        return None

    # Visit a parse tree produced by MonkeyParser#prthsCllExprsAST.
    def visitPrthsCllExprsAST(self, ctx: MonkeyParser.PrthsCllExprsASTContext):
        return ctx

    # Visit a parse tree produced by MonkeyParser#intPrmtvExprsAST.
    def visitIntPrmtvExprsAST(self, ctx: MonkeyParser.IntPrmtvExprsASTContext):
        self.mainRepl.stackPush(int(ctx.INT().getText()))
        return None

    # Visit a parse tree produced by MonkeyParser#strnPrmtvExprgAST.
    def visitStrnPrmtvExprgAST(self, ctx: MonkeyParser.StrnPrmtvExprgASTContext):
        self.mainRepl.stackPush(str(ctx.STRING().getText()))
        return None

    # Visit a parse tree produced by MonkeyParser#idPrmtvAST.
    def visitIdPrmtvAST(self, ctx: MonkeyParser.IdPrmtvASTContext):
        value = self.mainRepl.getData(ctx.ID().getText())
        if value is not None:
            self.mainRepl.stackPush(value)
        else:
            raise Exception("Undefined indentifier:" + ctx.ID().getText())
        return None

    # Visit a parse tree produced by MonkeyParser#trPrmtAST.
    def visitTrPrmtAST(self, ctx: MonkeyParser.TrPrmtASTContext):
        self.mainRepl.stackPush(True)
        return None

    # Visit a parse tree produced by MonkeyParser#falsPrmtvExprsAST.
    def visitFalsPrmtvExprsAST(self, ctx: MonkeyParser.FalsPrmtvExprsASTContext):
        self.mainRepl.stackPush(False)
        return None

    # Visit a parse tree produced by MonkeyParser#prthsPrmtvExprsAST.
    def visitPrthsPrmtvExprsAST(self, ctx: MonkeyParser.PrthsPrmtvExprsASTContext):
        self.visit(ctx.expression())
        return None

    # Visit a parse tree produced by MonkeyParser#arryLitPrmtvExprsAST.
    def visitArryLitPrmtvExprsAST(self, ctx: MonkeyParser.ArryLitPrmtvExprsASTContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MonkeyParser#arryFnctnPrmtvExprsAST.
    def visitArryFnctnPrmtvExprsAST(self, ctx: MonkeyParser.ArryFnctnPrmtvExprsASTContext):
        if len(ctx.parentCtx.children) > 1:
            return ctx
        else:
            que = self.visit(ctx.arrayFunctions())
            le = self.visit(ctx.expressionList())
            self.visit(le.expression())
            if que == 1:
                self.mainRepl.stackPush(len(self.mainRepl.stackPop()))
            elif que == 2:
                self.mainRepl.stackPush((self.mainRepl.stackPop())[0])
            elif que == 3:
                self.mainRepl.stackPush((self.mainRepl.stackPop())[-1])
            elif que == 4:
                list = self.mainRepl.stackPop()
                list.pop(0)
                self.mainRepl.stackPush(list)
            else:
                raise Exception("la función no corresponde a las funciones de listas")

    # Visit a parse tree produced by MonkeyParser#fnctnLitPrmtvExprsAST.
    def visitFnctnLitPrmtvExprsAST(self, ctx: MonkeyParser.FnctnLitPrmtvExprsASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyParser#hshLitPrmtvExprsAST.
    def visitHshLitPrmtvExprsAST(self, ctx: MonkeyParser.HshLitPrmtvExprsASTContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MonkeyParser#prntExprsPrmtvExprsAST.
    def visitPrntExprsPrmtvExprsAST(self, ctx: MonkeyParser.PrntExprsPrmtvExprsASTContext):

        return self.visitChildren(ctx)

    # Visit a parse tree produced by MonkeyParser#ifExprsPrmtvExprsAST.
    def visitIfExprsPrmtvExprsAST(self, ctx: MonkeyParser.IfExprsPrmtvExprsASTContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MonkeyParser#arrayFunctions.
    def visitArrayFunctions(self, ctx: MonkeyParser.ArrayFunctionsContext):
        if ctx.LEN() is not None:
            return 1
        elif ctx.FIRST() is not None:
            return 2
        elif ctx.LAST() is not None:
            return 3
        elif ctx.REST() is not None:
            return 4
        elif ctx.PUSH() is not None:
            return 5
        else:
            raise Exception("Error in ArrayFunction")

    # Visit a parse tree produced by MonkeyParser#brckExprsLstarryLitAST.
    def visitBrckExprsLstarryLitAST(self, ctx: MonkeyParser.BrckExprsLstarryLitASTContext):
        self.lista(ctx)
        return None
    # Visit a parse tree produced by MonkeyParser#fnctnPrmtsBlckStatFnctnLitAST.
    def visitFnctnPrmtsBlckStatFnctnLitAST(self, ctx: MonkeyParser.FnctnPrmtsBlckStatFnctnLitASTContext):
        self.mainRepl.stackPush(ctx)
        return None
    # Visit a parse tree produced by MonkeyParser#mrIdsFnctnPrmtsAST.
    def visitMrIdsFnctnPrmtsAST(self, ctx: MonkeyParser.MrIdsFnctnPrmtsASTContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MonkeyParser#cmmaIdMrIdsAST.
    def visitCmmaIdMrIdsAST(self, ctx: MonkeyParser.CmmaIdMrIdsASTContext):

        return self.visitChildren(ctx)

    # Visit a parse tree produced by MonkeyParser#hshCtntMrHshCtntHshLitAST.
    def visitHshCtntMrHshCtntHshLitAST(self, ctx: MonkeyParser.HshCtntMrHshCtntHshLitASTContext):
        diccionario = self.visit(ctx.hashContent())
        if ctx.moreHashContent() is not None:
            diccionario1 = self.visit(ctx.moreHashContent())
            diccionario.update(diccionario1)
            self.mainRepl.stackPush(diccionario)
        else:
            self.mainRepl.stackPush(diccionario)
        return None

    # Visit a parse tree produced by MonkeyParser#exprsClnExprsHshCtntAST.
    def visitExprsClnExprsHshCtntAST(self, ctx: MonkeyParser.ExprsClnExprsHshCtntASTContext):
        d3 = {}
        cont = 0
        for element in ctx.expression():
            self.visit(element)
            if cont == 0:
                Clave = self.mainRepl.stackPop()
            else:
                Value = self.mainRepl.stackPop()
            cont = cont + 1
        d3[Clave] = Value

        return d3

    # Visit a parse tree produced by MonkeyParser#cmmaHshCtntMrHshCtntAST.
    def visitCmmaHshCtntMrHshCtntAST(self, ctx: MonkeyParser.CmmaHshCtntMrHshCtntASTContext):
        diccionario = {}
        for element in ctx.hashContent():
            l = self.visit(element)
            diccionario.update(l)
        return diccionario

    # Visit a parse tree produced by MonkeyParser#exprsMrExprsExprsLstAST.
    def visitExprsMrExprsExprsLstAST(self, ctx: MonkeyParser.ExprsMrExprsExprsLstASTContext):

        return ctx

    # Visit a parse tree produced by MonkeyParser#emptExprsLstASTAST.
    def visitEmptExprsLstASTAST(self, ctx: MonkeyParser.EmptExprsLstASTASTContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MonkeyParser#cmmaExprsMrExprsAST.
    def visitCmmaExprsMrExprsAST(self, ctx: MonkeyParser.CmmaExprsMrExprsASTContext):
        return ctx

    # Visit a parse tree produced by MonkeyParser#ptsExprsPrntExprsAST.
    def visitPtsExprsPrntExprsAST(self, ctx: MonkeyParser.PtsExprsPrntExprsASTContext):
        try:
            self.visit(ctx.expression())

        except:
            raise Exception("Error en la impresión")

        return None

    # Visit a parse tree produced by MonkeyParser#ifExprsBlckStatElsBlckStatIdExprsAST.
    def visitIfExprsBlckStatElsBlckStatIdExprsAST(self, ctx: MonkeyParser.IfExprsBlckStatElsBlckStatIdExprsASTContext):
        self.visit(ctx.expression())
        result = self.mainRepl.stackPop()
        if result == "True":
            self.visit(ctx.blockStatement(0))
        if result == "False":
            self.visit(ctx.blockStatement(1))
            self.visit(ctx.children[1])
        else:
            self.visit(ctx.children[1])
            return None
        return None

    # Visit a parse tree produced by MonkeyParser#stntBlckStatAST.
    def visitStntBlckStatAST(self, ctx: MonkeyParser.StntBlckStatASTContext):
        return self.visitChildren(ctx)
