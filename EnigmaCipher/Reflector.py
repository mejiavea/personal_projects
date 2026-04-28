from random import sample

alphabet = [i for i in range(0, 26)]

class Reflector:
    def __init__(self):
        self.__wiring = {}
        sub_alphabet = sample(alphabet, len(alphabet))

        for i in range(0, 26, 2):
            a = sub_alphabet[i]
            b = sub_alphabet[i+1]
            self.__wiring[a] = b
            self.__wiring[b] = a

    def reflect(self, n):
        return self.__wiring[n]
