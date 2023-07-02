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
    new_text = ""
    for i in range(0, len(text)):
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            new_text += text[i]
            new_text += '\n\n'
            continue
        new_text += text[i]
    print(new_text, end="")
