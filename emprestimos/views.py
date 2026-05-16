from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from django.utils.dateparse import parse_datetime

from .models import EmprestimoEPI
from colaboradores.models import Colaborador
from equipamentos.models import Equipamento



def lista_emprestimos(request):
    dados = EmprestimoEPI.objects.all()

    colaborador = request.GET.get('colaborador')
    equipamento = request.GET.get('equipamento')
    status = request.GET.get('status')

    if colaborador:
        dados = dados.filter(colaborador__nome__icontains=colaborador)

    if equipamento:
        dados = dados.filter(equipamento__nome__icontains=equipamento)

    if status:
        dados = dados.filter(status=status)

    return render(request, 'emprestimos/lista.html', {
        'dados': dados,
        'status_choices': EmprestimoEPI.Status.choices  # 🔥 ESSENCIAL
    })





def criar_emprestimo(request):
    if request.method == "POST":
        try:
            data_prevista_raw = request.POST.get('data_prevista_devolucao')


            if not data_prevista_raw:
                messages.error(request, 'Data prevista é obrigatória.')
                return redirect('emprestimos_criar')


            data_prevista = parse_datetime(data_prevista_raw)


            if not data_prevista:
                messages.error(request, 'Formato de data inválido.')
                return redirect('emprestimos_criar')


            
            if timezone.is_naive(data_prevista):
                data_prevista = timezone.make_aware(data_prevista)


            
            if data_prevista <= timezone.now():
                messages.error(request, 'A data deve ser futura.')
                return redirect('emprestimos_criar')


            colaborador = get_object_or_404(Colaborador, id=request.POST['colaborador'])
            equipamento = get_object_or_404(Equipamento, id=request.POST['equipamento'])


            EmprestimoEPI.objects.create(
                colaborador=colaborador,
                equipamento=equipamento,
                data_prevista_devolucao=data_prevista,
                status=EmprestimoEPI.Status.EMPRESTADO
            )


            messages.success(request, 'Empréstimo criado com sucesso!')
            return redirect('emprestimos_lista')


        except Exception as e:
            messages.error(request, f'Erro ao criar: {str(e)}')
            return redirect('emprestimos_criar')


    return render(request, 'emprestimos/form.html', {
        'colaboradores': Colaborador.objects.all(),
        'equipamentos': Equipamento.objects.all(),


        'status_choices': [
            (EmprestimoEPI.Status.EMPRESTADO, 'Emprestado'),
            (EmprestimoEPI.Status.FORNECIDO, 'Fornecido'),
        ]
    })


def editar_emprestimo(request, id):
    obj = get_object_or_404(EmprestimoEPI, pk=id)

    if request.method == "POST":
        try:
            obj.status = request.POST['status']

            data_dev_raw = request.POST.get('data_devolucao')
            data_dev = None

            if data_dev_raw:
                data_dev = parse_datetime(data_dev_raw)

                if data_dev and timezone.is_naive(data_dev):
                    data_dev = timezone.make_aware(data_dev)

            obj.data_devolucao = data_dev
            obj.observacao_devolucao = request.POST.get('observacao_devolucao')

            obj.save()

            messages.success(request, 'Empréstimo atualizado com sucesso!')
            return redirect('emprestimos_lista')

        except Exception as e:
            messages.error(request, f'Erro ao atualizar: {str(e)}')

    return render(request, 'emprestimos/form.html', {
        'obj': obj,
        'colaboradores': Colaborador.objects.all(),
        'equipamentos': Equipamento.objects.all(),

        
        'status_choices': EmprestimoEPI.Status.choices
    })



def excluir_emprestimo(request, id):
    obj = get_object_or_404(EmprestimoEPI, pk=id)

    if request.method == "POST":
        obj.delete()
        messages.success(request, 'Empréstimo excluído com sucesso!')
        return redirect('emprestimos_lista')

    return render(request, 'emprestimos/confirmar_exclusao.html', {
        'obj': obj
    })