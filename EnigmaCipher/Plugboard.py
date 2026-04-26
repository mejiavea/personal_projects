alphabet = "abcdefghijklmnopqrstuvwxyz"

class Plugboard:
    def __init__(self):
        self.__wiring = {}
        for i in alphabet:
            self.__wiring[i] = i

    # getter to display current wiring
    def getWiring(self):
        return self.__wiring

    # setter for user to input pairs of letters they wish to swap on the plugboard
    def setWiring(self, pairs):
        self.resetWiring()
        if len(pairs) % 2 != 0:
            print("Error: Invalid pairs")
            return
        for i in range(0, len(pairs), 2):
            a, b = pairs[i], pairs[i+1]
            if self.__wiring[a] != a or self.__wiring[b] != b:
                print(f"Error: {a} or {b} already paired")
                return
            self.__wiring[a] = b
            self.__wiring[b] = a

    # resets plugboard to normal alphabetic mapping
    def resetWiring(self):
        self.__wiring = {}
        for i in alphabet:
            self.__wiring[i] = i
