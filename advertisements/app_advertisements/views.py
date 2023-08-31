from django.shortcuts import render, redirect, reverse
from .models import Advertisement
from .forms import AdvertisementForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.db.models import Count
from django.contrib.auth import get_user_model

User = get_user_model()


def index(request):
    title = request.GET.get('query')
    if title:
        advertisements = Advertisement.objects.filter(title__contains=title)
    else:
        advertisements = Advertisement.objects.all()
    context = {'advertisements': advertisements,
               'title': title}
    return render(request, 'app_advertisements/index.html', context)


def top_sellers(request):
    users = User.objects.annotate(
        adv_count=Count('advertisement')
    ).order_by('-adv_count')
    return render(request, 'app_advertisements/top-sellers.html', {'users': users})


@login_required(login_url=reverse_lazy('login'))
def advertisement_post(request):
    if request.method == 'POST':
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            advertisement = form.save(commit=False)
            advertisement.user = request.user
            advertisement.save()
            return redirect(reverse('index-page'))
        return render(request, 'app_advertisements/advertisement-post.html', {'form': form})
    form = AdvertisementForm()
    return render(request, 'app_advertisements/advertisement-post.html', {'form': form})


def advertisement_detail(request, pk):
    adv = Advertisement.objects.get(id=pk)
    return render(request, 'app_advertisements/advertisement.html', {'adv': adv})