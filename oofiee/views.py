from django.shortcuts import redirect
from django.views import generic

class toHome(generic.View):
    def get(self, request):
        return redirect('home:index')