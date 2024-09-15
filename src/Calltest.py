class Person:
    def __call__(self, name):
        print("__call__"+"Hell "+name)

    def hello(self, name):
        print("Hello"+name)

person = Person()
person("tsai")
person.hello("han")