from django.shortcuts import render
from .models import Project


# Create your views here.
def perfil(request):
    # p1 = Project(title="Proyecto1", desc="Descripcion del proyecto1")
    # p1.save()

    # p2 = Project(title="Proyecto2", desc="Descripcion del proyecto2")
    # p2.save()

    # p3 = Project(title="Proyecto3", desc="Descripcion del proyecto3")
    # p3.save()
    projects = Project.objects.all()
    print(projects)
    return render(request, 'profile.html', {'projects': projects})
