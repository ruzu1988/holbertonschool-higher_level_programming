#!/usr/bin/python3
"""inicializando el square """


class Square:
    def __init__(self, size):
        self.__size = size

       
        #!/usr/bin/python3
Square = __import__('1-square').Square

my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

try:
    print(my_square.size)
except Exception as e:
    print(e)

try:
    print(my_square.__size)
except Exception as e:
    print(e)
