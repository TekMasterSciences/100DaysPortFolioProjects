

"""
Author: Aditya Verma Gottumukkala
Project : Morse Code Converter
Function: Should be able to encode string text into International Morse Code
"""

space_between_char  = 2 # Pause between characters

# Morse Code Table
morse_code_dict = {

    # Alphabet symbols
    'a' : '· – ',
    'b' : '– · · · ',
    'c' : '– · – · ',
    'd' : '– · · ',
    'e' : '· ',
    'f' : '· · – · ',
    'g' : '– – · ',
    'h' : '· · · · ',
    'i' : '· · ',
    'j' : '· – – – ',
    'k' : '– · – ',
    'l' : '· – · · ',
    'm' : '– – ',
    'n' : '– · ',
    'o' : '– – – ',
    'p' : '· – – · ',
    'q' : '– – · – ',
    'r' : '· – · ',
    's' : '· · · ',
    't' : '– ',
    'u' : '· · – ',
    'v' : '· · · – ',
    'w' : '· – – ',
    'x' : '– · · – ',
    'y' : '– · – – ',
    'z' : '– – · · ',

    # Numbers
    '0' : '– – – – – ',
    '1' : '· – – – – ',
    '2' : '· · – – – ',
    '3' : '· · · – – ',
    '4' : '· · · · – ',
    '5' : '· · · · · ',
    '6' : '– · · · · ',
    '7' : '– – · · · ',
    '8' : '– – – · · ',
    '9' : '– – – – · ',

    # Special Symbols
    '.' : '· – · – · – ',
    ',' : '– – · · – – ',
    '?' : '· · – – · · ',
    "'" : '· – – – – · ',
    '!' : '– · – · – – ',
    '/' : '– · · – · ',
    '(' : '– · – – · ',
    ')' : '– · – – · – ',
    '&' : '· – · · · ',
    ':' : '– – – · · · ',
    ';' : '– ·– · – · ',
    '=' : '– · · · – ',
    '+' : '· – · – · ',
    '-' : '– · · · · – ',
    '_' : '· · – – · – ',
    '"' : '· – · · – · ',
    '$' : '· · · – · · – ',
    '@' : '· – – · – · ',
    ' ' : '      ', # Space will create a space between words in the encoded morse code
}

print("------- Morse Code Converter App -------")

text_to_be_encoded = input("Enter text to be encoded: ")

# Split string text characters into elements in a list
text_split_up = list(text_to_be_encoded)

encoded_text = list()

for char in text_split_up:

    # Map string characters into Morse Code and save it into encoded data storage
    encoded_text.append(morse_code_dict[char.lower()])
    encoded_text.append('  ')

# Output converted data
print(''.join(encoded_text))