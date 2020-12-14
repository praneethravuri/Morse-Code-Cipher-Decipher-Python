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