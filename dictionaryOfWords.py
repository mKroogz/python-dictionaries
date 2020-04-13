"""
Create a dictionary with key value pairs to
represent words (key) and its definition (value)
"""
word_definitions = dict()

"""
Add several more words and their definitions
   Example: word_definitions["Awesome"] = "The feeling of students when they are learning Python"
"""
word_definitions["Programmer"] = "A person who turns caffeine into code"
word_definitions["Flexbox"] = "The hero of CSS and styling"
word_definitions["Rubber Ducking"] = "Talking to a rubber duck to help understand your own code"

"""
Use square bracket lookup to get the definition of two
words and output them to the console with `print()`
"""
for (key, value) in word_definitions.items():
    print(f'The definition of {key} is "{value}"')

"""
Loop over the dictionary to get the following output:
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
"""