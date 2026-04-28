from Plugboard import Plugboard
from Rotor import Rotor
from Reflector import Reflector

class Machine:
    def __init__(self):
        self.plugboard = Plugboard()
        self.rotors = [Rotor(), Rotor(), Rotor()]
        self.reflector = Reflector()

    def step_rotors(self):
        if self.rotors[2].getPosition() == self.rotors[0].getNotch():
            step_next = self.rotors[1].step()
            if step_next:
                self.rotors[0].step()
        self.rotors[2].step()

    def encrypt(self, n):
        n = self.plugboard.swap(n)
        self.step_rotors()

        for rotor in reversed(self.rotors):
            n = rotor.forward(n)
        n = self.reflector.reflect(n)
        for rotor in self.rotors:
            n = rotor.reverse(n)

        n = self.plugboard.swap(n)
        return n
