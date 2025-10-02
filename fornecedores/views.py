from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import FornecedorModelForm
from .models import Fornecedor

class FornecedoresView(PermissionRequiredMixin,ListView):
    permission_required = 'agendamentos.view_agendamento'
    permission_denied = 'Visualizar agendamento'
    model = Fornecedor
    template_name = 'fornecedores.html'

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs = super(FornecedoresView, self).get_queryset()

        if buscar:
            qs = qs.filter(nome__icontains=buscar)

        if qs.count() > 0:
            paginator = Paginator(qs, 1)
            listagem = paginator.get_page(self.request.GET.get('page'))
            return listagem
        else:
            return messages.info(self.request, 'Não existem fornecedores cadastrados.')

class FornecedorAddView(PermissionRequiredMixin,SuccessMessageMixin, CreateView):
    permission_required = 'fornecedores.add_fornecedores'
    permission_denied = 'Cadastrar fornecedores'
    model = Fornecedor
    form_class = FornecedorModelForm
    template_name = 'fornecedor_form.html'
    success_url = reverse_lazy('fornecedores')
    success_message = "Fornecedor cadastrado com sucesso!"

class FornecedorUpdateView(PermissionRequiredMixin,SuccessMessageMixin, UpdateView):
    permission_required = 'fornecedores.update_fornecedores'
    permission_denied = 'Editar cliente'
    model = Fornecedor
    form_class = FornecedorModelForm
    template_name = 'fornecedor_form.html'
    success_url = reverse_lazy('fornecedores')
    success_message = "Fornecedor atualizado com sucesso!"

class FornecedorDeleteView(PermissionRequiredMixin,SuccessMessageMixin, DeleteView):
    permission_required = 'fornecedor.delete_fornecedores'
    permission_denied = 'Excluir cliente'
    model = Fornecedor
    template_name = 'fornecedor_apagar.html'
    success_url = reverse_lazy('fornecedores')
    success_message = 'Fornecedor deletado com sucesso!'