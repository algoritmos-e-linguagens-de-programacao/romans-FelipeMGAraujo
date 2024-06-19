def int_to_roman(num):
    
    milhar = ["", "M", "MM", "MMM"]
    centena = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    dezena = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    unidade = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

    return milhar[num // 1000] + centena[(num % 1000) // 100] + dezena[(num % 100) // 10] + unidade[num % 10]

def roman_to_int(s):
    
    roman_int = { 'I': 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000 }
    total = 0
    i = 0

    for i in range( len(s) ):
        if i + 1 < len(s) and roman_int[s[i]] < roman_int[s[i + 1]]:
            total -= roman_int[s[i]]

        else:
            total += roman_int[s[i]]

    return total

#print( int_to_roman(2002) )
#print( roman_to_int('MMII') )
