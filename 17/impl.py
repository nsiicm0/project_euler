import math
from functools import reduce
def round_base(x): 
    ''' Will return magnitude of number (i.e. 1, 1000, 1000000, and so on)
    '''
    if x < 0: 
        return 0 
    elif x == 0: 
        return 0 
    return 10**(3*(math.floor(math.log10(x)) // 3))

def wordify(n: str) -> list:
    try:
        int(n)
    except ValueError:
        raise AssertionError('Non int provided')
    numbers = {'0':'Zero','1':'One','2':'Two','3':'Three','4':'Four','5':'Five','6':'Six','7':'Seven','8':'Eight','9':'Nine','10':'Ten',
'11':'Eleven','12':'Twelve','13':'Thirteen','14':'Fourteen','15':'Fifteen','16':'Sixteen','17':'Seventeen','18':'Eighteen',
'19':'Nineteen','20':'Twenty','30':'Thirty','40':'Forty','50':'Fifty','60':'Sixty','70':'Seventy','80':'Eighty','90':'Ninety',
'100':'Hundred','1000':'Thousand','1000000':'Million','1000000000':'Billion','1000000000000':'Trillion'}
    representation = []
    if int(n) <= 20:
        return [numbers[n]]
    skip_next = False
    for i in range(len(n)):
        if skip_next:
            skip_next = False
            continue
        _position_number_repr = n[i]+('0'*(len(n)-i-1)) 
        _position_number = int(_position_number_repr) 
        _magnitude_number = round_base(_position_number) 
        if _magnitude_number == 0: 
            if (len(n)-i)%3 == 0 and representation[-1] not in ['Thousand', 'Million','Billion','Trillion']:
                representation.append(numbers[repr(1000**((len(n)-i) // 3))])
            continue 
        _order_number = _position_number // _magnitude_number 
        if _order_number // 100 > 0: 
            _hundreds = _order_number // 100 
            representation.append(numbers[repr(_hundreds)])
            representation.append(numbers[repr(_order_number // _hundreds  if _order_number % 100 == 0 else (_order_number % 100) // _hundreds)])
            #magnitude number
        else: 
            if _order_number == 10:
                # handling teen cases
                skip_next = True
                _compound_repr = repr(_order_number // 10)+n[i+1]
                representation.append(numbers[_compound_repr])
                if i+1 != len(n)-1 and (len(n)-i-1) % 3 == 1: 
                    representation.append(numbers[repr(_magnitude_number)]) 
            else:
                representation.append(numbers[repr(_order_number)])
        if _magnitude_number > 1 and (len(n)-i) % 3 == 1: 
            representation.append(numbers[repr(_magnitude_number)]) 
    return representation

t = int(input().strip())
for _ in range(t):
    n = input().strip()
    representation = wordify(n)
    print(' '.join(representation))
    #print(reduce(lambda x,y: x+y, map(len, representation)))