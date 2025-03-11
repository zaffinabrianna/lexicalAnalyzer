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
                clearedLines.appened(line.strip())
        return clearedLines
    
def tokenization(lines):
    tokens = []

    #Map of lexemes and tokens using regex pattern
    tokenIdentifier =
    [
        ('KEYWORD', r'\b(int|float|double|char|if|else|while|for|return)\b'), #Find pattern of keywords
        ('SEPARATOR', r'[(){};,]'), #Find pattern of seperators
        ('IDENTIFIER', r'\b [a-z A-Z_]\w*\b'), #Find pattern of identifiers
        ('OPERATOR', r'[+\-*/=><!]'), #Find pattern of operators
        ('INTEGER', r'\b\d+\b'), #Find pattern of integers
        ('WHITESPACE', r'\s+'), #Find pattern of whitespace
        ('UNKOWN', r'.') #Catch unknown characters
    ]


def main(): # Main to test lexical analysis
