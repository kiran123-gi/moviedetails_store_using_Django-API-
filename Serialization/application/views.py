from django.shortcuts import render
from .models import MovieModels
from .serializer import MoviesSerializers

def test_case(request):
    #ORM QUERY
    obj1 = MovieModels.objects.all()
    serializer = MoviesSerializers(obj1,many = True)
    context = {'obj1':serializer.data}
    return render(request,"frontend/index.html",context)
