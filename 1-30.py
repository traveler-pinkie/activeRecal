def findEnglish(args):
    args = args.lower()
    argsArray = list(args)
    for index in range(len(argsArray)-1):
        if (argsArray[index] == 'e' and argsArray[index+1] == 'n' and argsArray[index+2] == 'g' and argsArray[index+3] == 'l' and argsArray[index+4] == 'i' and argsArray[index+5] == 's' and argsArray[index+6] == 'h'):
            return True
    return False

print(findEnglish("1234english ;k"))