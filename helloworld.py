class HelloWorld:
    def __init__(self):
        self.str_const = "Hellloooo"
        print("Hello World from HelloWorld class")

    def __str__(self):
        # print("my object helloworld")
        return self.str_const


obj1 = HelloWorld()
print(obj1)
