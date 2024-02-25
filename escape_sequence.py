print("Hello")
#Escape sequence 
print("Hello\nWorld")#Inserts a new line character
print("Hello\tWorld")#Insert a tab character
print("Hello\"World")#Insert a double quotation mark
print("Hello\'World")#Insert a single quotation mark
print("Hello\\World")#Insert a backslash character
print("Hello\bWorld")#Insert a backspace character


#print statement

print(object(s), sep=separator, end=end, file=file, flush=flush)

'''object(s): Any object, and as many as you like. Will be converted to string before printed

sep='separator': Specify how to separate the objects, if there is more than one. Default is ' '

end='end': Specify what to print at the end. Default is '\n' (line feed)

file: An object with a write method. Default is sys.stdout

Parameters 2 to 4 are optional'''