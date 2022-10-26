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
            REPL.instance = self

    def getData(self, var):
        return self.data.get(var)

    def setData(self, key, value):
        self.data.put(key, value)

    def stackPush(self, value):
        self.stack.append(value)

    def stackPop(self):
        return self.stack.pop()

    def returnStack(self):
        return self.stack

