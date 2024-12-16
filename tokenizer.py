import re


def tokenize(text):
    # Compiling the regex pattern with capturing groups for each part
    pattern = r"""
        (?P<abbreviation>(?:[A-Z]\.)+)                          # Abbreviations (e.g., U.S.A., U.K.)
        | (?P<contractions>(?:[A-Za-z]+(?:'[A-Za-z]+)+))        # Contractions (e.g., "isn't")
        | (?P<hyphenated>[A-Za-z]+(?:-[A-Za-z]+)+)              # Hyphenated words (e.g., ice-cream)
        | (?P<word>[A-Za-z]+)                                   # Regular words
        | (?P<numbers>\d+)                                      # Numbers
        | (?P<punctuation>[.,!?;:])                             # Punctuation
        | (?P<brackets>[\(\)\[\]{}])                            # Brackets and braces
        | (?P<quotes>["'`]+)                                    # Quotes and other single-character symbols
    """


    compiled_pattern = re.compile(pattern, re.VERBOSE)
    matches = compiled_pattern.finditer(text)

    tokens = []

    for match in matches:
        
        if match.group('contractions'):
            print(match.group('contractions'))
            splitted = match.group('contractions').split("'")
            splitted[1] = splitted[0][-1] + "'" + splitted[1]
            splitted[0] = splitted[0][:-1]
            tokens.append(splitted[0])
            tokens.append(splitted[1])
        else:
            token_types = ['abbreviation', 'hyphenated', 'word', 'numbers', 'punctuation', 'brackets', 'quotes']
            for token_type in token_types:
                if match.group(token_type):
                    tokens.append(match.group(token_type))   

    return tokens


sentence = "I love ice-cream ,but he doesn't like it. If he isn't here, I will go to the U.S.A. in 10 hours (from now)."
tokens = tokenize(sentence)
print(tokens)