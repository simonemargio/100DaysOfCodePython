#  Created by Simone Margio
#  www.simonemargio.im

# Problem: a text-based program to convert strings into morse code

MORSE_CODE = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    ',': '--..--',
    '.': '.-.-.-',
    '?': '..--..',
    '/': '-..-.',
    '-': '-....-',
    '(': '-.--.',
    ')': '-.--.-'
}


def text_to_morse(text):
    morse_text = ""
    for letter in text:
        if letter != " ":
            # Find letter into the dictionery
            if letter.upper() in MORSE_CODE:
                morse_text += MORSE_CODE[letter.upper()]
                morse_text += " "
            else:
                print("Error text!")
                exit()
        # There's a space
        else:
            morse_text += "/"
    return morse_text


text_code = input("Please enter text to covert:")
text_morse = text_to_morse(text_code)

print(f"Your text: [{text_code}]\nMorse text: [{text_morse}]")
