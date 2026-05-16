from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
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
        try:
            Colaborador.objects.create(
                nome=request.POST['nome'],
                cpf=request.POST['cpf'],
                cargo=request.POST['cargo'],
                setor=request.POST['setor']
            )
            messages.success(request, 'Colaborador criado com sucesso!')
        except Exception as e:
            messages.error(request, f'Erro ao criar colaborador: {str(e)}')
        return redirect('criar')

    return render(request, 'form.html')


# EDITAR
def editar(request, id):
    obj = get_object_or_404(Colaborador, pk=id)

    if request.method == "POST":
        try:
            obj.nome = request.POST['nome']
            obj.cpf = request.POST['cpf']
            obj.cargo = request.POST['cargo']
            obj.setor = request.POST['setor']
            obj.save()
            messages.success(request, 'Colaborador atualizado com sucesso!')
            return redirect('editar', id=id)
        except Exception as e:
            messages.error(request, f'Erro ao atualizar colaborador: {str(e)}')

    return render(request, 'form.html', {'obj': obj})


# EXCLUIR
def excluir(request, id):
    obj = get_object_or_404(Colaborador, pk=id)
    if request.method == "POST":
        obj.delete()
        messages.success(request, 'Colaborador excluído com sucesso!')
        return redirect('lista')
    return render(request, 'confirmar_exclusao.html', {'obj': obj})