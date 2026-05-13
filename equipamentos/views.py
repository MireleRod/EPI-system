from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from .models import Equipamento


def lista_equipamentos(request):
    query = request.GET.get('q')

    if query:
        dados = Equipamento.objects.filter(
            Q(nome__icontains=query) | Q(codigo__icontains=query)
        )
    else:
        dados = Equipamento.objects.all()

    return render(request, 'equipamentos_lista.html', {'dados': dados})


def criar_equipamento(request):
    if request.method == 'POST':
        try:
            Equipamento.objects.create(
                nome=request.POST['nome'],
                codigo=request.POST['codigo'],
                tipo=request.POST['tipo'],
                classe_risco=request.POST['classe_risco'],
                data_aquisicao=request.POST['data_aquisicao'] or None,
                ativo=('ativo' in request.POST),
            )
            messages.success(request, 'Equipamento criado com sucesso!')
        except Exception as e:
            messages.error(request, f'Erro ao criar equipamento: {str(e)}')
        return redirect('equipamentos_criar')

    return render(request, 'equipamentos_form.html')


def editar_equipamento(request, id):
    obj = get_object_or_404(Equipamento, pk=id)

    if request.method == 'POST':
        try:
            obj.nome = request.POST['nome']
            obj.codigo = request.POST['codigo']
            obj.tipo = request.POST['tipo']
            obj.classe_risco = request.POST['classe_risco']
            obj.data_aquisicao = request.POST['data_aquisicao'] or None
            obj.ativo = ('ativo' in request.POST)
            obj.save()
            messages.success(request, 'Equipamento atualizado com sucesso!')
            return redirect('equipamentos_editar', id=id)
        except Exception as e:
            messages.error(request, f'Erro ao atualizar equipamento: {str(e)}')

    return render(request, 'equipamentos_form.html', {'obj': obj})


def excluir_equipamento(request, id):
    obj = get_object_or_404(Equipamento, pk=id)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, 'Equipamento excluído com sucesso!')
        return redirect('equipamentos_lista')
    return render(request, 'equipamentos_confirmar_exclusao.html', {'obj': obj})
