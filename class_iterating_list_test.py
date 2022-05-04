class Test:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

obj1 = Test("object 1 arg1", "object 1 arg2")
obj2 = Test("object 2 arg1", "object 2 arg2")

objects = [obj1, obj2]

for i in objects:
    print(i.arg1)
