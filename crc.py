def xor(a, b):
    """Perform XOR operation between two binary strings."""
    result = []
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)

def mod2div(dividend, divisor):
    """Perform Modulo-2 division and return the remainder."""
    pick = len(divisor)
    tmp = dividend[0:pick]

    while pick < len(dividend):
        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + dividend[pick]
        else:
            tmp = xor('0'*pick, tmp) + dividend[pick]
        pick += 1

    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0'*pick, tmp)
        
    return tmp

def encodeData(data, key):
    """Encode data by appending CRC bits."""
    l_key = len(key)
    appended_data = data + '0'*(l_key-1)
    remainder = mod2div(appended_data, key)
    return data + remainder

# User input for frame size, frame, generator size, and generator
frame_size = int(input("Enter frame size: "))
frame = input(f"Enter frame (binary string of length {frame_size}): ")
generator_size = int(input("Enter generator size: "))
generator = input(f"Enter generator (binary string of length {generator_size}): ")

print("\nSender Side:")
print(f"Frame size: {frame_size}")
print(f"Frame: {frame}")
print(f"Generator size: {generator_size}")
print(f"Generator: {generator}")

# Number of zeroes to be appended (generator size - 1)
num_zeroes = generator_size - 1
print(f"No. of zeroes to be appended: {num_zeroes}")

# Message after appending zeroes
appended_message = frame + '0' * num_zeroes
print(f"Message after appending 0's: {appended_message}")

# Calculate CRC bits and transmitted frame
transmitted_frame = encodeData(frame, generator)
crc_bits = transmitted_frame[-num_zeroes:]
print(f"CRC bits: {crc_bits}")
print(f"Transmitted frame: {transmitted_frame}")

print("\nReceiver Side:")
received_frame = input(f"Enter the received frame (binary string of length {len(transmitted_frame)}): ")

# Check remainder
remainder = mod2div(received_frame, generator)
print(f"The remainder is: {remainder}")

if '1' not in remainder:
    print("Message transmission is correct")
else:
    print("Message transmission is incorrect")
