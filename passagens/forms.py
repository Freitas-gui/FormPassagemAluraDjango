from datetime import datetime
from django import forms
from .classe_viagem import tipos_de_classes
from .validations import *


class PassagemForm(forms.Form):
    ''' Formulario com todos os campos necessarios para o usuario especificar uma passagem '''

    origem = forms.CharField(label='Origem',max_length=100)
    destino = forms.CharField(label='Destino', max_length=100)
    data_ida = forms.DateField(label='Data da ida',
        widget=forms.DateInput(format='%m/%d/%Y'),input_formats=['%m/%d/%Y'])
    data_volta = forms.DateField(label='Data da volda')
    data_pesquisa = forms.DateField(label='Data da pesquisa', disabled=True, initial=datetime.today)
    classe_viagem = forms.ChoiceField(label='Tipo de classe', choices=tipos_de_classes)
    informacoes = forms.CharField(
        label='Informações extras',
        widget=forms.Textarea,
        required=False,
        max_length=250
    )
    email = forms.EmailField(label='Email',max_length=50)

    def clean(self):
        ''' Verifica se há erros nos formatos suportados por cada campo e caso exista mostra o tipo de erro. '''

        #captura o valor do campo (origem) preenchido.
        origem = self.cleaned_data.get('origem')
        #captura o valor do campo (destino) preenchido.
        destino = self.cleaned_data.get('destino')
        lista_de_erros={}
        origem_destino_iguais(origem, destino, lista_de_erros)
        campo_tem_algum_numero(origem, 'origem', lista_de_erros)
        campo_tem_algum_numero(destino, 'destino', lista_de_erros)
        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_erro = lista_de_erros[erro]
                #adiciona uma mensagem de erro no devido campo que esta com erro.
                self.add_error(erro, mensagem_erro)
        return self.cleaned_data

