def cookie(x):
    if type(x) == int or type(x) == float:
        return "Who ate the last cookie? It was Monica!"
    elif type(x) == str:
        return "Who ate the last cookie?It was Zach!"
    else:
        return "Who ate the last cookie? It was the dog!"

print(cookie("Ryan"))
print(cookie(2.3))
print(cookie(26))
print(cookie(True))
