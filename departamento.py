# coding: utf-8

class Coordenador:

  def __init__(self, nome, cpf, idade):
    self.nome = nome
    self.cpf = cpf
    self.idade = idade

  def validar_campos_obrigatorios(self):
    if not self.nome:
        raise Exception("O campo nome do coordenador é obrigatório")

    if not self.cpf:
        raise Exception("O campo cpf do coordenador é obrigatório")
    
    if not self.idade:
        raise Exception("O campo idade do coordenador é obrigatório")

  def dados_coordenador(self):
    self.validar_campos_obrigatorios()

    return f'''Nome: {self.nome}\nCpf: {self.cpf}\nIdade: {self.idade}'''

class Departamento:
  
  def __init__(self, nome, sigla, localizacao, coordenador):
    self.nome = nome
    self.sigla = sigla
    self.localizacao = localizacao
    self.coordenador = coordenador
  
  def validar_campos_obrigatorios(self):
    if not self.nome:
        raise Exception("O campo nome do departamento é obrigatório")

    if not self.sigla:
        raise Exception("O campo sigla do departamento é obrigatório")
    
    if not self.localizacao:
        raise Exception("O campo localizacao do departamento é obrigatório")
    
    if not self.coordenador:
        raise Exception("O campo coordenador do departamento é obrigatório")

  def dados_departamento(self):
    self.validar_campos_obrigatorios()

    return f'''COORDENADOR:\n{self.coordenador.dados_coordenador()}\nDEPARTAMENTO:\nNome: {self.nome}\nSigla: {self.sigla}\nLocalizacao: {self.localizacao}'''
