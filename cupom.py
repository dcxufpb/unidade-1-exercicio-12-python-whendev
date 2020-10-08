# coding: utf-8

class Endereco:
  
  def __init__(self, logradouro, numero, complemento, bairro, municipio, 
      estado, cep):
    self.logradouro = logradouro
    self.numero = numero
    self.complemento = complemento
    self.bairro = bairro
    self.municipio = municipio
    self.estado = estado
    self.cep = cep

  def validar_campos_obrigatorios(self):
    if (self.logradouro == "" or self.logradouro == None):
        raise Exception("O campo logradouro do endereço é obrigatório")

    if (self.numero == 0):
        self.numero = "s/n"
    
    if (self.municipio == "" or self.municipio == None):
        raise Exception("O campo município do endereço é obrigatório")
    
    if (self.estado == "" or self.estado == None):
        raise Exception("O campo estado do endereço é obrigatório")

  def dados_endereco(self):
      # Implemente aqui
    self.validar_campos_obrigatorios()
    
    _COMPLEMENTO = " " + self.complemento if self.complemento else ""

    _BAIRRO = self.bairro + " - " if self.bairro else ""

    _CEP = "CEP:" + self.cep if self.cep else ""

    _NUMERO =  self.numero if self.numero else "s/n"

    return f'''{self.logradouro}, {_NUMERO}{_COMPLEMENTO}
{_BAIRRO}{self.municipio} - {self.estado}
{_CEP}'''

class Loja:
  
  def __init__(self, nome_loja, endereco, telefone, observacao, cnpj, 
      inscricao_estadual):
    self.nome_loja = nome_loja
    self.endereco = endereco
    self.telefone = telefone
    self.observacao = observacao
    self.cnpj = cnpj
    self.inscricao_estadual = inscricao_estadual

  def validar_campos_obrigatorios(self):
    if (self.nome_loja == "" or self.nome_loja == None):
        raise Exception("O campo nome da loja é obrigatório")
    
    if (self.cnpj == "" or self.cnpj == None):
        raise Exception("O campo CNPJ da loja é obrigatório")
    
    if (self.inscricao_estadual == "" or self.inscricao_estadual == None):
        raise Exception("O campo inscrição estadual da loja é obrigatório")

  def dados_loja(self):
    # Implemente aqui
    self.validar_campos_obrigatorios()

    _TELEFONE = ""
    
    if(self.endereco.cep):
      _TELEFONE = " Tel " + self.telefone if self.telefone else ""
    else:
      _TELEFONE = "Tel " + self.telefone if self.telefone else ""

    _OBSERVACAO = self.observacao if self.observacao else ""

    show = f'''{self.nome_loja}
{self.endereco.dados_endereco()}{_TELEFONE}
{_OBSERVACAO}
CNPJ: {self.cnpj}
IE: {self.inscricao_estadual}'''
    return show
