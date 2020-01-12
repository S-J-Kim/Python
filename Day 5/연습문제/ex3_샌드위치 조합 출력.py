bread = ['whole', 'wheat', 'white']
meat = ['meatball', 'sausage', 'chicken']
veg = ['lettuce', 'tomato', 'cucumber']
sauce = ['mayo', 'mustard', 'chili']

i = 1

for bread_name in bread:
    for meat_name in meat:
        for veg_name in veg:
            for saue_name in sauce:
                print(f'Combination {i} : {bread_name} + {meat_name} + {veg_name} + {saue_name}')
                i += 1

h=0

j = k = l = m = 0

while j < 3:
    while k < 3:
        while l < 3:
            while m < 3:
                print(f'Combination {h+1} : {bread[j]} + {meat[k]} + {veg[l]} + {sauce[m]}')
                h += 1; m += 1;
            l += 1; m = 0
        k += 1; l = 0; m = 0
    j += 1; k = 0; l = 0; m = 0
    
