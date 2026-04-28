alphabet = [i for i in range(0, 26)]

class Reflector:
    def __init__(self):
        self.__wiring = {}
        sub_alphabet = [24, 17, 20, 7, 16, 18, 11, 3, 15, 23, 13, 6, 14, 10, 12, 8, 4, 1, 5, 25, 2, 22, 21, 9, 0, 19]

        for i in range(0, 26, 2):
            a = sub_alphabet[i]
            b = sub_alphabet[i+1]
            self.__wiring[a] = b
            self.__wiring[b] = a

    def reflect(self, n):
        return self.__wiring[n]
