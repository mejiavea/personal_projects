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
    old_positions = [machine.rotors[0].getPosition(), machine.rotors[1].getPosition(), machine.rotors[2].getPosition()]
    print("Machine initialized\n")

    plugboard_settings = input("Enter pairs of letters in format abcd (or just hit enter) > ")
    plaintext = input("enter plaintext (must be lowercase string with no spaces or special characters) > ")

    print("Encrypting...")
    if plugboard_settings != "":
        machine.plugboard.setWiring(plugboard_settings)
    ciphertext = []
    plaintext = convert(plaintext)
    for n in plaintext:
        ciphertext.append(machine.encrypt(n))
    ciphertext = revert(ciphertext)
    print(f"Ciphertext: {ciphertext}\n")

    for i in range(3):
        machine.rotors[i].setPosition(old_positions[i])

    plugboard_settings = input("enter more pluboard pairs (or enter) > ")
    plaintext = input("enter another plaintext > ")
    print(f"Encrypting...")
    ciphertext = []
    plaintext = convert(plaintext)
    for n in plaintext:
        ciphertext.append(machine.encrypt(n))
    ciphertext = revert(ciphertext)
    print(f"Ciphertext: {ciphertext}")

