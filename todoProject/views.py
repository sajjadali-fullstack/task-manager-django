from django.shortcuts import render
from todo.models import Task



def home_view(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')  # Decanding order
    # tasks = Task.objects.filter(is_completed=False).order_by('updated_at')  # Assending order
    # print(tasks)

    completed_tasks = Task.objects.filter(is_completed=True)
    
    context = {'tasks':tasks, 'completed_tasks':completed_tasks}

    return render(request, 'testapp/home.html', context)


 