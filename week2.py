ch = input("Enter a character: ")
if ch >= '0' and ch <= '9':
    print("Digit")
elif ch >= 'A' and ch <= 'Z':
    print("Uppercase character")
elif ch >= 'a' and ch <= 'z':
    print("Lowercase character")
else:
    print("Special character")
