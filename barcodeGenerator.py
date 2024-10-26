# Barcode Generator

# Input the start and end values for the barcode range
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

# Convert the start and end values to lists of digits for easy access
start_digits = [int(d) for d in str(start)]
end_digits = [int(d) for d in str(end)]

# Initialize a list to store all valid barcodes
valid_barcodes = []

# Loop through each digit within the specified range for each position
for d1 in range(start_digits[0], end_digits[0] + 1):
    for d2 in range(start_digits[1], end_digits[1] + 1):
        for d3 in range(start_digits[2], end_digits[2] + 1):
            for d4 in range(start_digits[3], end_digits[3] + 1):

                # Construct the barcode as a string from the four digits
                barcode = f"{d1}{d2}{d3}{d4}"

                # Check if all digits in the barcode are odd
                if all(int(digit) % 2 != 0 for digit in barcode):
                    # If all digits are odd, add the barcode to the list of valid barcodes
                    valid_barcodes.append(barcode)

# Print all valid barcodes, separated by spaces
print(" ".join(valid_barcodes))
