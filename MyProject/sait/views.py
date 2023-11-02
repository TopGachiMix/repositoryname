from django.shortcuts import render, redirect, reverse
from .forms import AdvertisementsForm
from .models import advertisement
from django.contrib.auth.models import User
from django.db.models import Count
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required





def max(request):
    title = request.GET.get('query')
    if title:
        Advertisements = advertisement.objects.filter(title__icontains=title)
    else:
        Advertisements = advertisement.objects.all()
    context = {'Advertisements': Advertisements, 'title': title,
               }
    return render(request, 'index.html', context)


def top_sellers(request):
    users = User.objects.annotate(adv_count=Count('advertisement')).order_by('-adv_count')
    context = {
        'users': users,
    }
    return render(request, 'top-sellers.html', context)

#@login_required(login_url=reverse_lazy('login'))
def advertisement_post(request):
    form = AdvertisementsForm()
    if request.method == 'POST':
        form = AdvertisementsForm(request.POST, request.FILES)
        if form.is_valid():
            Advertisements = advertisement(**form.cleaned_data)
            Advertisements.user = request.user
            Advertisements.save()
            url = reverse('main-page')
            return redirect(url)
    context = {'form': form}
    return render(request, 'advertisement-post.html', context)


def tovar_details(request,pk):
    Advertisements = advertisement.objects.get(id=pk),
    context = {
            'Advertisements': Advertisements
    }
    return render(request,'advertisement.html',context)