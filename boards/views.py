from django.shortcuts import render, get_object_or_404,redirect
from .models import Board, Topic, Post
from django.contrib.auth.models import User
from .forms import NewTopicForm

""""
day 1

def home(request):
    boards = Board.objects.all()
    boards_names = list()

    for board in boards:
        boards_names.append(board.name)

    response_html = '<br>'.join(boards_names)

    return HttpResponse(response_html)
"""


def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})


def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'topics.html',{'board': board})


def new_topic(request,pk):
    board = get_object_or_404(Board, pk=pk)
    user = User.objects.first()

    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = user
            topic.save()
            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=user
            )
        '''
        #subject = request.POST['subject']
        #message = request.POST['message']

        #user = User.objects.first()

        #topic = Topic.objects.create(
        #    subject=subject,
        #    board=board,
        #    starter=user,
        #)

        #post = Post.objects.create(
        #    message=message,
        #    topic=topic,
        #    created_by=user,
        #)
        '''
        return redirect('board_topics', pk=board.pk)
    else:
        form = NewTopicForm()
    return render(request, 'new_topic.html',{'board': board, 'form': form})
