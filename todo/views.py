from django.views.generic import(
  ListView, DetailView, CreateView, UpdateView, DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect

from .models import Todo
from .forms import TodoForm

# Create your views here.

class IndexView(LoginRequiredMixin, ListView):
  
  template_name = 'index.html'
  model = Todo
  context_object_name = 'todos'

  def get_queryset(self):
    return Todo.objects.filter(create_user_id = self.request.user.id).filter(status__in=[1, 2]).order_by('deadline')

index = IndexView.as_view()

class TodoDetailView(LoginRequiredMixin, DetailView):

  template_name = 'todo/detail.html'
  model = Todo
  context_object_name = 'todo'

todo_detail = TodoDetailView.as_view()

class TodoCreateView(LoginRequiredMixin, CreateView):

  template_name = 'todo/create.html'
  model = Todo
  form_class = TodoForm
  success_url = reverse_lazy('todo:index')

  def form_valid(self, form):
    qryset = form.save(commit=False)
    qryset.create_user = self.request.user
    qryset.save()
    return redirect('todo:index') 

todo_create = TodoCreateView.as_view()

class TodoUpdateView(LoginRequiredMixin, UpdateView):

  template_name = 'todo/update.html'
  model = Todo
  form_class = TodoForm
  success_url = None

  def get_success_url(self):
    success_url = reverse_lazy('todo:todo_detail', kwargs={'pk':self.kwargs['pk']})
    return success_url
  

todo_update = TodoUpdateView.as_view()

class TodoDeleteView(LoginRequiredMixin, DeleteView):

  template_name = 'todo/delete.html'
  model = Todo
  success_url = reverse_lazy('todo:index')

todo_delete = TodoDeleteView.as_view()