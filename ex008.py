# valida o número do cpf com pontos e hífens
import re
cpf = str(input('Entre com o número do CPF, com pontos e hífen: \n'))
if re.search('\d{3}.\d{3}.\d{3}-\d{2}', cpf):
    print('Número CPF validado')
else:
    print('Número do CPF fora do padrão')
input('Pressione ENTER para sair...')
