
print("Trabalho prático de Lógica de programação e Algorítmos")
print('Nome: Thiago Levi Ramos da Costa')
print('RU: XXXXXX')
print('Questão 01')

#Entrada de dados
valorUnitarioDoProduto = float(input('Digite o valor unitário do produto: '))
quantidadeDeProdutos = int(input('Digite a Quantidade de produtos: '))

#Processamento
#A variável placeholder é apenas para informar o percentual de desconto.

if quantidadeDeProdutos >= 10 and quantidadeDeProdutos <= 99:
    descontoPorUnidade = 0.05
    placeholder = "(desconto 5%)"
elif quantidadeDeProdutos >= 100 and quantidadeDeProdutos <= 999:
    descontoPorUnidade = 0.1
    placeholder = "(desconto 10%)"
elif quantidadeDeProdutos >= 1000:
    descontoPorUnidade = 0.15
    placeholder = "(desconto 15%)"
else:
    descontoPorUnidade = 0.00
    placeholder = ""


#calculo do preço final sem desconto
valorTotalSemDesconto = quantidadeDeProdutos * valorUnitarioDoProduto
#calculo do preço final com desconto
valorTotalAposDesconto = valorTotalSemDesconto - (descontoPorUnidade * valorTotalSemDesconto)

#saida de dados
if quantidadeDeProdutos <= 9:
    print('Valor total  --> R$ {} '.format(valorTotalSemDesconto))
else:
    print('Valor total sem desconto --> R$ {:.2f} '.format(valorTotalSemDesconto))
    print("Valor Total após o desconto --> {:.2f}  {}".format(valorTotalAposDesconto, placeholder))

"""print('Valor Unitário --> {}'.format(valorUnitarioDoProduto))
    print('Desconto de --> {}'.format(descontoPorUnidade * valorTotalSemDesconto))
    print('Quantidade de Produtos --> {}'.format(quantidadeDeProdutos))
    print('Desconto por unidade --> {:.2f}'.format(descontoPorUnidade))
"""


