#  Created by Simone Margio
#  www.simonemargio.im

# Problem: remove all special symbols and punctuation from a string
# Input: str = "/*This _ is a @funny .( & strin%s"
# Output: This is a funny strings
import string

input_string = "/*This_ is .a @funny &string%s!_"

print(f"Input:[{input_string}]")
output_string = input_string.translate(str.maketrans('', '', string.punctuation))
print(f"Output:[{output_string}]")
