numero = '1123123'
print('O programa vai transcrever um numero digitado que tenha até 4 casas')
cont = 5
while len(numero) > 4:
    numero = input('Digite um numero : ')
    if len(numero) > 4:
        print('Numero Invalido!')

numero = numero.zfill(4)

if numero[0] == '1':
    print('Mil ',end='')

if numero[0] == '2':
    print('Dois Mil ',end='')

if numero[0] == '3':
    print('Três Mil ',end='')

if numero[0] == '4':
    print('Quatro Mil ',end='')

if numero[0] == '5':
    print('Cinco Mil ',end='')

if numero[0] == '6':
    print('Seis Mil ',end='')

if numero[0] == '7':
    print('Sete Mil ',end='')

if numero[0] == '8':
    print('Oito Mil ',end='')

if numero[0] == '9':
    print('Nove Mil ',end='')

if numero[2] == '0' and numero[3] == '0':
    print('e ',end='')

    if numero [1] == '1':
        print('Cem',end='')

if numero[1] == '1':
    print('Cento ',end='')

elif numero[1] == '2':
    print('Duzentos ',end='')

elif numero[1] == '3':
    print('Trezentos ',end='')

elif numero[1] == '4':
    print('Quatrocentos ',end='')

elif numero[1] == '5':
    print('Quinhentos ',end='')

elif numero[1] == '6':
    print('Quinhentos ',end='')

elif numero[1] == '7':
    print('Seiscentos ',end='')

elif numero[1] == '8':
    print('Setecentos ',end='')

elif numero[1] == '9':
    print('Quatrocentos ',end='')

if numero[0] != '0' or numero[1] != '0':
    if numero[2] != '0' or numero[3] != '0':
        print('e ',end='')

if numero[2] == '1':

    if numero[3] == '0':
        print('Dez',end='')

    if numero[3] == '1':
        print('Onze',end='')

    if numero[3] == '2':
        print('Doze',end='')

    if numero[3] == '3':
        print('Treze',end='')

    if numero[3] == '4':
        print('Catorze',end='')

    if numero[3] == '5':
        print('Quinze',end='')

    if numero[3] == '6':
        print('Dezesseis',end='')

    if numero[3] == '7':
        print('Dezesete',end='')

    if numero[3] == '8':
        print('Dezoito',end='')

    if numero[3] == '9':
        print('Dezenove',end='')

elif numero[2] == '2':
    print('Vinte ',end='')

elif numero[2] == '3':
    print('Trinta ',end='')

elif numero[2] == '4':
    print('Quarenta ',end='')

elif numero[2] == '5':
    print('Cinquenta ',end='')

elif numero[2] == '6':
    print('Sessenta ',end='')

elif numero[2] == '7':
    print('Setenta ',end='')

elif numero[2] == '8':
    print('Oitenta ',end='')

elif numero[2] == '9':
    print('Noventa ',end='')

if numero[2] != '1' and numero[2] != '0' and numero[3] != '0':

    print('e ',end='')

if numero[2] != '1' and numero[3] != '0':

    if numero[3] == '1':
        print('Um',end='')

    if numero[3] == '2':
        print('Dois',end='')

    if numero[3] == '3':
        print('Três',end='')

    if numero[3] == '4':
        print('Quatro',end='')

    if numero[3] == '5':
        print('Cinco',end='')

    if numero[3] == '6':
        print('Seis',end='')

    if numero[3] == '7':
        print('Sete',end='')

    if numero[3] == '8':
        print('Oito',end='')

    if numero[3] == '9':
        print('Nove',end='')



input('\n\n\nENTER PARA FINALIZAR!!!')

