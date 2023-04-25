from django.utils import timezone
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Url
from django.contrib import messages
import random,string
from .forms import UrlForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group, User
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.decorators import login_required

from rest_framework.authtoken.models import Token

# Create your views here.

def getAlias():
    return "".join([random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(8) ])


def dashboard(request):
    urls = Url.objects.filter(user=request.user)

    token_exists = Token.objects.filter(user=request.user).exists()
    if token_exists:
        token = Token.objects.get(user=request.user)
        print(token)
    else:
        token = None

    site = get_current_site(request)
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            URL = form.cleaned_data['target_url']
            alias = form.cleaned_data['alias']
            if not alias:
                alias = getAlias()
            Url.objects.create(user=request.user, target_url = URL, alias = alias).save()
            messages.success(request, 'Shortening Successful')
            return redirect("dashboard")
            # try:
            #     # request.user.url_set(target_url=url)
            #     Url.objects.create(user=request.user, target_url = URL, alias = alias).save()
            #     messages.success(request, 'Shortening Successful')
            #     return redirect("dashboard")
            # except:
            #     form = UrlForm()           
            #     messages.error(request, "Alias already in use")
            #     return render(request, 'services/dashboard.html', {'urlform':form, 'urls': urls, 'domain':site}) 
        else:
             if Url.objects.filter(alias=request.POST.get('alias')).exists():
                print("Hi subham")
                messages.error(request, "Alias already in use")
                return redirect("dashboard")
    form = UrlForm()           
    return render(request, 'services/dashboard.html', {'urlform':form, 'urls': urls, 'domain':site, 'token':token})   


def redirect_to_target_page(request, alias):
    obj = Url.objects.get(alias=alias)
    obj.redirect_count += 1
    obj.last_clicked = timezone.now()
    obj.save(update_fields=['last_clicked', 'redirect_count'])
    URL = obj.target_url
    return redirect(URL)

@login_required
def delete_view(request, pk):
    obj = Url.objects.get(pk=pk)
    if (request.user.email == obj.user.email):
        obj.delete()
        messages.error(request, "Deleted Entry!!!!")
        return redirect("dashboard")
    else:
        messages.error(request, "Don't try to be smart!!!!, You are not authorised to delete any entry that you haven't created.")
        return redirect("dashboard")
    
@login_required
def gettoken(request):
    token, created = Token.objects.get_or_create(user=request.user)
    messages.success(request, 'Unique Token successfully generated')
    return redirect("dashboard")
