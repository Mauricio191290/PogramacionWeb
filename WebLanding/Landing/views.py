from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import redirect
from django.contrib.auth import authenticate

# Unicamente acá el request que me manda al landing

class LandingClass(View):
    templates_ok = 'Landing/Landing.html'
    def get(self, request, *args, **kwargs):
        return render(request,self.templates_ok,{})