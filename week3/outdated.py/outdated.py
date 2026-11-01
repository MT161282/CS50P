months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

while True:
    date = input("Date: ").strip()

    try:
        if "/" in date:
            month, day, year = date.split("/")

            month = int(month)
            day = int(day)
            year = int(year)

        else:
            month_day, year = date.split(", ")
            month, day = month_day.split()

            month = months.index(month) + 1
            day = int(day)
            year = int(year)

        if 1 <= month <= 12 and 1 <= day <= 31:
            break

    except ValueError:
        pass

print(f"{year:04d}-{month:02d}-{day:02d}")
