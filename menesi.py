def nolasaDrukaDatni(nosauk):
  datne = open(nosauk)
  dati = datne.readline()
  rinda = dati.split(" ")
  print(rinda)
  datne.close()
#..
def raksta(nosauk, veids):
  with open('info.txt', veids) as datne:
    for vards in menesi:
      datne.write(vards)
      datne.write(' ')
#..
menesi = ['janvāris', '31', 'februāris', '28', 'aprīlis', '30'] 
#..
a=open("info.txt",'w')
#raksta('info.txt', 'w')
 
print('nolasa un izdrukā ierakstīto ar w')
nolasaDrukaDatni('info.txt')

b=open("info.txt",'a')
#raksta('info.txt', 'a')
#..s
print('nolasa un izdrukā ierakstīto ar a')
nolasaDrukaDatni('info.txt')
