def day_of_week(DD, MM, YYYY):
    month = ["January", "February", "March", "April", "May", "June, "July","August", "September", "October", "November", "December"]

    if DD == 32 and MM == 13 and YYYY == -1:
        print(" Please enter your birthday in this ")
        print("     format (including spaces):      ")
        print("            DD MM YYYY              ")
        return -1

    if DD <= 0:
        if MM <= 0:
            print(" We don't have negative or null days and months. ")
            print("                   Try again!                    ")
            return -1

        print(" We don't have negative or null days. ")
        print("              Try again!              ")
        return -1

    if MM <= 0:
        print(" We don't have negative or null months. ")
        print("               Try again!               ")
        return -1

    if DD > 31 or MM > 12 or YYYY <= 0:
        if DD > 31 and MM > 12:
            if YYYY <= 0:
                print(" We have 12 months, the days of a month are up to 31 ")
                print("       and a year should be a positive number.       ")
                print("                     Try again!                      ")
            else:
                print("       We have 12 months and       ")
                print(" the days of a month are up to 31. ")
                print("            Try again!             ")

        elif DD > 31 and MM <= 12:
            if YYYY <= 0:
                print(" The days of a month are up to 31 and ")
                print(" a year should be a positive number.  ")
                print("             Try again!               ")
            else:
                print(" The days of a month are up to 31. ")
                print("            Try again!             ")

        elif DD <= 31 and MM > 12:
            if YYYY <= 0:
                print("        We have 12 months and        ")
                print(" a year should be a positive number. ")
                print("             Try again!              ")
            else:
                print(" We have 12 months. ")
                print("     Try again!     ")

        elif DD <= 31 and MM <= 12 and YYYY <= 0:
            print(" A year should be a positive number. ")
            print("             Try again!              ")
        return -1

    if MM == 2:
        if (YYYY % 400 == 0) or ((YYYY % 4 == 0) and (YYYY % 100 != 0)):
            if DD > 29:
                print("  The year", YYYY, "is a leap year. ")
                print(" So, February has up to 29 days.          ")
                print("           Try again!                     ")
                return -1
        else:
            if DD > 28:
                print(" The year", YYYY, "isn't a leap year. ")
                print(" So, February has up to 28 days.            ")
                print("           Try again!                       ")
                return -1

    elif MM in [4, 6, 9, 11]:
        if DD > 30:
            print(month[MM - 1], "has up to 30 days. ")
            print("        Try again!        ")
            return -1

    if MM <= 2:
        NYYYY = YYYY - 1
        NMM = 0
    else:
        NYYYY = YYYY
        NMM = (4 * MM + 23) // 10

    IDAY = 365 * YYYY + DD + 31 * (MM - 1) - NMM + (NYYYY // 4) - ((3 * ((NYYYY // 100) + 1) // 4))

    day = IDAY % 7

    flag = DD % 10 if DD not in {11, 12, 13} else 0

    days_of_week = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    print(" You were born on", days_of_week[day] + ",", end=" ")

    if flag == 1:
        print(f"{DD}st of ", end="")
    elif flag == 2:
        print(f"{DD}nd of ", end="")
    elif flag == 3:
        print(f"{DD}rd of ", end="")
    else:
        print(f"{DD}th of ", end="")

    print(month[MM - 1], f"of {YYYY}!")

#input -- 9 3 2003
# Example usage:
DD,MM,YYYY=list(map(int,input().split()))
day_of_week(DD, MM, YYYY)
