from django.shortcuts import render, HttpResponse
from .forms import PassagemForm

def index(request):
    ''' Formulario para usuario preencher informacoes sobre a passagem. '''
    form = PassagemForm()
    contexto = {'form':form}
    return render(request,'index.html',contexto)

def minha_consulta(request):
    '''
        Se o formulario for valido: Mostra as informacoes da passagem que o usuario preencheu.
        Se nao: retorna para atualizar formulario instanciado com as informacoes que o usuario havia preenchido.
    '''
    if request.method == 'POST':
        form = PassagemForm(request.POST)
        if form.is_valid():
            contexto = {'form':form}
            return render(request,'minha_consulta.html',contexto)
        else:
            contexto = {'form':form}
            return render(request,'index.html',contexto)