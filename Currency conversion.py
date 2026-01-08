import os
import time
def asciis():
   return """
Welcome to the currency exchange program.
        
              
        
    ||====================================================================||
    ||//$\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//$\\||
    ||(100)==================| FEDERAL RESERVE NOTE |================(100)||
    ||\\$//        ~         '------========--------'                \\$//||
    ||<< /        /$\              // ____ \\                         \ >>||
    ||>>|  12    //L\\            // ///..) \\         L38036133B   12 |<<||
    ||<<|        \\ //           || <||  >\  ||                        |>>||
    ||>>|         \$/            ||  $$ --/  ||        One Hundred     |<<||
||====================================================================||>||
||//$\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//$\\||<||
||(100)==================| FEDERAL RESERVE NOTE |================(100)||>||
||\\$//        ~         '------========--------'                \\$//||\||
||<< /        /$\              // ____ \\                         \ >>||)||
||>>|  12    //L\\            // ///..) \\         L38036133B   12 |<<||/||
||<<|        \\ //           || <||  >\  ||                        |>>||=||
||>>|         \$/            ||  $$ --/  ||        One Hundred     |<<||
||<<|      L38036133B        *\\  |\_/  //* series                 |>>||
||>>|  12                     *\\/___\_//*   1989                  |<<||
||<<\      Treasurer     ______/Franklin\________     Secretary 12 />>||
||//$\                 ~|UNITED STATES OF AMERICA|~               /$\\||
||(100)===================  ONE HUNDRED DOLLARS =================(100)||
||\\$//\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\$//||
||====================================================================||
              

=========================================================================
"""
ascii=asciis()
currency_bank={ 
        "": ascii,
        "USD": 1.0,
        "EGP": 47.2539,
        "EUR": 0.8558,     
        "CNY": 6.9936,
        "JOD": 0.709,
        "AED": 3.6725,
        "JPY": 156.9118,
        "SAR": 3.75,
        "TRY": 43.0485,
        "MAD": 9.236,
        }
def survey():
    os.system("cls" if os.name=="nt" else "clear")
def conversion(exchange,amount,own):
    if own==1.0:
        return exchange*amount
    elif exchange==1.0:
       return amount/own
    else:
       return (exchange*(amount/own))
def entries():
    while True:
        survey()
        for x in currency_bank:
            print(f"{x} {currency_bank[x]}")
        
        currency=input("\nEnter the currency identification code: ").upper() 
        while True:
            quantity=float(input("\nEnter the quantity: "))
            if input(f"\nYou own {quantity} {currency} Do you want to confirm? (Y/N): ").upper() !="Y":
                continue
            else:
                survey()
                break
        purchase=input("\nEnter the currency you want to convert to: ").upper()
        print("\nI analyze your demand .... Wait a bit")
        time.sleep(2)
        print(f"\nThe best price is being searched for {currency}.....Wait a bit")
        time.sleep(2)
        print(f"\nPrices are being sought {purchase}.....Wait a bit")
        time.sleep(2)
        if currency not in currency_bank or purchase not in currency_bank:
            print("\nMistake for entering an unknown currency.")
            time.sleep(2)
            survey()
            entries()
        else:
            currencys=currency_bank[purchase]
            money=currency_bank[currency]
            survey()
            print(f"\nSearch for conversion rates {currency} to {purchase}....Wait a bit")
            time.sleep(2)
            if money==1.0:
                equals=currencys*money
                print(f"\nExchange Rate: 1{currency} = {round(equals,3)} {purchase}")
            else:
                equals=currencys/money
                print(f"\nExchange Rate: 1{currency} = {round(equals,3)} {purchase}")
            currency_conversion=conversion(exchange=currencys,amount=quantity,own=money)
            print(f"\n{quantity} {currency} is equal to {currency_conversion} {purchase}")
            if input("\nDo you want to complete the purchase (Y/N): ").upper() == "Y":
                print("\nComplete the deal.")
            else:
                print("\nThe deal was canceled.")
        if input("\nDo you want to convert another currency? (Y/N) ").upper() == "Y":
            survey()
            continue
        else:
            survey()
            print("\nThe exit is done....")
            break
entries()