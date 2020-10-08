# coding: utf-8

import departamento
import pytest

def verifica_campo_obrigatorio_objeto(mensagem_esperada, departamento):
    with pytest.raises(Exception) as excinfo:
        departamento.dados_departamento()
    the_exception = excinfo.value
    assert mensagem_esperada == str(the_exception)

# Todas as variaveis preenchidas

NOME_COORDENADOR = "whendel"
CPF = "703.917.760-96"
IDADE = 21
NOME_DEPARTAMENO = "departamento-01"
LOCALIZACAO = "Local-01"
SIGLA = "WSM-01"


COORDENADOR_COMPLETO = departamento.Coordenador(NOME_COORDENADOR, CPF, IDADE)

DEPARTAMENTO_COMPLETO = departamento.Departamento(NOME_DEPARTAMENO, SIGLA, LOCALIZACAO, COORDENADOR_COMPLETO)

TEXTO_ESPERADO_DEPARTAMENTO_COMPLETO = """COORDENADOR:
Nome: whendel
Cpf: 703.917.760-96
Idade: 21
DEPARTAMENTO:
Nome: departamento-01
Sigla: WSM-01
Localizacao: Local-01"""

def test_departamento_completo():
    assert (
        DEPARTAMENTO_COMPLETO.dados_departamento() == TEXTO_ESPERADO_DEPARTAMENTO_COMPLETO
    )

COORDENADOR_NOME_NULO = departamento.Coordenador(None, CPF, IDADE)

DEPARTAMENTO_COORDENADOR_NOME_NULO = departamento.Departamento(NOME_DEPARTAMENO, SIGLA, LOCALIZACAO, COORDENADOR_NOME_NULO)

DEPARTAMENTO_NOME_NULO = departamento.Departamento(None, SIGLA, LOCALIZACAO, COORDENADOR_COMPLETO)

TEXTO_ESPERADO_DEPARTAMENTO_NOME_NULO = """O campo nome do departamento é obrigatório"""

TEXTO_ESPERADO_COORDENADOR_NOME_NULO = """O campo nome do coordenador é obrigatório"""

def test_valida_nome():
    verifica_campo_obrigatorio_objeto(TEXTO_ESPERADO_DEPARTAMENTO_NOME_NULO,
                                      DEPARTAMENTO_NOME_NULO)
    verifica_campo_obrigatorio_objeto(TEXTO_ESPERADO_COORDENADOR_NOME_NULO,
                                      DEPARTAMENTO_COORDENADOR_NOME_NULO)

