k=-7
i=input()
result=""
for character in i:
    a=chr(int(ord(character))+k)
    result += a
print(result)