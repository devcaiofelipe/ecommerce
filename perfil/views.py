from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, View
from .forms import UserForm, PerfilForm
from .models import Perfil


class BasePerfil(View):
    template_name = 'perfil/criar.html'


    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)

        self.perfil = None

        if self.request.user.is_authenticated:
            self.perfil = Perfil.objects.filter(usuario=self.request.user).first()
            print(self.perfil)
            self.contexto = {'userform': UserForm(data=self.request.POST or None, usuario=self.request.user, instance=self.request.user,),
                             'perfilform': PerfilForm(data=self.request.POST or None)}
        else:
            self.contexto = {'userform': UserForm(data=self.request.POST or None),
                             'perfilform': PerfilForm(data=self.request.POST or None)}

        self.userform = self.contexto['userform']
        self.perfilform = self.contexto['perfilform']


        self.renderizar = render(self.request, self.template_name, self.contexto)


    def get(self, *args, **kwargs):
        return self.renderizar


class Criar(BasePerfil):
    def post(self, *args, **kwargs):
        if not self.userform.is_valid() or not self.perfilform.is_valid():
            return self.renderizar

        username = self.userform.cleaned_data.get('username')
        password = self.userform.cleaned_data.get('password')
        email = self.userform.cleaned_data.get('email')


        if self.request.user.is_authenticated:
            pass
        else:
            usuario = self.userform.save(commit=False)
            usuario.set_password(password)
            usuario.save()

            perfil = self.perfilform.save(commit=False)
            perfil.usuario = usuario
            perfil.save()

        return self.renderizar


class Atualizar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('AtualizarPerfil')


class Login(View):
    def get(self, *args, **kwargs):
        return HttpResponse('LoginPerfil')


class Logout(View):
    def get(self, *args, **kwargs):
        return HttpResponse('LogoutPerfil')
