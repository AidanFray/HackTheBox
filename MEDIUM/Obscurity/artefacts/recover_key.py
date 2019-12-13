if __name__ == "__main__":
    
    checkData = None
    with open("./check.txt") as f:
        checkData = f.read()

    outData = None
    with open("./out.txt") as f:
        outData = f.read()

    for i, x in enumerate(checkData):

        c = checkData[i]
        o = outData[i]

        keyChar = chr((ord(o) - ord(c)) % 255)

        print(keyChar, end="")
    print()

        