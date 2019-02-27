repetir = 's'
fatura = []
total = 0
valid_preco = False

while repetir == 's':
   produto = input('Digite o nome do produto: ')

   while valid_preco == False:
       preco = input('Digite o valor do produto: ')
       try:
           preco = float(preco)

           if preco <= 0:
                print('O preço precisa ser maior que zero')
                print('-------------------------------------------------------------------------------')
           else:
                valid_preco = True
       except:
           print("Formato de preço invalido. Use apenas numeros e separe os centavos com '.' ")
           print('------------------------------------------------------------------------------------')
   fatura.append([produto,preco])
   total += preco
   valid_preco = False
   repetir = input('Deseja comprar mais algum produto? ( S ou N )'.lower())
   print('--------------------------------------------------------------------------------------------')
for i in fatura:
    print(i[0],'=>',i[1])

print('-----------------------------------------------------------------------------------------------')
print('O valor da fatura é:',total)