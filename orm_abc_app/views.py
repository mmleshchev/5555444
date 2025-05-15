from django.shortcuts import render, redirect
from django.db.models import Count
from .forms import AdmissionForm
from .models import Admission

def abc_form(request):
    if request.method == 'POST':
        form = AdmissionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('orm_abc_app:abc_result')
    else:
        form = AdmissionForm()
    return render(request, 'abc_form.html', {'form': form})

def abc_result(request):
    submissions = Admission.objects.order_by('-date_submitted')
    return render(request, 'abc_result.html', {'submissions': submissions})

def table(request):
    qs = Admission.objects.all()

    # 1) фильтр по году
    year = request.GET.get('admission_year')
    if year:
        qs = qs.filter(admission_year=year)

    # 2) сортировка
    valid_fields = {'full_name','admission_year','program_name','date_submitted'}
    sort_by = request.GET.get('sort_by','date_submitted')
    if sort_by not in valid_fields:
        sort_by = 'date_submitted'
    order = request.GET.get('order','desc')
    prefix = '-' if order == 'desc' else ''
    qs = qs.order_by(f'{prefix}{sort_by}')

    # подготовим параметры для переключения направления сортировки в шаблоне
    next_order = 'asc' if order == 'desc' else 'desc'

    # 3) агрегация: посчитаем, сколько заявок по каждому году
    stats = (Admission.objects
                   .values('admission_year')
                   .annotate(count=Count('id'))
                   .order_by('admission_year'))

    return render(request, 'table.html', {
        'objects': qs,
        'request': request,
        'current_sort': sort_by,
        'current_order': order,
        'next_order': next_order,
        'stats': stats,
    })
