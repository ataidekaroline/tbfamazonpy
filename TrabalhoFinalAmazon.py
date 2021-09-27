#1 - Cadastrar novos clientes
class cliente:
  nome:None
  cpf:None
  senha:None
  email:None
  limite_credito:None

  #lista para armazenar as variáveis 'cliente'
clientes = []

#1ª função do menu
def cadastro():
  global clienteN
  clienteN = cliente() 
  clienteN.nome = input("Nome : ")
  clienteN.cpf = int(input("CPF : "))
  clienteN.senha = input("Senha: (6 dígitos) :"[:6])
  clienteN.email = input("Email : ")
  clienteN.limite_credito = 1000
  # Adiciona os novos usuários a uma lista de clientes
  clientes.append(clienteN.nome)
  clientes.append(clienteN.senha)
  clientes.append(clienteN.limite_credito)
  #verifica se o cpf já foi cadastrado
  if clienteN.cpf in clientes :
    print("CPF já cadastrado")
    return
  elif clienteN.cpf not in clientes :
    clientes.append(clienteN.cpf)    
  elif clienteN.email in clientes :
    print("Email já cadastrado")
  elif clienteN.email not in clientes :
    clientes.append(clienteN.email)
  #verifica se o email contém o caracter @
  def email_valido(simbolos_permitidos) :
    letras_min = [chr(x) for x in range(ord('a'), ord('z') + 1)]
    simbolos_permitidos = [i for i in clienteN.email if i not in letras_min]
    if simbolos_permitidos == ['@', '.'] :
      print("Email válido")
      return True
    else :
      print("Email inválido")
      return False
# agora começarei a validação de cpf por cliente
  def cpf_valido(numbers):
# valida os números do CPF e ignora outros caracteres
    cpf = [int(char) for char in numbers if char.isdigit()]
#  verificar se o CPF tem 11 dígitos
    if len(cpf) != 11:
      return False
#  verificar se o CPF tem todos os números iguais, ex: 111.111.111-11
    elif cpf == cpf[::-1]:
      return False
  menu()

#verificar  para ver se o cpf já não existe no sistema
def existecpf(cpf):
  for cpf in cliente.cpf:
    if cpf["cpf"] == cpf:
      return False
    return True

#função de login - 2ª função do menu:
def login() :
  id = int(input("Digite o CPF : \n"))
  senha_ = input("Digite a senha : \n")
  if id in clientes and senha_ not in clientes :
    print("Senha errada")
  elif id not in clientes and senha_ in clientes :
    print("CPF errado")
  elif id not in clientes and senha_ not in clientes :
    print("Cliente não cadastrado")
    return cadastro()
  elif id in clientes and senha_ in clientes :
    return menu()

#cadastro dos produtos :
class produtos :
  codigo = None
  valor = None
  nome = None
  quantidade = None

lista_produtos = []
preco_produtos = []

fever_part_3_by_ateez = produtos()
fever_part_3_by_ateez.valor = 69.90
fever_part_3_by_ateez.nome = "1 - CD FEVER Part. 3 by Ateez"
lista_produtos.append(fever_part_3_by_ateez.nome)
preco_produtos.append(fever_part_3_by_ateez.valor)

fever_part_2_by_ateez = produtos()
fever_part_2_by_ateez.nome = "2 - CD FEVER Part. 2 by Ateez"
fever_part_2_by_ateez.valor = 60.0
lista_produtos.append(fever_part_2_by_ateez.nome)
preco_produtos.append(fever_part_2_by_ateez.valor)

fever_part_1_by_ateez = produtos()
fever_part_1_by_ateez.nome = "3 - CD FEVER Part. 1 by Ateez"
fever_part_1_by_ateez.valor = 55.0
lista_produtos.append(fever_part_1_by_ateez.nome)
preco_produtos.append(fever_part_1_by_ateez.valor)

treasure_epilogue_by_ateez = produtos()
treasure_epilogue_by_ateez.nome = "4 - CD Treasure Epilogue : Action to Answer by Ateez"
treasure_epilogue_by_ateez.valor = 52.0
lista_produtos.append(treasure_epilogue_by_ateez.nome)
preco_produtos.append(treasure_epilogue_by_ateez.valor)

treasure_ep_fin_by_ateez = produtos()
treasure_ep_fin_by_ateez.nome = "5 - CD Treasure EP. Fin : All to Action by Ateez"
treasure_ep_fin_by_ateez.valor = 49.90
lista_produtos.append(treasure_ep_fin_by_ateez.nome)
preco_produtos.append(treasure_ep_fin_by_ateez.valor)

treasure_ep_3_by_ateez = produtos()
treasure_ep_3_by_ateez.nome = "6 - CD Treasure EP. 3 : One to All by Ateez"
treasure_ep_3_by_ateez.valor = 44.90
lista_produtos.append(treasure_ep_3_by_ateez.nome)
preco_produtos.append(treasure_ep_3_by_ateez.valor)

treasure_ep_2_by_ateez = produtos()
treasure_ep_2_by_ateez.nome = "7 - CD Treasure EP. 2 : Zero to One by Ateez"
treasure_ep_2_by_ateez.valor = 44.90
lista_produtos.append(treasure_ep_2_by_ateez.nome)
preco_produtos.append(treasure_ep_2_by_ateez.valor)

treasure_ep_1_by_ateez = produtos()
treasure_ep_1_by_ateez.nome = "8 - CD Treasure EP. 1 : All to Zero by Ateez"
treasure_ep_1_by_ateez.valor = 44.90
lista_produtos.append(treasure_ep_1_by_ateez.nome)
preco_produtos.append(treasure_ep_1_by_ateez.valor)

dystopia_lose_by_dreamcatcher = produtos()
dystopia_lose_by_dreamcatcher.nome = "9 - CD Dystopia : Lose Myself by Dreamcatcher"
dystopia_lose_by_dreamcatcher.valor = 49.90
lista_produtos.append(dystopia_lose_by_dreamcatcher.nome)
preco_produtos.append(dystopia_lose_by_dreamcatcher.valor)

dystopia_road_by_dreamcatcher = produtos()
dystopia_road_by_dreamcatcher.nome = "10 - CD Dystopia : Road to Utopia by Dreamcatcher"
dystopia_road_by_dreamcatcher.valor = 49.90
lista_produtos.append(dystopia_road_by_dreamcatcher.nome)
preco_produtos.append(dystopia_road_by_dreamcatcher.valor)

cd_chromatica_by_lady_gaga= produtos()
cd_chromatica_by_lady_gaga.valor= 45.0
cd_chromatica_by_lady_gaga.nome= "11 - CD Chromatica by Lady Gaga"
lista_produtos.append(cd_chromatica_by_lady_gaga.nome)
preco_produtos.append(cd_chromatica_by_lady_gaga.valor)

cd_future_nostalgia_by_dua_lipa= produtos()
cd_future_nostalgia_by_dua_lipa.valor= 40.0
cd_future_nostalgia_by_dua_lipa.nome= "12 - CD Future Nostalgia by Dua Lipa"
lista_produtos.append(cd_future_nostalgia_by_dua_lipa.nome)
preco_produtos.append(cd_future_nostalgia_by_dua_lipa.valor)

cd_anti_by_rihanna= produtos()
cd_anti_by_rihanna.valor= 85.0
cd_anti_by_rihanna.nome= "13 - CD Anti by Rihanna"
lista_produtos.append(cd_anti_by_rihanna.nome)
preco_produtos.append(cd_anti_by_rihanna.valor)

cd_25_by_adele= produtos()
cd_25_by_adele.valor= 50.0
cd_25_by_adele.nome= "14 - CD 25 by Adele"
lista_produtos.append(cd_25_by_adele.nome)
preco_produtos.append(cd_25_by_adele.valor)

cd_dangerous_woman_by_ariana_grande= produtos()
cd_dangerous_woman_by_ariana_grande.valor= 65.0
cd_dangerous_woman_by_ariana_grande.nome= "15 - CD Dangerous Woman by Ariana Grande"
lista_produtos.append(cd_dangerous_woman_by_ariana_grande.nome)
preco_produtos.append(cd_dangerous_woman_by_ariana_grande.valor)

cd_plastic_hearts_by_miley_cyrus= produtos()
cd_plastic_hearts_by_miley_cyrus.valor= 60.0
cd_plastic_hearts_by_miley_cyrus.nome= "16 - CD Plastic Hearts by Miley Cyrus"
lista_produtos.append(cd_plastic_hearts_by_miley_cyrus.nome)
preco_produtos.append(cd_plastic_hearts_by_miley_cyrus.valor)

cd_positions_by_ariana_grande= produtos()
cd_positions_by_ariana_grande.valor= 70.0
cd_positions_by_ariana_grande.nome= "17 - CD Positions by Ariana Grande"
lista_produtos.append(cd_positions_by_ariana_grande.nome)
preco_produtos.append(cd_positions_by_ariana_grande.valor)

cd_after_hours_by_the_weeknd= produtos()
cd_after_hours_by_the_weeknd.valor= 87.0
cd_after_hours_by_the_weeknd.nome= "18 - CD After Hours by The Weeknd"
lista_produtos.append(cd_after_hours_by_the_weeknd.nome)
preco_produtos.append(cd_after_hours_by_the_weeknd.valor)

cd_high_as_hope_by_florence_and_the_machine= produtos()
cd_high_as_hope_by_florence_and_the_machine.valor= 78.0
cd_high_as_hope_by_florence_and_the_machine.nome= "19 - CD High as Hope by Florence and the Machine"
lista_produtos.append(cd_high_as_hope_by_florence_and_the_machine.nome)
preco_produtos.append(cd_high_as_hope_by_florence_and_the_machine.valor)

cd_high_as_hope_by_florence_and_the_machine= produtos()
cd_high_as_hope_by_florence_and_the_machine.valor= 78.0
cd_high_as_hope_by_florence_and_the_machine.nome= "20 - CD High as Hope by Florence and the Machine"
lista_produtos.append(cd_high_as_hope_by_florence_and_the_machine.nome)
preco_produtos.append(cd_high_as_hope_by_florence_and_the_machine.valor)

#lista dos produtos --- 1ª função do menu
def listar_produtos() :
  x = 0
  while x < 20 :
    print(lista_produtos[0 + x], "-", "R$", preco_produtos[0 + x])
    x += 1
    
#criando uma função de compra - 3ª função do menu
def comprar_produtos() :
  listar_produtos()
  item = -1
  valorTotal = 0.0
  global carrinho 
  while clienteN.limite_credito <= 1000 and item != 0: #verificar se o usuário informou zero
    item = int(input("Insira o código do produto (1 a 20) \nCaso queira parar de comprar digite 0. \n"))
    if item != 0 :
      quantia = int(input("Insira quantas unidades do produto você deseja \n"))
      valorTotal += (preco_produtos[item -1] * quantia)
      produtoAdicionado = produtos()
      produtoAdicionado.codigo = item
      produtoAdicionado.quantidade = quantia
      produtoAdicionado.valor = preco_produtos[0]
      carrinho.append(produtoAdicionado)
  print("Valor total :", valorTotal)
  return menu()

#4ª função menu 
def mostrarcarrinho() :
  global carrinho
  somador = 0
  print("Produtos adicionados : \n")
  for x in range (0,len(carrinho)):
    print("Código do produto : ",carrinho[x].codigo,";","Quantidade : ",carrinho[x].quantidade,";",carrinho[x].valor)
    somador += carrinho[x].quantidade * carrinho[x].valor
  print("Total da compra : ", somador )
  return menu()

#5ª função do menu
def pagarfatura() :
  somador = 0
  pagarei = input("Deseja prosseguir com o pagamento ?\n Se sim digite 's'\n Se não digite 'n'. \n")
  if pagarei == 's' or pagarei == 'S' :
    saldo = clienteN.limite_credito - somador
    confirma = input("Digite a senha para aprovar a compra : ")
    if confirma == cliente.senha :
      if clienteN.limite_credito == 0 :
        print("Você não possui crédito suficiente")
      elif clienteN.limite_credito < somador :
        print("Você não possui crédito suficiente")
      elif clienteN.limite_credito >= somador :
        clienteN.limite_credito = saldo
        print("Pagamento efetuado")
        novoLimite = 1000
        clientes.append(novoLimite)
  elif pagarei == 'n' or pagarei == 'N' :
    return menu()

def menu():
    #Mostra as opçoes de ações do sistema
    escolha = int(input("escolha uma opção: \n 1 - cadastro. \n 2 - login. \n 3 - comprar produto. \n 4 - mostrar carrinho \n 5 - pagar a fatura. \n"))
    if(escolha == 1):
      cadastro()
    elif(escolha == 2):
      login()
    elif(escolha == 3):
      comprar_produtos()
    elif(escolha == 4):
      mostrarcarrinho()
    elif(escolha == 5):
      pagarfatura()
    else:
      return input("escolha uma opção válida")
    return 0
carrinho = []
menu()