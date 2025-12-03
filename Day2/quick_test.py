def is_repeated_pattern(n):
    s = str(n)
    length = len(s)
    if length % 2 != 0:
        return False
    half = length // 2
    first_half = s[:half]
    second_half = s[half:]
    return first_half == second_half and first_half[0] != '0'

print('Testing key values from the example:')
print(f'11: {is_repeated_pattern(11)}')
print(f'22: {is_repeated_pattern(22)}')
print(f'99: {is_repeated_pattern(99)}')  
print(f'1010: {is_repeated_pattern(1010)}')
print(f'1188511885: {is_repeated_pattern(1188511885)}')
print(f'222222: {is_repeated_pattern(222222)}')
print(f'446446: {is_repeated_pattern(446446)}')
print(f'38593859: {is_repeated_pattern(38593859)}')

# Sum them
total = 11 + 22 + 99 + 1010 + 1188511885 + 222222 + 446446 + 38593859
print(f'\nExpected sum from example: 1227775554')
print(f'Actual sum: {total}')
print(f'Match: {total == 1227775554}')
