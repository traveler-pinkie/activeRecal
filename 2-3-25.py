def tidyNumber(n):
    n = str(n)
    numArray = list(n)
    for i in range(len(numArray)-1):
        if(numArray[i] > numArray[i+1]):
            return False
    return True

print(tidyNumber(1024))
print(tidyNumber(13579))
