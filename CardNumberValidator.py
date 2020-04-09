def check_card(num):
    validlist = []
    for i in num:
        validlist.append(int(i))
    for i in range(0, len(num), 2):  # applying Luhn Algorithm to check whether resulting sum is divisible by ten
        validlist[i] = validlist[i] * 2
        if validlist[i] >= 10:
            validlist[i] = (validlist[i] // 10 + validlist[i] % 10)

    if sum(validlist) % 10 == 0:
        print("This is a valid card.")

    else:
        print('Invalid card number.')

def cardnumber():
    n = ''
    while True:
        try:
            n = input('Enter you card number [16 digit]: ')
            if not (len(n) == 16) or not type(int(n) == int):
                raise Exception

        except Exception:
            print('This is not a valid card number - please try again.')
            continue
        else:
            break

    return n

def tryagain():
    return input("Do you want to try again? : ").lower()[0] == 'y'

def main():
    while True:
        num = cardnumber()
        check_card(num)

        if not tryagain():
            break

if __name__ == '__main__':
    main()