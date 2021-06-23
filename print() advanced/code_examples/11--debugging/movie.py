def movie_year(number):
    roman = { 1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M', }

    output = []
    divisor = 1000
    print(f'movie_year({number})')
    for digit in [int(x) for x in str(number)]:
        print(f'   digit={digit} divisor={divisor}')
        if 1 <= digit <= 3:
            # e.g. 3 -> 3*'I' -> 'III'
            output.append( roman[divisor] * digit )
        elif digit == 4:
            output.append( roman[divisor] +  roman[divisor * 5] )
        elif 5 <= digit <= 8:
            output.append( roman[divisor * 5] + roman[divisor] * (digit - 5) )
        elif digit == 9:
            output.append( roman[divisor] + roman[divisor * 10] )

        divisor = int(divisor / 10)
        print('      ', output)

    return ''.join(output)
