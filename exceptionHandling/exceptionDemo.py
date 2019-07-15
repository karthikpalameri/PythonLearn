class ExceptionHandlingDemo(object):
    def someMethod(self):
        a = 10
        b = 20
        c = 0
        try:
            x = (a + b) / c
            print(x)
        except:
            print("unable to delete from zero so executing except block")
            raise Exception("Some random exception") #raising execution manually
        else:
            print("else block execute Only if there is no exception")

        finally:
            print("Finally block executes no matter what ")

ExceptionHandlingDemo().someMethod()
