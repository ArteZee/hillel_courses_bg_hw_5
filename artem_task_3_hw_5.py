lst_numbers = [12, 21, 66, 44, 76, 534]
i = 0

while i <= len(lst_numbers) - 1:
    if lst_numbers[i] % 2 == 0:
        i += 1

    else:
        print("NO")
        break

else:
    print("all numbers are even")



