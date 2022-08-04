from django.urls import path
from . import views

urlpatterns = [

    path('',views.getroutes,name="routes"),
    path('notes/',views.getnotes,name='notes'),

    path('notes/create/',views.createnote,name='create-note'),
    path('notes/<str:pk>/update/',views.updatenote,name='update-note'),
    path('notes/<str:pk>/delete/',views.deletenote,name='delete-note'),

    path('notes/<str:pk>/',views.getnote,name='note'),

]
