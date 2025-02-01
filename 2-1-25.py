def odds(args):
    odds = []
    for ele in args:
        if ele % 2 != 0:
            odds.append(ele)
    return odds

odds([1,3,5])