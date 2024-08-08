from django.shortcuts import render, redirect

def index(request):
    if request.method == "GET" and 'room_name' in request.GET:
        room_name = request.GET['room_name']
        return redirect('room', room_name=room_name)
    return render(request, 'chat/index.html')

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })
