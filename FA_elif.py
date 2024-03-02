FA = input('what is FA number?')
FA = float(FA)
if FA == 1.9:
    print('perfect')
elif FA > 1.98 or FA < 1.82:
    print('reject')
else: 
    print('acceptable')