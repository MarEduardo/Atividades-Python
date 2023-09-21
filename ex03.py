precoProd=float(input('Digite o valor do produto abaixo \n'))
desconto=precoProd-(precoProd*0.21)
adicional=precoProd+(precoProd*0.25)
print('O preço do produto é: {} \n O preço do produto com o desconto de 21%: {} \n O preço adicional adicionado ao produto(25%) foi de: {} ' .format(precoProd, desconto, adicional))
