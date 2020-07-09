
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Movie, Type, Seat, Status
# Create your views here.


def my_home(request):

    types = Type.objects.all()
    """
        แสดงข้อมูล ทั้งหมดในระบบ
    """
    search_txt = request.GET.get('inputSearch', '')
    print(search_txt)
    semester = request.GET.get('semester', '')

    object_list = Movie.objects.filter(
        title__icontains=search_txt
    )
    if semester:
        object_list = object_list.filter(movie_type=semester)


    return render(request, 'home.html', context={
        'types' : types,
        'object_list' : object_list,
        'search_txt': search_txt,
        'semester': semester,

    })

def des_movie(request, id):
    movie = Movie.objects.get(pk=id)
    seat = Seat.objects.filter(movie_seat=movie.id)
    income = 0

    for m in seat:
        if m.seat_status_id == 2:
            income += m.price

    movie.income = income
    movie.save()
    return render(request, 'movie.html', context={
        'movie' : movie,
        'seat' : seat,

    })



def report(request):
    return render(request, 'report.html', context={
      
    })

def buy(request, id):
    seat = Seat.objects.get(pk=id)

    if request.method == 'GET':
        if (seat.seat_status_id == 1):
            seat.seat_status_id = 2
            seat.save()
            msg = 'Reservation Successful'

        else:
            seat.seat_status_id = 1
            seat.save()
            msg = 'Cancel Reservation'
            
            
    return render(request, 'status.html', context={
                        'seat' : seat,
                        'msg' : msg
                    })

