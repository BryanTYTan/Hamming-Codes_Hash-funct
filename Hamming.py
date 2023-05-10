import math

def StringToBinary(data : str) -> str:
    s = ""
    # convert char to ascii number 
    # Conver ascii number to binary while standarizing them to all be 7 bits long
    for i in data:
        fixer = str(bin(ord(i))[2:])
        while len(fixer) < 7:
            fixer = "0" + fixer
        s += fixer

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