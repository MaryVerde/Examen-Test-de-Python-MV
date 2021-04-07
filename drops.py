num = int(input ("Indica un número entero: "))
if num % 3 == 0:
    if num % 5 == 0:
        if num % 7 == 0:
            print("Plic Plac Ploc")
        else:
            if num % 3 == 0:
                if num % 5 == 0:
                    print("Plic Plac")
    else:
        if num % 3 == 0:
            if num % 7 == 0:
                print("Plic Ploc")
            else:
                print("Plic")
else:
    if num % 5 == 0:
        if num % 7 == 0:
            print("Plac Ploc")
        else:
            print("Plac")
    else:
        if num % 7 == 0:
            print("Ploc")
        else:
           print(num)