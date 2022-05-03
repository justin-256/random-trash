i = 0
while True:
    globals()[f"var{i}"] = i
    print(eval("var"+str(i))*i)
    i += 1
#makes a crap ton of variables nd prints them for no reason
