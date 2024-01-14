from django.shortcuts import render
from django.http import HttpResponse
from .models import Servers, ServerTypes

from django.shortcuts import render
from .models import Servers, ServerTypes

def index(request):
    # Get all server types with name 'tp1'

    server_type = ServerTypes.objects.filter(name='tp1')
    # server_type = ServerTypes.objects.get(name='tp1').first()

    # servers = Servers.objects.filter(server=server_type)
        # Handle the case when no server type is found
    active_server = Servers.objects.filter(status='active', servertypes__name='tp1')
    inactive_server = Servers.objects.filter(status='inactive')
    server = Servers.objects.get(name='server1')
    # active_servers = Servers.objects.filter(status='active')


    context = {'server_types': server_type, 'active_servers': active_server, 'inactive_servers': inactive_server, 'server': server}

    return render(request, 'index.html', context)




