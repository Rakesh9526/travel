from django.urls import path
from travelapp import views

urlpatterns=[

    path('indexpg/',views.indexpg,name='indexpg'),
    # path('add/',views.addition,name='addition'),


]