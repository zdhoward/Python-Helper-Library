#!/usr/bin/env python3

def header(text):
    width = 40
    top_dressing = '='
    bot_dressing = '='
    left_dressing = '||'
    right_dressing = '||'

    left_spacer = " "
    right_spacer = " "

    left_spacing = int((width - len(text))/2) - len(left_dressing)
    right_spacing = int((width - len(text))/2) + ((width - len(text))%2) - len(right_dressing)

    head = ""
    head += (top_dressing * width) + '\n'
    head += left_dressing + left_spacer * left_spacing + text + right_spacer * right_spacing + right_dressing + '\n'
    head += (bot_dressing * width) + '\n'
    return head

if __name__ == '__main__':
    print(header("Hello World"))
