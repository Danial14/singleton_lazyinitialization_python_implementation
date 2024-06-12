class DatabaseDriver():
    __coming_from_outside = True
    __driver = None
    def __init__(self):
        if DatabaseDriver.__coming_from_outside:
            raise Exception("Cannot instantiate directly")
    @staticmethod
    def getInstance():
        if DatabaseDriver.__driver == None:
            DatabaseDriver.__coming_from_outside = False
            DatabaseDriver.__driver = DatabaseDriver()
            DatabaseDriver.__coming_from_outside = True
        return DatabaseDriver.__driver
    