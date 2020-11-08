class MySingleton(object):
    __instance = None

    def __new__(self):
        if not self.__instance:
            self.__instance = super(MySingleton, self).__new__(self)
            self.y = 100
        return self.__instance


x = MySingleton()
print(x.y)
x.y = 101
y = MySingleton()
print(y.y)

print(x, y)
