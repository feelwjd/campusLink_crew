from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Agent


def dashboard(request):
    agents = Agent.objects.all()
    return render(request, 'dashboard.html', {'agents': agents})


def update_agent(request, agent_id):
    agent = Agent.objects.get(id=agent_id)
    if request.method == 'POST':
        agent.status = request.POST.get('status')
        agent.log += f"\n{agent.status}"
        agent.save()
        return redirect('dashboard')
    return render(request, 'update_agent.html', {'agent': agent})


def get_logs(request, agent_id):
    agent = Agent.objects.get(id=agent_id)
    logs = agent.log.split('\n')
    return JsonResponse({'logs': logs})
