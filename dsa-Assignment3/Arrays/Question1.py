def add_one(digits):
    num = int(''.join(map(str, digits)))
    num += 1
    return [int(digit) for digit in str(num)]

# Test Cases
print(add_one([1, 2, 3]))  # Output: [1, 2, 4]
print(add_one([9, 9]))     # Output: [1, 0, 0]
print(add_one([0]))        # Output: [1]
print(add_one([1, 0, 0, 0]))  # Output: [1, 0, 0, 1]
