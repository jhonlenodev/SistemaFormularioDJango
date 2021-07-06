from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404

from core.models import Contato
from core.forms import ContatoForm

class ContatoCreate(CreateView):
    form_class = ContatoForm
    template_name = 'contato.html'

    def get_success_url(self):
        return reverse('contato_form_sucesso')

class ContatoCreateSucesso(TemplateView):
    template_name = 'contato_sucesso.html'