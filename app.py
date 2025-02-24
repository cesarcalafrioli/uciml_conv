"""

Tecnologias utilizadas
ucimlrepo
numpy
"""
from ucimlrepo import fetch_ucirepo
import streamlit as st
import numpy as np


REPOSITORY_ID = 53
DATASET_FILE = 'iris.csv'
PATH_CONV_FILE = 'files/conv'


class Uci_Repo:
    def __init__(self, repo_id, repo_name):
        """Construtor da classe Uci_Repo"""
        self._repo_id = repo_id
        self._repo_name = repo_name
    
def uci_repository_name(REPOSITORY_ID):
    """
    Recupera o nome do repositório UCI através do ID informado pelo
    usuário. Caso o id seja 0, o id será solicitado novamente.
    """

    if REPOSITORY_ID == 0:
        return "Informe o id do repositorio!"
    
    repo = fetch_ucirepo(id=REPOSITORY_ID)
    return repo.metadata.name

def uci_conv(REPOSITORY_ID):
    """
    Converte o arquivo extraído do Repositório UCI para o formato CSV.
    
    Os dados do repositório UCI é primeiramente colocado na memória. Em
    seguida, tais dados são salvos em um arquivo csv atendendo aos seguin
    tes parâmetros:
    - delimiter = Strings ou caracteres que separam as colunas
    - fmt = Tipo de dados a ser convertido ( Integer ou String )
    - comments = String que será colocado antes das colunas ou rodapés.
    """

    repo = fetch_ucirepo(id=REPOSITORY_ID)

    data_headers = np.asarray(repo.data.headers)
    data_content = np.asarray(repo.data.original)

    # Salvando o array no arquivo csv
    # delimiter = Strings ou caracteres que separam as colunas
    # fmt -> converte o tipo de dados, integer ou string
    # comments -> String que será colocado antes das colunas ou rodapés.
    # É preciso colocar '' para não aparecer o hash (#) no início do header.
    np.savetxt(DATASET_FILE, data_content, delimiter=",", header=",".join(data_headers) , fmt = '%s', comments='')



repo_input_id = st.number_input("Id do repositório : ", 0)
st.write("Id do repositório : ", str(repo_input_id))
st.write("Nome do repositório : ", uci_repository_name(repo_input_id))

if repo_input_id != 0:
    if st.button('Convert to CSV file'):
        uci_conv(repo_input_id)
