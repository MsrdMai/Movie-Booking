from django.contrib import admin

from django.contrib.auth.models import Permission
from .models import Movie, Type, Seat, Status
# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'datetime', 'movie_type', 'des', 'img', 'capital', 'income']


class TypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class SeatAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'movie_seat', 'seat_status']

    
class StatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

admin.site.register(Permission)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Seat, SeatAdmin)