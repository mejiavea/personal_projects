alphabet = [i for i in range(0, 26)]

class Rotor:
    def __init__(self, position=0, rotor_type="I"):
        self.__possible_wires = {
            "I": [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9],
            "II": [0, 9, 3, 10, 18, 8, 17, 20, 23, 1, 11, 7, 22, 19, 12, 2, 16, 6, 25, 13, 15, 24, 5, 21, 14, 4],
            "III": [1, 3, 5, 7, 9, 11, 2, 15, 17, 19, 23, 21, 25, 13, 24, 4, 8, 22, 6, 0, 10, 12, 20, 18, 16, 14]
        }
        self.__possible_notches = {"I": 16, "II": 4, "III": 21}
        self.__wires = self.__possible_wires[rotor_type]
        self.__position = position
        self.__notch = self.__possible_notches[rotor_type]

        self.__inverse_wires = [0] * 26
        for i, v in enumerate(self.__wires):
            self.__inverse_wires[v] = i

    def setRotor(self, rotor_type):
        self.__wires = self.__possible_wires[rotor_type]
        self.__inverse_wires = [0] * 26
        for i, v in enumerate(self.__wires):
            self.__inverse_wires[v] = i
        self.__notch = self.__possible_notches[rotor_type]

    # getter methods for position and notch
    def getNotch(self):
        return self.__notch
    def getPosition(self):
        return self.__position

    # setter method for position, user-changeable
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
