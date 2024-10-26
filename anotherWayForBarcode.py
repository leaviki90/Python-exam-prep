# Barcode Generator

# Input the start and end values for the range
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

# Convert start and end values to strings to access individual digits
start_str = str(start)
end_str = str(end)

# Extract individual digits from the start and end values
start_first_digit = int(start_str[0])
start_second_digit = int(start_str[1])
start_third_digit = int(start_str[2])
start_fourth_digit = int(start_str[3])

end_first_digit = int(end_str[0])
end_second_digit = int(end_str[1])
end_third_digit = int(end_str[2])
end_fourth_digit = int(end_str[3])

# Loop through each digit in the specified range for each position
for first_digit in range(start_first_digit, end_first_digit + 1):
    # Check if the first digit is odd
    if first_digit % 2 != 0:
        for second_digit in range(start_second_digit, end_second_digit + 1):
            # Check if the second digit is odd
            if second_digit % 2 != 0:
                for third_digit in range(start_third_digit, end_third_digit + 1):
                    # Check if the third digit is odd
                    if third_digit % 2 != 0:
                        for fourth_digit in range(start_fourth_digit, end_fourth_digit + 1):
                            # Check if the fourth digit is odd
                            if fourth_digit % 2 != 0:
                                # Construct a number from the four odd digits
                                number = (first_digit * 1000 +
                                          second_digit * 100 +
                                          third_digit * 10 +
                                          fourth_digit)
                                # Check if the number is within the specified range
                                if start <= number <= end:
                                    print(number, end=' ')
