import math

def StringToBinary(stringy):
    tempt, listo = [], []
    # convert char to ascii number
    for i in stringy:
        tempt.append(ord(i))

    # convert ascii numbers to binary
    for i in tempt:
        listo.append(int(bin(i)[2:]))

    return listo

def BinaryToString(listo):
    stringy = ""

    return stringy

# prep data for transfer
def hamming(listo):

    return listo

# interpret transfered data
def Dehamming(listo):

    return listo

def main():
    stringy = "hello world"
    data = StringToBinary(stringy)
    print(data)
    return


# call program
main()