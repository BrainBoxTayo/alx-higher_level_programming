#!/usr/bin/python3
'''
replace all . ? : with 2 new lines
'''


def text_indentation(text):
    '''
    Args:
        text: string to be manipulated
    Returns:
        Nothing
    '''
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i < len(text) and text[i] == ' ':
        # handles spaces at beginning of text
        i += 1
    while i < len(text):
        print(text[i], end="")
        if text[i] == ' ' or text[i] in '.?:':
            if text[i] == '.' or text[i] == '?' or text[i] == ':':
                print("\n\n", end="")
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
