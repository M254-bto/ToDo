from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from.models import ToDo
from django.http import HttpResponseRedirect
from django.urls import reverse


def index(request):
    todo_items = ToDo.objects.all().order_by('-date_added')
    return render(request, 'list/index.html', {
        "todo_items": todo_items
    })


@csrf_exempt
def add_item(request):
    request.POST
    current_date = timezone.now
    content = request.POST['content']
    new_object = ToDo.objects.create(date_added = current_date, text = content)
    return redirect('/list')


@csrf_exempt
def delete_item(request, item_id):
      ToDo.objects.get(id=item_id).delete()
      return redirect('/list')

