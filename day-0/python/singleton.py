class Singleton:
    __instance = None

    @staticmethod
    def getInstance():
        # Static access method.
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        if Singleton.__instance != None:
            raise Exception("This class is a Singleton!")
        else:
            Singleton.__instance = self


s = Singleton()
print(s)

# This will raise an Error
# s2 = Singleton()
# print(s2)

s2 = Singleton.getInstance()
print(s2)
