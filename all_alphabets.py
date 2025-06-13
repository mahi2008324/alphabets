# Full Python code to print A to Z letter patterns using functions

def print_A():
    for row in range(7):
        for col in range(7):
            if ((col == 0 or col == 6) and row != 0) or ((row == 0 or row == 3) and 0 < col < 6):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def print_B():
    for row in range(7):
        for col in range(7):
            if col == 0 or ((row == 0 or row == 3 or row == 6) and col < 6) or (col == 6 and row not in (0, 3, 6)):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def print_C():
    for row in range(7):
        for col in range(7):
            if col == 0 and row not in (0, 6) or row in (0, 6) and col > 0:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def print_D():
    for row in range(7):
        for col in range(7):
            if col == 0 or (col == 6 and row not in (0, 6)) or (row in (0, 6) and col < 6):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def print_E():
    for row in range(7):
        for col in range(7):
            if col == 0 or row in (0, 3, 6):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def print_F():
    for row in range(7):
        for col in range(7):
            if col == 0 or row in (0, 3):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def print_G():
    for row in range(7):
        for col in range(7):
            if col == 0 and row not in (0, 6) or row in (0, 6) and col > 0 or (row == 3 and col > 2) or (col == 6 and row > 3):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def print_H():
    for row in range(7):
        for col in range(7):
            if col in (0, 6) or row == 3:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def print_I():
    for row in range(7):
        for col in range(7):
            if row in (0, 6) or col == 3:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def print_J():
    for row in range(7):
        for col in range(7):
            if row == 0 or col == 3 or (row == 6 and col < 4) or (col == 0 and row > 3):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def print_K():
    for row in range(7):
        for col in range(7):
            if col == 0 or row + col == 6 or row - col == 0:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def print_L():
    for row in range(7):
        for col in range(7):
            if col == 0 or row == 6:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def print_M():
    for row in range(7):
        for col in range(7):
            if col == 0 or col == 6 or (row == col and col < 4) or (row + col == 6 and col > 2):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def print_N():
    for row in range(7):
        for col in range(7):
            if col == 0 or col == 6 or row == col:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def print_O():
    for row in range(7):
        for col in range(7):
            if ((col == 0 or col == 6) and row not in (0, 6)) or ((row == 0 or row == 6) and 0 < col < 6):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def print_P():
    for row in range(7):
        for col in range(7):
            if col == 0 or (row in (0, 3) and col < 6) or (col == 6 and row in (1, 2)):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def print_Q():
    for row in range(7):
        for col in range(7):
            if ((col == 0 or col == 6) and row not in (0, 6)) or ((row == 0 or row == 6) and 0 < col < 6) or (row == col and row > 3):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def print_R():
    for row in range(7):
        for col in range(7):
            if col == 0 or (row == 0 and col < 6) or (row == 3 and col < 6) or (col == 6 and row in (1, 2)) or (row - col == 2 and row > 3):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def print_S():
    for row in range(7):
        for col in range(7):
            if (row in (0, 3, 6)) or (col == 0 and row in (1, 2)) or (col == 6 and row in (4, 5)):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def print_T():
    for row in range(7):
        for col in range(7):
            if row == 0 or col == 3:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def print_U():
    for row in range(7):
        for col in range(7):
            if (col == 0 or col == 6) and row < 6 or row == 6 and 0 < col < 6:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def print_V():
    for row in range(7):
        for col in range(7):
            if (col == row and row < 4) or (row + col == 6 and row < 4) or (row >= 4 and col == 3):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def print_W():
    for row in range(7):
        for col in range(7):
            if col in (0, 6) or (row == col and row > 2) or (row + col == 6 and row > 2):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def print_X():
    for row in range(7):
        for col in range(7):
            if row == col or row + col == 6:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def print_Y():
    for row in range(7):
        for col in range(7):
            if (row == col and row < 4) or (row + col == 6 and row < 4) or (col == 3 and row >= 4):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def print_Z():
    for row in range(7):
        for col in range(7):
            if row == 0 or row == 6 or row + col == 6:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

# Dictionary mapping each letter to its corresponding function
letter_functions = {
    'A': print_A, 'B': print_B, 'C': print_C, 'D': print_D, 'E': print_E,
    'F': print_F, 'G': print_G, 'H': print_H, 'I': print_I, 'J': print_J,
    'K': print_K, 'L': print_L, 'M': print_M, 'N': print_N, 'O': print_O,
    'P': print_P, 'Q': print_Q, 'R': print_R, 'S': print_S, 'T': print_T,
    'U': print_U, 'V': print_V, 'W': print_W, 'X': print_X, 'Y': print_Y,
    'Z': print_Z
}

def main():
    for letter in range(ord('A'), ord('Z') + 1):
        print("\nPattern for {}:\n".format(chr(letter)))
        letter_functions[chr(letter)]()

main()

