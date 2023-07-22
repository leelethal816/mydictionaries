alpha_dict = {
    "A": "1",
    "a": "!",
    "B": "2",
    "b": "@",
    "C": "3",
    "c": "#",
    "D": "4",
    "d": "$",
    "E": "5",
    "e": "%",
    "F": "6",
    "f": "^",
    "G": "7",
    "g": "&",
    "H": "8",
    "h": "*",
    "I": "9",
    "i": "(",
    "J": "<",
    "j": ")",
    "K": ">",
    "k": "-",
    "L": "_",
    "l": "+",
    "M": "[",
    "m": "]",
    "N": "{",
    "n": "}",
    "O": ":",
    "o": "|",
    "P": ";",
    "p": ",",
    "Q": "n",
    "q": "o",
    "R": ".",
    "r": "/",
    "S": "?",
    "s": "~",
    "T": "`",
    "t": "a",
    "U": "b",
    "u": "c",
    "V": "d",
    "v": "e",
    "W": "f",
    "w": "g",
    "X": "h",
    "x": "i",
    "Y": "j",
    "y": "k",
    "Z": "l",
    "z": "m",
    " ": "s",
    ":": "q",
    ".": "z",
}

info_sec = open("info_security.txt", "r")

output_file = open("encrypted.txt", "w")

info_sec = info_sec.read()

for each in info_sec:
    if each in alpha_dict:
        output_file.write(alpha_dict[each])

output_file.close()
