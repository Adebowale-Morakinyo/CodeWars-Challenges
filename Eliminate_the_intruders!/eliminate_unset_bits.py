def eliminate_unset_bits(number):
    bits = ''.join(bit for bit in number if bit == '1')
    return int(bits, 2) if bits else 0
