def hashing(text: str) -> str:
    hashed = 0
    
    for i in text:
        tempt = int(bin(ord(i))[2:])
        hashed = hashed * 101 + tempt

    return hashed

def main():
    # testing collision
    inputs = ["Go", "go", "gO"]    
    holder = set()

    for i in inputs:
        holder.add(hashing(i))


    print(holder)

    return

# call program
main()