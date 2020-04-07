from django.shortcuts import render,redirect,get_object_or_404,reverse
from.models import Room,Chat
from django.contrib.auth.decorators import login_required
from .forms import MessageForm,RoomForm
from django.contrib.auth.models import User
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from django.db.models import Q

            # ======================ROOM LIST==========================================#
@login_required(login_url='login')
def room_list(request):
    rooms = Room.objects.filter(Q(invited__in=[request.user.id]) | Q(creater = request.user.id))
    return render(request,'room/room_list.html',{'rooms':rooms,'user_profile':request.user})

           # ======================ROOM DETAIL==========================================#
@login_required(login_url='login')
def room_detail(request,id):
    if request.method =="GET":
        chat = Room.objects.get(id=id)
        messages = chat.chat_set.all()
        paginator = Paginator(messages,5)
        page = request.GET.get('page')
        paged_messages = paginator.get_page(page)
        print( chat.invited)
        print( chat.creater)
        if request.user == chat.invited or  request.user == chat.creater :
            return render(request,'room/room.html',{'user_profile': request.user,'chat': chat,'messages':paged_messages,'form': MessageForm()})
        return redirect('index')

    if request.method=="POST":
        form = MessageForm(data=request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            room = Room.objects.get(id=id)
            message.room=room
            message.user= request.user
            message.save()
        return redirect(reverse('room_detail', kwargs={'id': id}))
    return render(request,'room/room.html',{'chat':chat})


            # ======================ROOM CREATE==========================================#

@login_required(login_url='login')
def room_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        invited_user = User.objects.filter(id=request.POST['id_user'])
        creator = User.objects.filter(id=request.user.id)
        created = Room.objects.filter(Q(invited=invited_user[0]) & Q(creater=creator[0]) | Q(invited=creator[0]) & Q(creater=invited_user[0]) )
        print(created)
        if created:
            print('This room is created')
            return redirect(room_list)
        else:
            print('create room')
            room = Room.objects.create(creater = request.user,invited = invited_user[0],name = name)
            room.save()
            return redirect(room_list)

    return render(request,'room/room_create.html')





def index(request):
    return render(request,'room/index.html')
def about(request):
    return render(request,'room/index.html')

#API VIEWS
# class Room(APIView):
#     def get(self,request):
#         rooms = Room.objects.all()
#         serializer = RoomSerializer(rooms,many=True)
#         return Response(serializer.data)
