from django.http import HttpResponse
from django.views.generic import TemplateView, View
from .models.carrera import Carrera  
from tutorial.vistas.formCarrera import FormCarrera  
from django.shortcuts import redirect, render, get_object_or_404


def index(request):
    return HttpResponse("Hola, mundo!")


class HomePageView(TemplateView):
    template_name = 'home.html'
    model = Carrera

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Saludo"] = "Hola de nuevo"
        context["Lista"] = self.model.objects.all()
        return context


class AboutPageView(TemplateView):
    template_name = 'about.html'


class CarreraCreateViewPage(View):
    template_name = "carreras_form.html"

    def get(self, request, *args, **kwargs):
        form = FormCarrera()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = FormCarrera(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_carrera')
        else:
            context = {'form': form}  
            return render(request, self.template_name, context)  

class CarrerasEditarPageView(TemplateView):
    template_name = "carreras_form.html"
    def get(self, request, pk, *args, **kwargs):
        carrera = get_object_or_404(Carrera, pk=pk)
        form = FormCarrera(instance=carrera)
        return self.render_to_response({ 'form' : form })

    def post(self, request, pk, *args, **kwargs):
        carrera = get_object_or_404(Carrera, pk=pk)
        form = FormCarrera(request.POST, instance=carrera)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return self.render_to_response({'form' : form})

class CarrerasEliminarPageView(TemplateView):
    template_name = "carreras_form.html"
    def get(self, request, pk, *args, **kwargs):
        carrera = get_object_or_404(Carrera, pk=pk)
        form = FormCarrera(instance=carrera)
        carrera.delete()
        return redirect('/')
        