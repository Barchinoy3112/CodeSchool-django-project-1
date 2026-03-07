from django.shortcuts import render

# Create your views here.
def home(request):
    text = 'This is the text for the home page.'
    context = {'text': text}
    return render(request, 'home.html', context)