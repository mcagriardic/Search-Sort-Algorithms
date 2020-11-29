# Consider an array representing a binary string, where every element's data
# value is 0 or 1. Write a bool function to determine whether the binary string
# had odd parity (an off number of 1 bits). Return True or False

# bs -> bit string
def is_odd_parity(bs, count=0):

    if len(bs) == 0:
        return 0

    count += int(int(bs[0]) % 2  == 1) + is_odd_parity(bs[1:], count)

    return count % 2 == 1

is_odd_parity("10111")

# >> False

is_odd_parity("1011")

# >> True
