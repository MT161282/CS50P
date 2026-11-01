while True:
    try:
        fraction = input("Fraction: ")
        x, y = fraction.split("/")

        x = int(x)
        y = int(y)

        if x < 0 or y <= 0 or x > y:
            continue

        percentage = round(x / y * 100)

    except (ValueError, ZeroDivisionError):
        pass
    else:
        break

if percentage <= 1:
    print("E")
elif percentage >= 99:
    print("F")
else:
    print(f"{percentage}%")
