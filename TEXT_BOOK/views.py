# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from models import Book



class BookList(ListView):
    template_name = 'book_list.html'
    model = Book


class BookCreate(CreateView):
    template_name = 'book_form.html'
    model = Book
    fields = ['name', 'pages']
    success_url = reverse_lazy('book_list')


class BookUpdate(UpdateView):
    template_name = 'book_form.html'
    model = Book
    fields = ['name', 'pages']
    success_url = reverse_lazy('book_list')

class BookDelete(DeleteView):
    template_name = 'book_confirm_delete.html'
    model = Book
    success_url = reverse_lazy('book_list')
# Create your views here.
