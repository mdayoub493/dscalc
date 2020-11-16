#importando um arquivo especifico
from dscalc.lib import sum, subtract

#importando uma funcao especifica no jupyter
#no terminal, roda pip install . (so vai funcionar se eu estiver na mesma pasta que estiver setup.py)
#from dscalc.lib import sum 

#nos testes:
# 1. a gente escolhe inputs dessa funcao (qq input que a gente sabe qual vai ser o output)
# 2. deve saber qual eh o output
# 3. deve ver se o que a gente consegue eh o esperado

def test_sum():
    a, b = 2, 2
    esperado = 4
    conseguiu = sum(a,b)
    assert conseguiu == esperado

    #ou
    c, d = 5, 0
    expected = 5
    got = sum(c,d)
    assert got == expected


def test_subtract():
    a, b = 2, 2
    esperado = 0
    conseguiu = subtract(a,b)
    assert conseguiu == esperado

    c, d = 5, 0
    expected = 5
    got = subtract(c,d)
    assert got == expected


#qdo projeto passa no test, posso rodar pip install .
