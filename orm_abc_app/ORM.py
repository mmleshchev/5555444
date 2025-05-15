'''
https://docs.djangoproject.com/en/4.1/ref/models/querysets/
https://docs.djangoproject.com/en/4.1/ref/models/
https://docs.djangoproject.com/en/4.1/ref/models/fields/


'''

# python manage.py shell

from django.db import models
from orm_abc_app.models import AbcModel


new_obj = AbcModel(task='new_task')
new_obj.save()

AbcModel.objects.all()
for e in AbcModel.objects.all():
    print(e.name)

AbcModel.objects.all().order_by('id').reverse()
AbcModel.objects.values('id', 'task', 'current_date').order_by('-id')
# !
AbcModel.objects.values().filter(id__gte=27).order_by('-id')[0:1][0]['task']

AbcModel.objects.all().order_by('-id')[:1][0]
AbcModel.objects.values('id')[2:3]
AbcModel.objects.values()[2:4][0]['id']

AbcModel.objects.all()[2:4]
AbcModel.objects.values_list()
AbcModel.objects.values_list('id')[:1]
AbcModel.objects.values_list()[2:4][1][1]
AbcModel.objects.values_list('id','task').order_by('id').reverse()[:3]

AbcModel.objects.filter(id__gte=27).delete()
del_obj = AbcModel.objects.filter(id__gte=27)
del_obj.delete()
AbcModel.objects.values_list('id').order_by('id').reverse()[:3]


AbcModel.objects.filter(id__gte=22).update(task = "update")
update_obj = AbcModel.objects.filter(id__gte=1)
update_obj.update(task = "update", b=1)
AbcModel.objects.values_list('id','task').order_by('id').reverse()[:3]


from django.db import connection
connection.queries
from django.db import reset_queries
reset_queries()

AbcModel.objects.all().order_by('-pk')
AbcModel.objects.all().reverse()
AbcModel.objects.values('pk', 'b').filter(b__gte=6)
AbcModel.objects.values('pk', 'b').get(pk=11)
AbcModel.objects.get(pk=11)
object = AbcModel.objects.get(pk=11)
object.current_date


object = AbcModel.objects.get(pk=11)
AbcModel.objects.filter(task__contains='Ра')
AbcModel.objects.filter(task__icontains='Ра')
AbcModel.objects.filter(task__contains='Ра').count()
connection.queries
AbcModel.objects.filter(task__icontains='на', id__gte=17)
AbcModel.objects.filter(task__icontains='на', id__gte=17).count()
cur_objects = AbcModel.objects.filter(task__icontains='на', id__gte=15)
cur_objects.values('b')
cur_objects = AbcModel.objects.filter(id__gte=17) & AbcModel.objects.filter(c__gte=15)

from django.db.models import Q
AbcModel.objects.filter(Q(id__gte=17) & Q(c__gte=15))
AbcModel.objects.filter(Q(id__gte=17) & Q(c__gte=15)).values()
AbcModel.objects.filter(Q(id__gte=17) & Q(c__gte=15)).values().first()

cur_objects.count()
cur_objects.earliest("current_date")
cur_objects.values().earliest("current_date")

Агрегируем
from django.db.models import *
cur_objects = AbcModel.objects.all()
cur_objects.values('id')
cur_objects.aggregate(Count('id'))
cur_objects.aggregate(Avg('id'))
cur_objects.aggregate(Min('id'))
cur_objects.aggregate(Max('id'))
cur_objects.aggregate(StdDev('id'))
cur_objects.aggregate(Sum('id'))


cur_objects.aggregate(res = Sum('id') - Count('id'))
result = cur_objects.aggregate(res = Sum('id') - Count('id'))
result['res']
result = cur_objects.values('id').aggregate(res = Sum('id') - Count('id'))

for item in cur_objects.values():
    print(item['id'], item['c'])

(AbcModel.objects.filter(id__gte=17) & AbcModel.objects.filter(c__gte=15)).values('c').annotate(Count('id'))
r = (AbcModel.objects.filter(id__gte=17) & AbcModel.objects.filter(c__gte=15)).values('c')
r.all()
r.annotate(Count('c'))
r.annotate(Sum('c'))

функции
obj = AbcModel.objects.filter(Q(id__gte=17) & Q(c__gte=15)).values('task').first()
obj = AbcModel.objects.filter(Q(id__gte=17) & Q(c__gte=15)).values().first()
obj['task'].__len__()


from django.db.models.functions import Abc
from django.db.models.functions import *

q = AbcModel.objects.values().annotate(a1 = Abs('c')+2)
q.values('a1')
q.values('a1')[3]
from django.db.models.functions import Power
q = AbcModel.objects.values().annotate(pw = Power('b','c'))
q.values('b', 'c', 'pw')
q.aggregate(Sum('pw'))

res = AbcModel.objects.values().annotate(r = Random())
res.values_list('r')

res = AbcModel.objects.values().annotate(r = 'a'*'b')
res.values_list('r')


x = AbcModel.objects.raw('SELECT * FROM orm_abc_app.Abc')
x.model.objects.values()
