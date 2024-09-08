print('Digite suas informções abaixo para verificarmos detalhes do seu alistamento Militar')
nome = str(input('Digite seu nome: ')).strip().capitalize()
print('Olá {}, digite seu nascimento abaixo'.format((nome)))
nascimento = int(input('Ano de nascimento: '))

print(''' Digite uma das opções abaixo:
      [1] Já fez o alistamento militar
      [2] Ainda não fiz o alistamento militar ''')
opçao = int(input('Digite: '))

idade = 2024 - nascimento

if opçao == 1:
    print('{} pela opção que você nos informou, você tem {} anos e já esta alistado. Entre no site do Exercito brasileiro abaixo para saber como está os detalhes do seu alistamento.'.format((nome), (idade)))
    print('Entre no site https://www.eb.mil.br/ e verifique!')
if opçao == 2:
    if idade == 18:
        print('{} você tem {} anos, chegou a hora de se alistar!'.format((nome), (idade)))
        print('Entre em https://www.eb.mil.br/ para se alistar o quanto antes')
    elif idade >= 19:
        devendo = idade - 18
    #devendo repersenta os anos que o usuario está atrasado para o alistamento# 
        alis =  2024 - devendo
        print('''{} com a sua idade de {} anos você deveria ter se alistado a {} anos atrás! Seu alistamento foi em {}.
Pelo atraso será cobrado uma multa de R$6.06
(A multa é corrigida a cada três meses, então pode haver aumento no valor!)'''.format((nome), (idade), (devendo), (alis)))
        print('Entre em https://www.eb.mil.br/ o quanto antes!')

    elif idade <= 17:
    #Anos sobrando representa quantos anos faltam para o alistamento do usuario#
        sobrando = idade - 18
        print('{} com {} anos você deve se alistar daqui {} anos'.format((nome), (idade), (sobrando)))

