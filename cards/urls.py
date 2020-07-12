
from django.urls import path
from . import views
from .views import SearchResultsView

app_name = 'cards'

urlpatterns = [
    path('', views.card_list, name='list'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('create/', views.card_create, name='create'),
    path('<number>/remove/', views.card_remove, name='card_remove'),
    path('<number>/update/', views.card_update, name='card_update'),
    path('<number>/',views.card_detail, name='detail'),
    

]
