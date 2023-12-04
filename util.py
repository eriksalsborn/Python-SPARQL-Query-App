def capitalize_first_letter(input_string):
    return input_string.title()

def replace_white_space_with_underscore(input_string):
    return input_string.replace(" ", "_") 

def format_input(input_string):
    input_string = capitalize_first_letter(input_string)
    input_string = replace_white_space_with_underscore(input_string)
    return input_string