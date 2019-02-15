'''
@author : Ajay Singh Parmar
@created on : Febuary 15, 2019
- Description: Convert Decimal number to binary format.
e.g. 13 --- 1011;
'''


#: convert number to its binary bits.
def get_bits_in_list(num):
    """ Convert a decimal number into a list of binary bits."""
    list_of_bits = list()
    while True:
        rem = num % 2
        list_of_bits.append(rem)
        num = int(num / 2)
        if num == 0:
            break
    return list_of_bits[::-1]


#: change bits to proper binary format.
def bits_to_binary(list_of_bits):
    """Takes a list of binary bits and join them to forma binary string."""
    binary = ''
    for num in list_of_bits:
        if num != 0:
            binary = binary + str(num)
        else:
            binary = binary + '0'
    return binary


#: to test the binary conversion.
def main():
    """main to to check all functions and behaviors."""
    num = int(input("Enter Number to convert to binary : "))
    list1 = get_bits_in_list(num)
    print(bits_to_binary(list1))


#: boiler-plate code for __main__ program.
if __name__ == '__main__':
    main()
