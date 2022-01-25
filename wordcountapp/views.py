from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def counter(request):
    text=request.POST['text']
    total_word = len(text.split())
    return render(request, 'counter.html', {'total_word':total_word})