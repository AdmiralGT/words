import argparse

letter_values = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
    "I": 9,
    "J": 10,
    "K": 11,
    "L": 12,
    "M": 13,
    "N": 14,
    "O": 15,
    "P": 16,
    "Q": 17,
    "R": 18,
    "S": 19,
    "T": 20,
    "U": 21,
    "V": 22,
    "W": 23,
    "X": 24,
    "Y": 25,
    "Z": 26
}

def is_prime(number):
    if number < 2:
        return True
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def main(word):
    sum = 0
    for char in list(word):
        sum += letter_values[char]
    if is_prime(sum):
        print(f"Total value of word: {sum} (prime)")
    else:
        print(f"Total value of word: {sum}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate the value of a word")
    parser.add_argument("word", help="The word to calculate the value of")
    args = parser.parse_args()
    main(args.word.upper())

