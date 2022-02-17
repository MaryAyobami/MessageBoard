from django.http import Http404
from django.shortcuts import render ,redirect , get_object_or_404
from .models import Board,Topic,Post,User
from .forms import NewTopicForm


# Create your views here.
def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html' ,{'boards':boards})

def board_topics(request , pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404
    return render(request, 'topics.html', {'board': board})

def new_topic(request,pk):
    board = get_object_or_404(Board,pk=pk)
    user = User.objects.first()
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save()
        return redirect('board_topics', pk=board.pk)
    else:
        form = NewTopicForm()
        return render(request, 'new_topic.html', {'form': form})
    return render(request, 'new_topic.html' , {'board': board})