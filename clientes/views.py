from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render

from .forms import ClienteModelForm
from .models import Cliente

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Cliente

class ClientesView(PermissionRequiredMixin,ListView):
    permission_required = 'clientes.view_cliente'
    permission_denied = 'Visualizar cliente'
    model = Cliente
    template_name = 'clientes.html'

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs = super(ClientesView, self).get_queryset()

        if buscar:
            qs = qs.filter(nome__icontains=buscar)

        if qs.count() > 0:
            paginator = Paginator(qs, 1)
            listagem = paginator.get_page(self.request.GET.get('page'))
            return listagem
        else:
            return messages.info(self.request, 'Não existem clientes cadastrados.')
class ClienteAddView(PermissionRequiredMixin,SuccessMessageMixin, CreateView):
    permission_required = 'clientes.add_cliente'
    permission_denied = 'Cadastrar cliente'
    model = Cliente
    form_class = ClienteModelForm
    template_name = 'cliente_form.html'
    success_url = reverse_lazy('clientes')
    success_message = 'Cliente cadastrado com sucesso.'

class ClienteUpdateView(PermissionRequiredMixin,SuccessMessageMixin, UpdateView):
    permission_required = 'clientes.update_cliente'
    permission_denied = 'Editar cliente'
    model = Cliente
    form_class = ClienteModelForm
    template_name = 'cliente_form.html'
    success_url = reverse_lazy('clientes')
    success_message = "Cliente atualizado com sucesso!"

class ClienteDeleteView(SuccessMessageMixin, DeleteView):
    permission_required = 'clientes.delete_cliente'
    permission_denied = 'Excluir cliente'
    model = Cliente
    template_name = 'cliente_apagar.html'
    success_url = reverse_lazy('clientes')
    success_message = 'Cliente Excluído com sucesso!'