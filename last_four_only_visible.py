input="rresjiurns"
l=len(input)
for item in input:
    if (l>4) and (input.index(item) <=(l-4)):
        string=input.replace(item,'#')
print(string)