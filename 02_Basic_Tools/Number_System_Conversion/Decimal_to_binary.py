print(f"====Decimal to Binary Converter")
x = int(input("Enter any number for binary conversion: "))

if x == 0:
    print("Binary: 0")
else:
    sign = ""
    if x < 0:
        sign = "-"
        x = abs(x)

    binary = []
    while x > 0:
        binary.append(x % 2)
        x = x // 2

    binary.reverse()
    final = "".join(str(bit) for bit in binary)
    print(f"Binary: {sign}{final}")
