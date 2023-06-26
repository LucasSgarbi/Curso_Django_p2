from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from .models import Produto
from .forms import ContatoForms, ProdutoModelForm


# Create your views here.

def index(request):
    context = {
        'produtos': Produto.objects.all()
    }
    return render(request, 'index.html', context)


def contato(request):
    form = ContatoForms(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_mail()
            messages.success(request, 'Email enviado com sucesso!')
            form = ContatoForms()
        else:
            messages.error(request, 'Erro ao enviar o Email')

    context = {
        'form': form
    }
    return render(request, 'contato.html', context)


def produto(request):
    print(f'Usuario:{request.user}')
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':
            form = ProdutoModelForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, 'Produto Salvo com Sucesso')
                form = ProdutoModelForm()
            else:
                messages.error(request, 'Erro a Salvar o produto')
        else:
            form = ProdutoModelForm()
        context = {
            'form': form
        }
        return render(request, 'produto.html', context)
    else:
        return redirect('index')
