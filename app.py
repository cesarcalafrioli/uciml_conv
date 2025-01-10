"""

"""
from ucimlrepo import fetch_ucirepo
import numpy as np


"""
A seção abaixo converte os dados do repositorio UCI para o formato CSV,
incluindo os nomes das variáveis. TRANSFORMAR EM UMA FUNÇÃO.
"""
print("\n")
# Tentando converter os dados do UCI para array e assim salvar em .csv
ds_id=53
repo = fetch_ucirepo(id=ds_id)

"""
print(repo.data.original)
data2 = repo.data.original

# Mesmo com o parametro .original, apenas o conteúdo das variáveis irão aparecer.
a = np.asarray(data2)
print(a)

# Transformando os headers em array para salvar no mesmo .csv
data_headers = repo.data.headers
b = np.asarray(data_headers)
print(b)

# Salvando o array no arquivo csv
# delimiter = 
# fmt -> converte o tipo de dados, integer ou string
# comments -> É preciso colocar '' para não aparecer o hash (#) no início do header.
#np.savetxt("teste.csv", a, delimiter=",", header=",".join(b) , fmt = '%s', comments='')
"""

data_headers2 = np.asarray(repo.data.headers)
print(data_headers2)

data_content = np.asarray(repo.data.original)
print(data_content)

# Salvando o array no arquivo csv
# delimiter = Strings ou caracteres que separam as colunas
# fmt -> converte o tipo de dados, integer ou string
# comments -> String que será colocado antes das colunas ou rodapés.
# É preciso colocar '' para não aparecer o hash (#) no início do header.
np.savetxt("teste.csv", data_content, delimiter=",", header=",".join(data_headers2) , fmt = '%s', comments='')
