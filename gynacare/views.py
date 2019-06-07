from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .forms import ShareForm
from .models import Share 
from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/login/')
def home(request):

  share = Share.objects.all()

  current_user = request.user
  if request.method == 'POST':
    form = ShareForm(request.POST)
    if form.is_valid():
      home = form.save(commit=False)
      home.save()
    return redirect('home')
  else:
    form = ShareForm()

  
  context ={
    'share':share,
    'form':form,

  }
  return render(request,'home.html',context)

@login_required(login_url='/accounts/login/')
def facts(request):

  return render(request,'facts.html')