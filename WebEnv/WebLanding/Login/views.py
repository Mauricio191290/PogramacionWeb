from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django

# def LoginView(request):
#     return render(request, 'Login.html',{})

# def LandingView(request):
#     return render(request, 'Landing.html',{})

class LoginClass(View):
    templates = 'Login/Login.html'
    templates_ok = 'Landing/Landing.html'
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            else: 
                #Si la autenticacion es correcta va a proceder a mostrarme el dashboard
                return redirect ('Dashboard:Dashboard')
        return render(request, self.templates,{})



        #Metodo post que hará mi validación
    def post (self, request, *args, **kwargs):
        user_post = request.POST['user']
        password_post = request.POST['password']
        user_session = authenticate(username = user_post, password = password_post)
        #Validacion a traves de un if
        if user_session is not None:
            login_django( #Uso de login django para ver si la sesion esta activa
                request, user_session
            )
            next_url = request.GET.get('next')
            
            if next_url:
                return redirect(next_url)
            else:
                return redirect('Dashboard:Dashboard')
        else:
            self.message = 'Usuario o contraseña incorrecto'
        
        return render(request, self.templates, self.get_context())

    def get_context(self):
        return{
           'error': self.message
        }

