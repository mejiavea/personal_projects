from random import randint, sample

alphabet = [i for i in range(0, 26)]

class Rotor:
    def __init__(self, position=0):
        self.__wires = sample(alphabet, len(alphabet))
        self.__position = position
        self.__notch = randint(0, 25)

        self.__inverse_wires = [0] * 26
        for i, v in enumerate(self.__wires):
            self.__inverse_wires[v] = i

    # getter methods for debugging purposes, actual implementation should remove the methods to ensure security
    def getWires(self):
        return self.__wires
    def getNotch(self):
        return self.__notch

    # getter methods for position, user-changeable
    def getPosition(self):
        return self.__position
    def setPosition(self, position):
        self.__position = position % 26
        return

    def forward(self, n):
        shifted_n = (n + self.__position) % 26
        wired = self.__wires[shifted_n]
        return (wired - self.__position) % 26

    def reverse(self, n):
        shifted_n = (n + self.__position) % 26
        wired = self.__inverse_wires[shifted_n]
        return (wired - self.__position) % 26

    def step(self):
        self.__position = (self.__position + 1) % 26
        return self.__position == self.__notch

