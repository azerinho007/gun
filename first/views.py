from django.shortcuts import render

# Create your views here.

def first(request):
    return render(request,template_name='index.html')

def cnn(request):
    return render(request,template_name='cnn.html')

def rnn(request):
    return render(request,template_name='rnn.html')

def crnn(request):
    return render(request,template_name='cnn-rnn.html')

def work(request):
    return render(request, template_name='work.html')