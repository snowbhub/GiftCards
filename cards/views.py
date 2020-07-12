from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Card
from django.contrib.auth.decorators import login_required
from . import forms
from .forms import CreateCards
from django.views.generic import ListView
from django.db.models import Q
from datetime import date



@login_required(login_url="/accounts/login/")
def card_list(request):
    cards = Card.objects.filter(author=request.user)
    return render(request, 'cards/card_list.html', { 'cards': cards })


@login_required(login_url="/accounts/login/")
def card_detail(request, number):
    card = Card.objects.get(number=number)
    if date.today() > card.expiration_date:
        Card.objects.filter(number=number).update(status="Прострочена")
    return render(request, 'cards/card_detail.html', { 'card': card })





@login_required(login_url="/accounts/login/")
def card_create(request):
    if request.method == 'POST':
        form = forms.CreateCards(request.POST, request.FILES)
        if form.is_valid():
            # save card to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('cards:list')
    else:
        form = forms.CreateCards()
    return render(request, 'cards/card_create.html', { 'form': form })




class SearchResultsView(ListView):
    model = Card
    template_name = 'cards/card_search.html'
    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Card.objects.filter(
            Q(series__icontains=query) | Q(number__icontains=query)|Q( amount__icontains=query) | Q(status__icontains=query)
        )
        return object_list

def card_remove(request, number):
    card = get_object_or_404(Card, number=number)
    card.delete()
    return redirect('home')


def card_update(request, number):
    model=Card
    
    template_name = 'cards/card_detail.html'
    card = get_object_or_404(Card, number=number)
    link = 'http://127.0.0.1:8000/cards/' + card.number
    if card.status == 'Неактивована':
        Card.objects.filter(number=number).update(status="Активована")
    elif card.status == 'Активована':
        Card.objects.filter(number=number).update(status="Неактивована")
 

    return redirect(link)
    
