import HashMap


class REPL:
    instance = None

    @staticmethod
    def getInstance():
        if REPL.instance is None:
            REPL()
        return REPL.instance

    def __init__(self):
        if REPL.instance is not None:
            raise Exception("Ya existe")

        else:
            self.data = HashMap.HashMap()
            self.stack = []
            self.arrayData = [self.data]
            REPL.instance = self

    def getData(self, var):
        return self.data.getData(var)

    def setData(self, key, value):
        self.data.setData(key, value)

    def stackPush(self, value):
        self.stack.append(value)

    def stackPop(self):
        return self.stack.pop()

    def returnStack(self):
        return self.stack

    def addArrayData(self):
        self.arrayData.append(HashMap.HashMap())

    def getArrayData(self, num):
        self.arrayData.pop(num)

    def searchData(self, variable):
        for item in reversed(self.arrayData):
            try:
                valor = item.getData(variable)
                return valor
            except:
                print("")
