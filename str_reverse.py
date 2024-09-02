def reverse(string):
    l=len(string)
    new_string=''
    for i in string:
        new_string+=string[l-1]
        l-=1
    return new_string
print(reverse('hello'))