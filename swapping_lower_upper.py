def swap_letters(data):
    return ''.join([_.lower() if _.isupper() else _.upper() for _ in list(data)])

name = "RagAsImgeR"
result = swap_letters(name)
print(result)
# >> rAGaSiMGEr