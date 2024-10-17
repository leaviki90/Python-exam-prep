#6.	Barcode Generator  Another solution
start = int(input())
end = int(input())


start_str = str(start)
end_str = str(end)


start_first_digit = int(start_str[0])
start_second_digit = int(start_str[1])
start_third_digit = int(start_str[2])
start_fourth_digit = int(start_str[3])

end_first_digit = int(end_str[0])
end_second_digit = int(end_str[1])
end_third_digit = int(end_str[2])
end_fourth_digit = int(end_str[3])


for first_digit in range(start_first_digit, end_first_digit + 1):
    if first_digit % 2 != 0:
        for second_digit in range(start_second_digit, end_second_digit + 1):
            if second_digit % 2 != 0:
                for third_digit in range(start_third_digit, end_third_digit + 1):
                    if third_digit % 2 != 0:
                        for fourth_digit in range(start_fourth_digit, end_fourth_digit + 1):
                            if fourth_digit % 2 != 0:
                                #Creating a number from all digits
                                number = (first_digit * 1000 +
                                        second_digit * 100 +
                                        third_digit * 10 +
                                        fourth_digit)
                                #
                                if start <= number <= end:
                                    print(number, end= ' ')




