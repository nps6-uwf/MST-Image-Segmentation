def color_text(text, color):
    '''Supported colors:
    red, blue, green, yellow
    '''
    colors={
        "magenta":"\u001b[35m",
        "green":"\u001b[32m",
        "blue":"\u001b[34m",
        "yellow":"\u001b[33m",
        "reset":"\u001b[0m"
    }
    key = color.lower().strip()
    if key in colors:
        return colors[key]+f"{text}" + colors['reset']
    else: return text