def card_number(num):
    if len(num) ==16:
        num = num[12:]
        star = '*'*12
        print(star+num)
    else: 
       print("invalid")
num = input('enter your credit card number: ')
card_number(num)