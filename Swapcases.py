def swap_case(s):
    a=[]
    for i in s:
        if(i.islower()):
            a.append(i.upper())
        else:
            a.append(i.lower())
    return ''.join(a)
