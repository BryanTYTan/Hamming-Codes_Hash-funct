import math
import constants



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

    # split string up into 7 bit chars
    for i in range(0, len(data),7):
        '''
        > it gets the 7 bits of data that corresponds to a char
        > converts string to an int, specifying that it is based in binary
        > converts int ascii char
        > appends it to string
        '''
        Symbol = chr(int(data[i:i+7],2))
        stringy += Symbol

    return stringy

# prep data for transfer with error tollerance
# Num of Redundant bits need to satisfy 2^r >= data_bits + r + 1
# Redundant bits = 4; 2^4 / 16 >= 7 + 4 + 1 / 12
def hamming(data : str) -> str:
    transport = ""
    tempt = StringToBinary(data)
    
    for i in range(0,len(tempt),7):
        # split & reverse string into char array
        Ham = list(tempt[i:i+7][::-1])
        # tempt vars
        r1 = r2 = r4 = r8 = 0

        # insert redundant bits, defaulted to 0
        Ham.insert(0,0),Ham.insert(1,0),Ham.insert(3,0),Ham.insert(7,0)

        # calculate redundant bits and update them
        for j in range(len(Ham)):
            holder = bin(j+1)[2:]
            if (holder[-1] == constants.R_Check):
                r1 += 1
            if (len(holder) >= 2):
                if (holder[-2] == constants.R_Check and Ham[j] == constants.R_Check):
                    r2 += 1
            if (len(holder) >= 3):
                if (holder[-3] == constants.R_Check and Ham[j] == constants.R_Check):
                    r4 += 1
            if (len(holder) >= 4):
                if (holder[0] == constants.R_Check and Ham[j] == constants.R_Check):
                    r8 += 1

        # ensure that everything ends in an even parity
        if r1 % 2 != 0:
            Ham[0] = 1
        if r2 % 2 != 0:
            Ham[1] = 1
        if r4 % 2 != 0:
            Ham[3] = 1
        if r8 % 2 != 0:
            Ham[7] = 1
        
        s = ''.join(str(x) for x in Ham[::-1])
        transport += s


    return transport

# interpret transfered data
def Dehamming(data : str) -> str:    
    # convert binary data to string data
    data = BinaryToString(data)

    return data

# intentionally alter a bit 
# in reality this error may occur during the transmission of data 
def BitInterferance(data : str) -> str:
    # Var to ensure i don't do a while true loop
    Loop_control = True

    print("\nthere are currently {} bits you can alter".format(len(data)))

    # handle user's inputs to always be valid.
    while(Loop_control):
        try:
            # if it is not a number throw exception
            bitaltered = int(input("Which bit would you like to alter: "))
            # if it is a number but too big or small, throw exception
            if bitaltered > len(data) or bitaltered <= 0:
                raise ValueError()
            Loop_control = False
        
        except ValueError:
            print("please enter a valid Number\n")

    s = list(data)
    if s[bitaltered-1] == "0":
        s[bitaltered-1] = "1"
    else:
        s[bitaltered-1] = "0"
    alteredData = "".join(s)
    

    return alteredData

def main():
    stringy = "Y"
    transport_data = hamming(stringy)
    print(transport_data)

    transport_data = BitInterferance(transport_data)

    print(transport_data)

    #received_data = Dehamming(transport_data)
    #print(received_data)

    return


# call program
main()