i =0
guest = 0
save = input('please enter input')
while i !='BILL':
    i = input('please enter a input')
    if i.lower()=='bill':
        break
    guest = guest+int(i.split('ADD_GUESTS ')[1])
    
    
ratio = save.split('ALLOT_WATER')[1].strip()
if ':' in ratio:
    bhk,ratio = ratio.split()
    if int(bhk)==2:
        assin_water = 900
    elif int(bhk)==3:
        assin_water = 1500

a,b = ratio.split(':') 
c = int(assin_water/(int(a)+int(b)))
corp_water = c*int(a)
borewell_water = c*int(b)
apartment_rupess = (corp_water*1)+int(borewell_water*1.5)
tanker_water = guest*300
if tanker_water>3000:
    price =  1000+3000+7500
    total_price = int((tanker_water-3000)*8+price)
elif tanker_water>1500:
    price =  1000+3000
    total_price = int((tanker_water-1500)*5+price)
elif tanker_water>500:
    price =  1000
    total_price = int((tanker_water-500)*3+price)
elif tanker_water<500:
    total_price = int((500-tanker_water)*2)
    
total_price = total_price+apartment_rupess
    
total_water = tanker_water+corp_water+borewell_water
print(total_water,total_price)


