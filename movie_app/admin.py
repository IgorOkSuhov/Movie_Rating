from django.contrib import admin
from .models import Movie, Director, Actor
from django.db.models import QuerySet
from django.contrib.auth.models import  User

admin.site.register(Director)
admin.site.register(Actor)

# Register your models here.
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    fields = []
    list_display = ['name','rating','currency','budget',]
    list_editable = ['rating','currency','budget',]
    ordering = ['name']
    list_per_page = 10
    actions = ['set_dollars','set_euro']
    search_fields = ['name','rating','currency']
    list_filter = ['name','currency']
    filter_horizontal = ['actors']


    @admin.action(description='Установить валюту в USD')
    def set_dollars(self, request, qs: QuerySet):
        qs.update(currency=Movie.USD)

    @admin.action(description='Установить валюту в EURO')
    def set_euro(self, request, qs: QuerySet):
        count_updated = qs.update(currency=Movie.EURO)
        self.message_user(
            request,
            f'Было обновленно {count_updated} записей'
        )






