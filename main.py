from databasedriver import DatabaseDriver
d1 = DatabaseDriver.getInstance()
d2 = DatabaseDriver.getInstance()
#the hash code for d1 and d2 objects will be same because of Singleton implementation
print(d1.__hash__() == d2.__hash__())
#DatabaseDriver() will throw an exception if you directly initialize it
d3 = DatabaseDriver()