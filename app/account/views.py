from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

class LoginView(LoginView):

  template_name = 'account/login.html'
  form_class = AuthenticationForm

login = LoginView.as_view()