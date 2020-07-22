def origem_destino_iguais(origem, destino, lista_de_erros):
    '''  Verifica se destino e origem sao iguais '''
    if destino==origem:
        lista_de_erros['destino']='Origem e destino não podem ser iguais'

def campo_tem_algum_numero(valor_campo, nome_campo, lista_de_erros):
    '''  Verifica se um campo tem algum valor numerico '''
    if any(char.isdigit() for char in valor_campo):
        lista_de_erros[nome_campo]='Este campo nao pode conter numeros'