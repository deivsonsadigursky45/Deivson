clear 
clc
disp('Discente: Deivson Sadigursky ')
disp('Inform�tica aplicada a Engenharia')
disp('Dimensionamento de reservat�rios ')
q= input('Digite o consumo per capita : ');
pop= input('Digite o popula��o : ');
k= 1.2;
cd=(k*pop*q);
disp (' O consumo di�rio � ');
disp (cd);
tr=2;
vr= (cd* tr) ;
disp ('O volume de reserva��o � ');
disp (vr);
vi= ( (vr*25)/100 );
disp ('O volume de inc�ndio � ');
disp (vi);
vt=(vr+vi);
disp ('O volume total � ');
disp (vt);
vrs=(((vr*2)/5)+vi);
hs=2.5;
ls=(sqrt(((vrs/1000)/hs)/0.75));
bs=(0.75*ls);
fprintf (' O volume do reservat�rio superior,ter� uma de base %1.2f m, um comprimento %1.2f m , ser� igual a %1.2f l.', bs,ls,vrs);
vri=((vr*3)/5);
hi=1.5;
bi=(sqrt(((vri/1000)/hi)/0.75));
li=(0.75*bi);
fprintf (' Enquanto o volume do reservat�rio inferior,ter� uma de base %1.2f m, um comprimento %1.2f m , ser� igual a %1.2f l.', bi,li,vri);
