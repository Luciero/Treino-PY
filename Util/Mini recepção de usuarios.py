# --------- Marcar reserva ---------

# ----- Variaveis -------
clientes = [""] * 5
listinha = [0] * 5


# ----------- Funções -----------
def cadastrar():
  for i in range(5):
    if clientes[i] == "":
      print("\nDigite o nome do cliente:\n")
      nome = input()
      clientes[i] = nome
      
'''------- Funcao para pesquisa os nomes dos usuarios --------- '''

def pesquisar():
  nomeApesquisar = input('\nDigite o nome a pesquisar: ')
  for i in range(5):
    if nomeApesquisar == clientes[i]:
      print("\nNome encontrado na posição: ",i+1)
      break
  else:
    print("\nNome não encontrado!")

'''------- Funcao para excluir os usuarios --------- '''

def excluir():
  for index,i in enumerate(clientes):
    controle = int(len(i) / 2)
    listinha[index] = "{}{}{}".format(controle*"  ",index+1,controle*" ")
  print('\n',clientes)
  print(' '.join(listinha))
  nome = int(input('\nDigite o indice do usuario que deseja excluir: '))
  clientes[nome-1] = ""
  print("\nUsuario excluido com Sucesso!")

'''------- Funcao para mostrar o menu de opções --------- '''

def mostrarMenu():
  print('\n1 - Cadastrar')
  print('\n2 - Pesquisar')
  print('\n3 - Excluir\n')


def main():
  
  mostrarMenu()
  resultado = 1
  
  while resultado >= 1 and resultado <= 3:
    resultado = int(input('\nDigite a sua escolha: '))
    
    if resultado == 1:
      cadastrar()
      mostrarMenu()
    elif resultado == 2:
      pesquisar()
      mostrarMenu()
    elif resultado == 3:
      excluir()
      mostrarMenu()
    else:
      break
  
main()