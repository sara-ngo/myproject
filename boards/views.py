from django.http.response import Http404
from django.shortcuts import get_object_or_404, render
from .models import Board

# Create your views here.
def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})

def board_topics(request, pk):
    # try:
    #     board = Board.objects.get(pk=pk)
    # except Board.DoesNotExist:
    #     raise Http404
    # return render(request, 'topics.html', {'board': board})
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'topics.html', {'board': board})