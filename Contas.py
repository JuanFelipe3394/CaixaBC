import json
import re
class Contas:
  def __init__(self):
    self.nomes = {}
    self.cpfs = {}
    self.macs = {}
    self.cods = []
    self.ativado = {}

  def gerarCOD(self, nome):
    from random import randint
    
    tam = len(nome)
    cod = randint(0, tam * tam)
    if(cod not in self.cods):
      self.cods.append(cod)
      return cod
    else:
      while(cod not in self.cods):
        cod = cod + 1
      return cod

  def MACs(self, mac):
    formato = ['a','b','c','d','e','f','0','1','2','3','4','5','6','7','8','9']
    #x = input('Digite seu Mac: ')
    if(len(mac) != 12):
      print('tamanho inválido')
      return False
    elif(not(all(mac for c in formato))):
      print('Formato inválido!')
      return False
    elif(mac in self.macs):
      print('Já possuimos esse cadastro!')
      return False
    else:
      print('MAC válido!')
      return True 

  def CPFs(self, cpf):
    formato = ['0','1','2','3','4','5','6','7','8','9']
    #x = input('Digite seu cpf: ')
    if(len(cpf) != 11):
      print('tamanho inválido')
      return False
    elif(not(all(cpf for c in formato))):
      print('Formato inválido!')
      return False
    elif(cpf in self.cpfs):
      print('Já possuimos esse cadastro!')
      return False
    else:
      print('cpf válido!')
      return True

  def inserir(self):
    mac = input("Digite seu mac.").lower()
    if(self.MACs(mac) == False):
      print("Error ao cadastrar.")
    else:
      nome = input("Digite o seu nome.")
      cod = self.gerarCOD(nome)
      cpf = input("Digite seu cpf.").lower()
      if(self.CPFs(cpf) == False):
        print("Error ao cadastrar CPF.")
      else:
        self.macs.setdefault(cod, mac)
        self.cpfs.setdefault(cod, cpf)
        self.nomes.setdefault(cod, nome)
        ativar = input("Ativar conta?").lower()
        if(ativar == "sim"):
          self.ativado.setdefault(cod, True)
        else:
          self.ativado.setdefault(cod, False)
        print("Cadastro realizado.")
        print("Cod de ID  = ", cod)
  
  def listar(self):
    print(self.nomes)
    print(self.cpfs)
    print(self.macs)
    print(self.ativado)
  
  def temCadastro(self):
    cod = int(input("Digite o cod de ID."))
    if(cod not in self.cods):
      print("Cod errado.")
    else:
      mac = input("Digite o mac para consulta.").lower()
      if(mac not in self.macs):
        print("Mac inexistente.")
      else:
        print("O mac ", mac, " possui cadastro.")
  
  def Excluir(self):
    cod = int(input("Digite o cod para excluir a conta."))
    if(cod not in self.cods):
      print("Cod de ID errado.")
    else:
      if(self.ativado.get(cod) == False):
        self.cods.remove(cod)
        self.macs.pop(cod)
        self.nomes.pop(cod)
        self.cpfs.pop(cod)
        self.ativado.pop(cod)
      else:
        print("Desative a conta")
  
  def Mudar(self):
    cod = int(input("Digite o cod para ativar/desativar a conta."))
    if(cod not in self.cods):
      print("Cod de ID errado.")
    else:
      if(self.ativado.get(cod) == False):
        self.ativado[cod] = True
        print("Ativado.")
      else:
        self.ativado[cod] = False
        print("Desativado.")

  def Atualizar(self):
    cod = int(input("Digite o cod."))
    if(cod not in self.cods):
      print("Código inexistente")
    else:
      mac = input("Digite o novo mac")
      if(self.MACs(mac) == False):
        print("Error ao verificar MAC")
      else:
        self.macs[cod] = mac
  def Exportar(self):

    arq = open('exportados.txt', 'w')
    form = str(self.nomes) +"\n"+ str(self.cpfs) +"\n" + str(self.macs)+"\n" + str(self.cods) + "\n" + str(self.ativado)
    arq.write(form)
    arq.close
  
  def Importar(self):
    arq = open('importar.txt', 'r')
    lista = arq.read()
    lista.split()
    print(lista)
    self.nomes = lista[0]
    self.cpfs = lista[1]
    self.macs = lista[2]
    self.cods = lista[3]
    self.ativado = lista[4]