def calculate_parity_bits(data, m, r):
    """Calculate and set parity bits in the encoded data."""
    for i in range(r):
        parity = (1 << i)
        parity_value = 0
        for j in range(1, m + r + 1):
            if j & parity:
                parity_value ^= int(data[j - 1])
        data[parity - 1] = str(parity_value)

def encode_data(data, m, r):
    """Encode data by inserting parity bits and setting their values."""
    encoded_data = ['0'] * (m + r)
    j = 0  # Parity bit position
    k = 0  # Data bit position
    for i in range(1, m + r + 1):
        if i == (1 << j):  # Parity bit location
            j += 1
        else:
            encoded_data[i - 1] = data[k]
            k += 1

    calculate_parity_bits(encoded_data, m, r)
    return ''.join(encoded_data)

def detect_and_correct_error(received_data, m, r):
    """Detect and correct a single-bit error in the received data."""
    error_position = 0
    for i in range(r):
        parity = (1 << i)
        parity_value = 0
        for j in range(1, m + r + 1):
            if j & parity:
                parity_value ^= int(received_data[j - 1])
        if parity_value != 0:
            error_position += parity

    return error_position

def main():
    data = input("Enter the data to be transmitted: ")
    m = len(data)
    r = 0

    while (1 << r) < (m + r + 1):
        r += 1

    encoded_data = encode_data(data, m, r)

    print("Original data without parity bits:", data)
    print("Data with parity bits:", encoded_data)

    received_data = input("Enter the received data: ")

    print("Received data:", received_data)

    error_position = detect_and_correct_error(received_data, m, r)
    if error_position == 0:
        print("No error detected.")
    else:
        print(f"Error detected at bit position: {error_position}")
        corrected_data = list(received_data)
        corrected_data[error_position - 1] = '1' if corrected_data[error_position - 1] == '0' else '0'
        print("Corrected data:", ''.join(corrected_data))

if __name__ == "__main__":
    main()
