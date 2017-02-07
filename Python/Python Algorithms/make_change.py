def change(cents):
    coins = {}
    coins["dollar"] = int(cents/100)
    coins["quarter"] = int((cents % 100) / 25)
    coins["dimes"] = int((cents % 25)/10)
    coins["nickels"] = int(((cents % 25) % 10) / 5)
    coins["pennies"] = int(cents % 5)
    return coins
print change(372)
