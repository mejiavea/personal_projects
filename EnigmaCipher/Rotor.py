from random import randint, sample

alphabet = [i for i in range(0, 26)]

class Rotor:
    def __init__(self, position=0):
        self.__wires = sample(alphabet, len(alphabet))
        self.__position = position
        self.__notch = randint(0, 25)

    # getter methods for debugging purposes, actual implementation should remove the methods to ensure security
    def getWires(self):
        return self.__wires
    def getNotch(self):
        return self.__notch

    # getter methods for position, user-changeable
    def getPosition(self):
        return self.__position
    def setPosition(self, position):
        self.__position = position
        return
