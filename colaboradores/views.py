from django.shortcuts import render, redirect, get_object_or_404
from .models import Colaborador

# LISTAR + PESQUISA
def lista(request):
    query = request.GET.get('q')

    if query:
        dados = Colaborador.objects.filter(nome__icontains=query)
    else:
        dados = Colaborador.objects.all()

    return render(request, 'lista.html', {'dados': dados})


# CRIAR
def criar(request):
    if request.method == "POST":
        Colaborador.objects.create(
            nome=request.POST['nome'],
            cpf=request.POST['cpf'],
            cargo=request.POST['cargo'],
            setor=request.POST['setor']
        )
        return redirect('lista')

    return render(request, 'form.html')


# EDITAR
def editar(request, id):
    obj = get_object_or_404(Colaborador, pk=id)

    if request.method == "POST":
        obj.nome = request.POST['nome']
        obj.cpf = request.POST['cpf']
        obj.cargo = request.POST['cargo']
        obj.setor = request.POST['setor']
        obj.save()

        return redirect('lista')

    return render(request, 'form.html', {'obj': obj})


# EXCLUIR
def excluir(request, id):
    obj = get_object_or_404(Colaborador, pk=id)
    obj.delete()
    return redirect('lista')