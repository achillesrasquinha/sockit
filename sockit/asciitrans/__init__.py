"""
Translation table for transliteration of non-ASCII characters.
"""
asciitrans = str.maketrans(
    {
        "\xc0": "A",
        "\xc1": "A",  # Remove accent mark over A
        "\xc2": "A",  # Remove hat mark over A
        "\xc3": "A",  # Remove ~ over A
        "\xc4": "A",
        "\xc5": "A",  # Remove ring over A
        "\xc6": "AE",
        "\xc7": "C",
        "\xc8": "E",
        "\xc9": "E",  # Remove acute over E
        "\xca": "E",
        "\xcb": "E",
        "\xcc": "I",
        "\xcd": "I",
        "\xce": "I",
        "\xcf": "I",  # Remove diaeresis over I
        "\xd0": "D",
        "\xd1": "N",  # Remove ~ on top of N
        "\xd2": "O",  # Remove grave over O
        "\xd3": "O",
        "\xd4": "O",  # Remove hat over O
        "\xd5": "O",  # Remove ~ over O
        "\xd6": "O",  # Remove diaeresis over O
        "\xd7": "x",  # Replace multiplication sign
        "\xd8": "O",
        "\xd9": "U",  # Remove grave over U
        "\xda": "U",  # Remove acute over U
        "\xdb": "U",  # Remove hat over U
        "\xdc": "U",  # Remove diaeresis over U
        "\xdd": "Y",  # Remove acute over Y
        "\xde": "Th",  # Replace capital letter thorn
        "\xdf": "s",  # Replace eszett with single s (assuming lower case)
        "\xe0": "a",  # Remove grave above a
        "\xe1": "a",  # Remove acute above a
        "\xe2": "a",  # Remove circumflex above a
        "\xe3": "a",  # Remove ~ above a
        "\xe4": "a",  # Remove diaeresis above a
        "\xe5": "a",  # Remove ring above a
        "\xe6": "ae",  # Replace ae single letter with ae
        "\xe7": "c",  # Remove tail on c
        "\xe8": "e",  # Remove grave on e
        "\xe9": "e",  # Remove acute on e
        "\xea": "e",
        "\xeb": "e",
        "\xec": "i",
        "\xed": "i",
        "\xee": "i",
        "\xef": "i",  # Remove diaeresis on i
        "\xf0": "d",
        "\xf1": "n",  # Remove ~ on top of n
        "\xf2": "o",
        "\xf3": "o",
        "\xf4": "o",  # Remove hat over o
        "\xf5": "o",
        "\xf6": "o",  # Remove diaeresis over o
        "\xf7": None,  # Remove math symbol
        "\xf8": "o",
        "\xf9": "u",  # Remove grave over u
        "\xfa": "u",  # Remove acute over u
        "\xfb": "u",  # Remove hat over u
        "\xfc": "u",  # Remove diaeresis over u
        "\xfd": "y",  # Replace accent over y
        "\xfe": "th",  # Replace lower case thorn
        "\xff": "y",  # Remove diaeresis over y
    }
)
