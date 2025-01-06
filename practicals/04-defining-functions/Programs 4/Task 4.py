def remove_last_character(string):
    if len(string) > 1:
        return string[:-1]
    else:
        return string

print(remove_last_character("Hello World"))
