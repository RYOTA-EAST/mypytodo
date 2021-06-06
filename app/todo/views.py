from django.views.generic import(
  ListView, DetailView, CreateView, UpdateView, DeleteView,
)
from django.urls import reverse_lazy

from .models import Todo
from .forms import TodoForm

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

class TodoCreateView(CreateView):

  template_name = 'todo/create.html'
  model = Todo
  form_class = TodoForm
  success_url = reverse_lazy('todo:index')

todo_create = TodoCreateView.as_view()

class TodoUpdateView(UpdateView):

  template_name = 'todo/update.html'
  model = Todo
  form_class = TodoForm
  success_url = None

  def get_success_url(self):
    success_url = reverse_lazy('todo:todo_detail', kwargs={'pk':self.kwargs['pk']})
    return success_url
  

todo_update = TodoUpdateView.as_view()

class TodoDeleteView(DeleteView):

  template_name = 'todo/delete.html'
  model = Todo
  success_url = reverse_lazy('todo:index')

todo_delete = TodoDeleteView.as_view()