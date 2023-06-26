from django import forms
from django.core.mail.message import EmailMessage
from .models import Produto


class ContatoForms(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    asunto = forms.CharField(label='Asunto', max_length=120)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        asunto = self.cleaned_data['asunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome: {nome} \n Email: {email} \n Asunto {asunto} \n Mensagem {mensagem}'

        mail = EmailMessage(
            subject='Email enviado com sucesso',
            body=conteudo,
            from_email='email@dominio.com.br',
            to=['email@dominio.com.br', ],
            headers={'Reply-To': email}
        )
        mail.send()


class ProdutoModelForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'estoque', 'imagem']
