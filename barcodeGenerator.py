#6.	Barcode Generator
start = int(input())
end = int(input())


start_digits = [int(d) for d in str(start)]
end_digits = [int(d) for d in str(end)]


valid_barcodes = []


for d1 in range(start_digits[0], end_digits[0] + 1):
    for d2 in range(start_digits[1], end_digits[1] + 1):
        for d3 in range(start_digits[2], end_digits[2] + 1):
            for d4 in range(start_digits[3], end_digits[3] + 1):

                barcode = f"{d1}{d2}{d3}{d4}"


                if all(int(digit) % 2 != 0 for digit in barcode):
                    valid_barcodes.append(barcode)


print(" ".join(valid_barcodes))

