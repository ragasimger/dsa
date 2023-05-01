# Read a given string, change the character at a given index and then print the modified string.

def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]


data = 'abracadabra'
position = 5
character = 'k'

print(mutate_string(
    string=data,
    position=position,
    character=character
    )
)