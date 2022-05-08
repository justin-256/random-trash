str = "put this item in box thing"

def put(str):
    str = str.split()
    command = str[0]
    if "in" in str:
        x = str.index("in")
    elif "on" in str:
        x = str.index("on")
    else:
        print("ERROR: NO ACTION")
    item = " ".join(str[1:x])
    container = " ".join(str[x+1:])
    print(command)
    print(item)
    print(str[x])
    print(container)
    
put(str)
