from Machine import Machine

def convert(plaintext):
    converted = []
    for i in plaintext:
        converted.append(ord(i) - ord("a"))
    return converted

def revert(ciphertext):
    converted = ""
    for i in ciphertext:
        converted = converted + (chr(i + ord("a")))
    return converted

if __name__ == "__main__":
    print("Initializing machine...")
    machine = Machine()
    print("Machine initialized\n")

    rotors = input("Set machine rotors in format rotor_type;position, rotor_type;position, rotor_type;position > ")
    rotors = rotors.split(", ")
    for i in range(len(rotors)):
        rotor_settings = rotors[i].split(";")
        machine.rotors[i].setRotor(rotor_settings[0])
        machine.rotors[i].setPosition(int(rotor_settings[1]))

    plugboard_settings = input("\nEnter pairs of letters in format abcd (or just hit enter) > ")
    plaintext = input("\nEnter plaintext (must be lowercase string with no spaces or special characters) > ")

    print("\nEncrypting...")
    if plugboard_settings != "":
        machine.plugboard.setWiring(convert(plugboard_settings))
    ciphertext = []
    plaintext = convert(plaintext)
    for n in plaintext:
        ciphertext.append(machine.encrypt(n))
    ciphertext = revert(ciphertext)
    print(f"Ciphertext: {ciphertext}\n")
