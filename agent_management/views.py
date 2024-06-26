from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Agent, Task
from .crew_agent import kickoff_all_processes


def dashboard(request):
    agents = Agent.objects.all()
    tasks = Task.objects.all()
    return render(request, 'dashboard.html', {'agents': agents, 'tasks': tasks})


def assign_task(request, agent_id):
    if request.method == 'POST':
        agent = get_object_or_404(Agent, id=agent_id)
        task = Task.objects.filter(status='pending').first()
        if task:
            task.assigned_to = agent
            task.status = 'in_progress'
            task.save()
            agent.status = 'busy'
            agent.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'failed'})


def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.result = request.POST.get('result')
        task.status = 'completed'
        task.save()
        return JsonResponse({'status': 'success'})
    return render(request, 'update_task.html', {'task': task})


def kickoff_process(request):
    kickoff_all_processes()
    return JsonResponse({'status': 'success'})
