from django.views.generic import(
  ListView, DetailView, CreateView, UpdateView, DeleteView,
)
from django.urls import reverse_lazy

from .models import Todo

# Create your views here.

class IndexView(ListView):
  
  template_name = 'index.html'
  model = Todo
  context_object_name = 'todos'

index = IndexView.as_view()

class TodoDetailView(DetailView):

  template_name = 'todo/detail.html'
  model = Todo
  context_object_name = 'todo'

todo_detail = TodoDetailView.as_view()

class TodoCreateViews(CreateView):

  template_name = 'todo/create.html'
  model = Todo
  fields = ('title', 'body')
  success_url = reverse_lazy('todo:index')

todo_create = TodoCreateViews.as_view()

class TodoUpdateViews(UpdateView):

  template_name = 'todo/update.html'
  model = Todo
  fields = ('title', 'body')
  success_url = reverse_lazy('todo:index')

todo_update = TodoUpdateViews.as_view()

class TodoDeleteViews(DeleteView):

  template_name = 'todo/delete.html'
  model = Todo
  success_url = reverse_lazy('todo:index')

todo_delete = TodoDeleteViews.as_view()