def scale(string, k, v):
    if(string == ""):
        return ""
    else:
        holder = ""
        strArray=  string.split("\n")
        for i in range(len(strArray)):
            for ele in strArray[i]:
                holder = holder + (ele*k)
            strArray[i] = (holder + "\n") * v
            holder = ""
        joined_string = "".join(strArray)
        joined_string = joined_string[:-1]
        print(joined_string)


a = "abcd\nefgh\nijkl\nmnop"
scale(a, 2, 3)
