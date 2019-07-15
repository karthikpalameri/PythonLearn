class writeThisMessage(object):
    def __init__(self, fileName):
        self.fileName = fileName

    def __enter__(self):
        self.refVar = open(self.fileName,"w")
        return self.refVar

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.refVar.close()


with writeThisMessage("writeToFile.txt") as ref:
    ref.write("hello world")
