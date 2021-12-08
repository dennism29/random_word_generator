from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def generate(request):
    request.session['iteration'] += 1
    request.session['random_word'] = get_random_string(length=14).upper()
    return redirect('/')

def index(request):
    if 'iteration' not in request.session:
        return redirect('/reset/')
    return render(request, 'index.html')

def reset(request):
    request.session['iteration'] = 0
    return redirect('/')
