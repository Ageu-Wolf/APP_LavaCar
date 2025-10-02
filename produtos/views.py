from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.context_processors import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from produtos.forms import ProdutoModelForm
from produtos.models import Produto


class ProdutosView(PermissionRequiredMixin,ListView):
    permission_required = 'produtos.view_produto'
    permission_denied = 'Visualizar produto'
    model = Produto
    template_name = 'produtos.html'

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs = super(ProdutosView, self).get_queryset()

        if buscar:
            qs = qs.filter(nome__icontains=buscar)

        if qs.count() > 0:
            paginator = Paginator(qs, 1)
            listagem = paginator.get_page(self.request.GET.get('page'))
            return listagem
        else:
            return messages.info(self.request, 'Não existe nenhum produto cadastrado.')


class ProdutoAddView(PermissionRequiredMixin,SuccessMessageMixin, CreateView):
    permission_required = 'produtos.add_produto'
    permission_denied = 'Cadastrar produto'
    model = Produto
    template_name = 'produto_form.html'
    form_class = ProdutoModelForm
    success_url = reverse_lazy('produtos')
    success_message = 'Produto Cadastrado com sucesso.'

class ProdutoUpdateView(PermissionRequiredMixin,SuccessMessageMixin, UpdateView):
    permission_required = 'produtos.update_produto'
    permission_denied = 'Editar produto'
    model = Produto
    form_class = ProdutoModelForm
    template_name = 'produto_form.html'
    success_url = reverse_lazy('produtos')
    success_message = "Produto atualizado com sucesso!"

class ProdutoDeleteView(PermissionRequiredMixin,SuccessMessageMixin, DeleteView):
    permission_required = 'produtos.delete_produto'
    permission_denied = 'Excluir produto'
    model = Produto
    template_name = 'produto_apagar.html'
    success_url = reverse_lazy('produtos')
    success_message = 'Produto deletado com sucesso!'