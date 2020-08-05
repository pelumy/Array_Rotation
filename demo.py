def isum (a, b):
    isum_result  = a + b
    return isum_result 

print(isum(5,10))

# creating class
class DemoClass:
    def __init__(self, name):
        self.name = name
    
    def getName(self):
        print(f'The name is {self.name}')

the_name = DemoClass('Itunu')
print(the_name.getName())

