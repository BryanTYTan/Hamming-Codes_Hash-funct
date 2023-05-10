import math

def StringToBinary(data : str) -> str:
    tempt, listo = [], []
    # convert char to ascii number
    for i in data:
        tempt.append(ord(i))
    
    # convert ascii numbers to binary
    for i in tempt:
        listo.append(int(bin(i)[2:]))

    s = ''.join(str(x) for x in listo)

    return s

def BinaryToString(data : str) -> str:
    stringy = ""

    for i in data:
        print(i)

    return stringy

# prep data for transfer with error tollerance 
def hamming(data : str) -> str:

    return data

# interpret transfered data
def Dehamming(data : str) -> str:

    return data

# intentionally alter a bit 
# in reality this error may occur during the transmission of data 
def BitInterferance(data : str) -> str:
    return data

def main():
    stringy = "1!"
    transport_data = StringToBinary(stringy)
    print(transport_data)

    # BitInterferance(transport_data)

    received_data = Dehamming(transport_data)


    return


# call program
main()