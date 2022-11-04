print('Discente: Deivson Sadigursky')
print('Informática aplicada a Engenharia')
print('Dimnesionamento de um reservatório')


q= int(input('Digite o consumo per capita'))
pop = int(input('Digite a população'))
print('Constante k=1,2')
k=(1.2);
cd = k * q * pop
print('Consumo diário:cd = k * q * pop');
print(cd);


tr=2;
vr= cd* tr
print('Volume de reservação: vr= cd* tr')
print(vr);


vi=((vr*25)/100)
print('Volume de incêndio: vi=((vr*25)/100)')
print(vi);

vt=(vr+vi);
print('O volume total é: vt=(vr+vi)');
print(vt);


vrs=(((vr*2)/5)+vi);
hs=2.5;
ls=int((((vrs/1000)/hs)/0.75)**0.5);
bs=(0.75*ls);
print (' O volume do reservatório superior é ');
print (vrs)

print (' Com base ')
print(round(bs,2))
print('Com comprimento')
print(round(ls,2))
print('e altura')
print(hs)


vri=((vr*3)/5);
hi=1.5;
bi=int((((vri/1000)/hi)/0.75)**0.5);
li=(0.75*bi);
print (' O volume do reservatório inferior é ');
print(vri)


print (' Com base ')
print(round(bi,2))
print('Com comprimento')
print(round(li,2))
print('e altura')
print(hi)
