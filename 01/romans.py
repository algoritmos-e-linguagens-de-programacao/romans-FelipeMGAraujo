def inteiro_para_romano(num):
    
    mil = [
        "", "M", 
        "MM", "MMM"
    ]
    cem = [
        "", "C", "CC", "CCC", 
        "CD", "D", "DC", 
        "DCC", "DCCC", 
        "CM"
    ]
    dez = [
        "", "X", "XX", "XXX",
        "XL", "L", "LX", 
        "LXX", "LXXX", 
        "XC"
    ]
    uni = [
        "", "I", "II", "III", 
        "IV", "V", "VI", 
        "VII", "VIII", 
        "IX"
    ]

    return mil[num // 1000] + cem[(num % 1000) // 100] + dez[(num % 100) // 10] + uni[num % 10]

def romano_para_inteiro(s):
    
    romano_inteiro = { 'I': 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000 }
    total = 0
    x = 0

    for x in range( len(s) ):
        if x + 1 < len(s) and romano_inteiro[s[x]] < romano_inteiro[s[x + 1]]:
            total -= romano_inteiro[s[x]]

        else:
            total += romano_inteiro[s[x]]

    return total

print( inteiro_para_romano(2006) )
print( romano_para_inteiro('MMVI') )
