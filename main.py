from Contas import Contas
obj = Contas()
#obj.inserir()
t = True
while(t):
  print ("Menu")
  print ("1 Cadastrar")
  print ("2 Consultar")
  print ("3 Listar")
  print ("4 Remover")
  print ("5 Atualizar")
  print ("6 Ativar")
  print ("7 Impotar")
  print ("8 Exportar")
  print ("9 Sair")

  opc = input("Digite a opção.").lower()

  menu = ["1" ,"cadastrar", "2", "consultar", "3", "listar", "4", "atualizar", "5", "remover", "atualizar", "6", "ativar", "7", "sair", "importar", "8", "exportar", "9"]

  if(opc not in menu):
    print("Opção inválida")
  else:
    if(opc == "1" or opc == "cadastrar"):
      obj.inserir()
    elif(opc == "2" or opc == "consultar"):
      obj.temCadastro()
    elif(opc == "3" or opc == "listar"):
      obj.listar()
    elif(opc == "4" or opc == "remover"):
      obj.Excluir()
    elif(opc == "5" or opc == "atualizar"):
      obj.Atualizar() 
    elif(opc == "6" or opc == "ativar"):
      obj.Mudar()
    elif(opc == "7" or opc == "impotar"):
      obj.Importar()
    elif(opc == "8" or opc == "exportar"):
      obj.Exportar()
    else:
      print("atualizando!")
      t = False
