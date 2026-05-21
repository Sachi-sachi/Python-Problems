class AccessSpecifiers:

    def public_method(self):
        print("Public method- can be accesed anywher")

    def _protected_method(self):
        print("Protected method-only accessed within class or subclass")

    def __private_method(self):
        print("Private method- accessible only in that class")

    def accesswithinclass(self):
        print("Hello:")
        self.public_method()       # should work
        self._protected_method()   # should work
        self.__private_method()    # should work


class ChildofAccess(AccessSpecifiers):

    def withinchild(self):
        print("Hello 2:")
        self.public_method()       #  works
        self._protected_method()   #  works

        # self.__private_method()  #  not working

        self._AccessSpecifiers__private_method() #  work s( name mangling)

obj = AccessSpecifiers()

print("Outside parent class:")

#  works
obj.public_method()

#  still works tho??
obj._protected_method()

#  error
# obj.__private_method()

#  works (name mangling)
obj._AccessSpecifiers__private_method()


#  ? works
obj.accesswithinclass()


#  Subclass
child = ChildofAccess()
child.withinchild()
child.accesswithinclass()
