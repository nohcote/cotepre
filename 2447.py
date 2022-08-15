def func(num, text):
    if num == 1:
        return [text]
    stars = func(int(num/3), text)
    arr = []
    
    [arr.append(s*3) for s in stars]
    [arr.append(s + " "*int(num/3) + s) for s in stars]
    [arr.append(s*3) for s in stars]
    
    return arr

txt = "*"
print("\n".join(func(int(input()), txt)))