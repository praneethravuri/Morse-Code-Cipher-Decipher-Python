"""
Website - https://morsecode.world/international/translator.html
"""
import string


class MorseCode:
    def __init__(self, message):
        self.morse_code_dict = None
        self.message = message

    def morse_code(self):
        # List of letter and their corresponding morse code
        # If you are using another dictionary, inset this at the end of the dictionary --->   "":""
        morse_code_dict = {'A': '.-', 'B': '-...',
                           'C': '-.-.', 'D': '-..', 'E': '.',
                           'F': '..-.', 'G': '--.', 'H': '....',
                           'I': '..', 'J': '.---', 'K': '-.-',
                           'L': '.-..', 'M': '--', 'N': '-.',
                           'O': '---', 'P': '.--.', 'Q': '--.-',
                           'R': '.-.', 'S': '...', 'T': '-',
                           'U': '..-', 'V': '...-', 'W': '.--',
                           'X': '-..-', 'Y': '-.--', 'Z': '--..',
                           '1': '.----', '2': '..---', '3': '...--',
                           '4': '....-', '5': '.....', '6': '-....',
                           '7': '--...', '8': '---..', '9': '----.',
                           '0': '-----', ',': '--..--', '.': '.-.-.-',
                           '?': '..--..', '/': '-..-.', '-': '-....-',
                           '(': '-.--.', ')': '-.--.-', "": "", " ": " / "}
        self.morse_code_dict = morse_code_dict

    def morse_code_cipher(self):
        try:
            # Message to be converted into morse code
            cipher = ""
            for letter in message:
                cipher += self.morse_code_dict[letter] + " "
            return cipher
        except KeyError:
            return "One of the characters in the input is not recognized in morse code. Please try again."
        except ValueError:
            return "One of the characters in the input is not recognized in morse code. Please try again."

    def morse_code_decipher(self):
        try:
            # Split all the words and spaces in the morse code
            word_list = []
            for word in message.split(" / "):
                word_list.append(word)

            # Separate spaces and add them separately in the word_list
            space = 1
            for _ in range(0, len(word_list)):
                word_list.insert(space, " / ")
                space += 2

            # Split the words into individual letters

            letter_list = []
            for word in word_list:
                for letter in word.split(" "):
                    letter_list.append(letter)

            # Get the letters from their corresponding morse code
            keys = list(self.morse_code_dict.keys())
            values = list(self.morse_code_dict.values())

            # Morse code to normal message
            decipher_string = ""

            # Replace the morse code to corresponding letter
            for letter in letter_list:
                if letter == "/":
                    decipher_string += " "
                else:
                    decipher_string += keys[values.index(letter)]

            return decipher_string
        except KeyError:
            return "One of the characters in the morse code is not recognized. Please try again"
        except ValueError:
            return "One of the characters in the morse code is not recognized. Please try again"


print("\n")
message = input("Enter the message to be generated in morse code or decipher a morse code: ").upper()
punctuation = string.punctuation
my_morse_code = MorseCode(message)
my_morse_code.morse_code()
for i in message:
    if i in punctuation:
        print(my_morse_code.morse_code_decipher())
        break
    else:
        print(my_morse_code.morse_code_cipher())
        break
