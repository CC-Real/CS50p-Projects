def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    new_dollar = d.replace("$", "")
    return float(new_dollar)
def percent_to_float(p):
    new_percent = p.replace("%","")
    return float(new_percent) / 100

main()
