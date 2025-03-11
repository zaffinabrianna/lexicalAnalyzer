# Brianna Zaffina & Harry Derderian
# CPSC 323
# Professor Venkatesh
# 24 March 2025

import re # Import Reg Expression 

# Function that reads files and returns the lines to be read
def fileRead(filename):
    with open(filename, 'r') as file: # Opens a file and reads it
        return file.readlines()       # Returns the lines to be read

# Function that removes unnecessary items such as white space and comment lines
def removeUnnecessaryItems(lines):
        clearedLines = []

        # Remove single-line comments
        for line in lines:

            # Subs patterns it finds with ''
            line = re.sub(r'//.*', '', line)

            # Removes leading and trailing characters
            if line.strip(): 
                clearedLines.append(line.strip())
        return clearedLines
    
def tokenization(lines):
    tokens = []

    #Map of lexemes and tokens using regex pattern
    tokenIdentifier = [
        ('KEYWORD', r'\b(int|float|double|char|if|else|while|for|return)\b'), #Find pattern of keywords
        ('SEPARATOR', r'[(){};,]'), #Find pattern of seperators
        ('IDENTIFIER', r'\b[a-zA-Z_]\w*\b'), #Find pattern of identifiers
        ('OPERATOR', r'[+\-*/=><!]'), #Find pattern of operators
        ('INTEGER', r'\b\d+\b'), #Find pattern of integers
        ('WHITESPACE', r'\s+'), #Find pattern of whitespace
        ('UNKOWN', r'.') #Catch unknown characters
    ]

# Token that takes the the token identifier and puts it into one string
    token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in tokenIdentifier) 

#Iterates each line of the file and applies tokenization to it
    for line in lines:
        #Finds pattern and registers the tokens
        for match in re.finditer(token_regex, line):
            # Takes the type of identifier found
            token_type = match.lastgroup
            # Takes the actual token value
            token_value = match.group(token_type)

            #If the token type isn't a white space and isn't an unknown character
            # Append the token (in lower cases) to the "token" obj
            if token_type != 'WHITESPACE' and token_type != 'UNKNOWN':
                tokens.append((token_value, token_type.lower()))
    return tokens

def main(): # Main to test lexical analysis
    filename = input("Input file name: ")
    lines = fileRead(filename)
    cleanLines = removeUnnecessaryItems(lines)
    tokens = tokenization(cleanLines)

    print("Erm:\n")
    for lexeme, token in tokens:
         print(f'"{lexeme}" = {token}')

if __name__ == "__main__":
    main()